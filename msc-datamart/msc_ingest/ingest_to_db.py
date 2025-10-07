'''

Script that is run by a sarracenia plugin when new buoy data is received, inserts parsed XML into postgres database table `swob_marine`


See docs at https://dd4.weather.gc.ca/observations/doc/

'''

# TODO add logging
# TODO could auto-create table here

import os
import click
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.dialects.postgresql import insert
from msc_ingest.parse_xml import buoy_xml_to_json

buoy_filename = "buoy_list.txt"

db_string = "postgres://user:password@db.org:5432/dbname"
TABLE_NAME = 'swob_marine'

db = create_engine(db_string)

# load existing swob table columns list
swob_table_meta = MetaData(db)
swob_table = Table(TABLE_NAME, swob_table_meta, autoload=True)
table_columns = swob_table.columns


def insert_into_db(line):
    'inserts dictionary into DB'
    insertstmt = insert(swob_table).values(line)

    stmt = insertstmt.on_conflict_do_update(
        index_elements=[swob_table.c.wmo_synop_id, swob_table.c.sampling_time],
        set_=line
    )

    return db.execute(stmt)


def remove_and_log_uninsertable_keys(line):
    '''Remove and report any fields that are in the XML but arent in the database
       This shouldnt be needed, but just in case a new field is added at the source before
       we have a chance to add the column to the DB
    '''

    for k in list(line.keys()):
        if k not in table_columns:
            print(f"Cannot insert {k}")
            del line[k]


def read_buoys_list(filename):
    file = open(filename)
    buoys_list = file.read().strip().split('\n')
    file.close()
    return buoys_list


def ingest_buoy_xml_file(filename):
    'Insert buoy data in XML format into a database'

    this_dir = os.path.dirname(os.path.realpath(__file__))

    buoys_list = read_buoys_list(this_dir + '/' + buoy_filename)

    # get a flat dictionary from the source XML
    buoy_record = buoy_xml_to_json(filename)

    #if buoy_record['wmo_synop_id'] not in buoys_list:
    #    print(
    #        f"Buoy {buoy_record['wmo_synop_id']} not in: {' '.join(buoys_list)}  ")
    #    return

    # remove and print extra fields that our table doesn't have (yet)
    # probably not necessary if we keep an eye on the mailing lists
    remove_and_log_uninsertable_keys(buoy_record)

    # insert the record
    return insert_into_db(buoy_record)


@click.command()
@click.argument('filename', type=click.Path(exists=True))
def main(filename):

    res = ingest_buoy_xml_file(filename)

    if res:
        print(f'{res.rowcount} rows update or inserted in table "{TABLE_NAME}"')


if __name__ == '__main__':
    main()
