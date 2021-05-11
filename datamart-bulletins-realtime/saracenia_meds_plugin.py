#!/usr/bin/env python3

import sentry_sdk

"""
    Basic Sarracenia plugin to load the buoy data ingestion script

    See https://github.com/MetPX/sarracenia/blob/master/doc/Prog.rst

"""


class DB_ingest(object):
    def __init__(self, parent):
        # Init sentry
        sentry_sdk.init(
           config['SENTRY_URL']
        )
        parent.logger.debug("Buoy plugin initialized")

    def perform(self, parent):
        """
        Imports have to be inside this function
        See https://github.com/MetPX/sarracenia/blob/master/doc/Prog.rst#why-doesnt-import-work

        """
        from fm13_ingest.ingest_to_db import DBIngester

        new_file = str(parent.new_dir + "/" + parent.msg.new_file)
        metadata = parent.msg.headers
        parent.logger.info("Buoy ingest file: " + new_file)
        DBIngester().ingest(new_file, parent.logger, metadata)
        return True


db_ingest = DB_ingest(self)

self.on_file = db_ingest.perform
