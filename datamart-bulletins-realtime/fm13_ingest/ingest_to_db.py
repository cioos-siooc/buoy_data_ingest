#!/usr/bin/env python3

import arrow
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.dialects.postgresql import insert
from fm13_ingest.decode_fm13 import decode
import sentry_sdk

import configparser


"""

This file takes a JSON document and inserts it into a Postgres database

"""
from dotenv import dotenv_values

config = dotenv_values("db.ini") 

TABLE_NAME = config['DB_TABLE']

class DBIngester(object):
    def __init__(self):

        # Init sentry
        sentry_sdk.init(
            config['SENTRY_URL']
        )

        self.TABLE_NAME = TABLE_NAME
        # setup DB
        self.db = create_engine(config['DB_CONNECTION'])
        table_meta = MetaData(self.db)
        table = Table(TABLE_NAME, table_meta, autoload=True)
        self.table_columns = table.columns
        self.table = table

    def insert_into_db(self, line: dict) -> dict:
        "inserts dictionary into DB"

        # load existing table columns list

        insertstmt = insert(self.table).values(line)

        stmt = insertstmt.on_conflict_do_update(
            index_elements=[self.table.c.station_id, self.table.c.result_time],
            set_=line,
        )

        return self.db.execute(stmt)

    def remove_and_log_uninsertable_keys(self, line):
        """Remove and report any fields that are in the XML but arent in the
        database. This shouldnt be needed, but just in case a new field is
        added at the source before we have a chance to add the column to
        the DB
        """

        for k in list(line.keys()):
            if k not in self.table_columns:
                print(f"Cannot insert {k}")
                del line[k]

    def ingest(self, filename: str, logger, metadata={}):
        """Ingest FM13 file to database. Also gets some metadata from AMQP"""
        with open(filename) as file:
            lines = file.read()
            record = decode(lines)

            if not record["station_id"]:
                logger.info("skipping record, no station ID (not a buoy?)")
                return None
            if "hour" in record and "day" in record:
                # buoy reported day
                try:
                    day = int(record.get("day", 1))

                    # buoy reported hour, doesnt have minutes/month/year
                    hour = int(record.get("hour", 1))

                    record["observation_time"] = str(
                        arrow.utcnow().replace(
                            day=day, hour=hour, minute=0, second=0, microsecond=0
                        )
                    )
                except Exception:
                    return None
            # sundew_extension just contains some extra metadata
            # Note: cant test this from command line easily
            if "sundew_extension" in metadata:
                splat = metadata["sundew_extension"].split(":")
                office = splat[1]
                date_raw = splat[5]

                record["result_time"] = str(arrow.get(date_raw, "YYYYMMDDHHmmss"))
                record["headers"] = metadata
                record["headers"]["sundew"] = splat
                record["office"] = office

            self.remove_and_log_uninsertable_keys(record)

            res = self.insert_into_db(record)

            if res:
                print(res.rowcount, "rows update or inserted in table", TABLE_NAME)
                return res.rowcount
            return None