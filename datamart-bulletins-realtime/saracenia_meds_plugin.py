#!/usr/bin/env python3

import sentry_sdk
from dotenv import dotenv_values

"""
    Basic Sarracenia plugin to load the buoy data ingestion script

    See https://github.com/MetPX/sarracenia/blob/master/doc/Prog.rst

"""

config = dotenv_values("config.ini")

TABLE_NAME = config["DB_TABLE"]

class DB_ingest(object):
    def __init__(self, parent):
        self.logger=parent.logger
        logger=self.logger
        # Init sentry
        logger.debug(config)
        
        if 'SENTRY_URL' in config and config.get('SENTRY')=='true':
            sentry_sdk.init(
            config['SENTRY_URL']
            )
            logger.debug("Sentry initialized")

        logger.debug("Buoy plugin initialized")

    def perform(self, parent):
        """
        Imports have to be inside this function
        See https://github.com/MetPX/sarracenia/blob/master/doc/Prog.rst#why-doesnt-import-work

        """
        from fm13_ingest.ingest_to_db import DBIngester
        logger=self.logger
        new_file = str(parent.new_dir + "/" + parent.msg.new_file)
        metadata = parent.msg.headers
        logger.info("Buoy ingest file: " + new_file)
        DBIngester().ingest(new_file, logger, metadata)
        return True


db_ingest = DB_ingest(self)

self.on_file = db_ingest.perform
