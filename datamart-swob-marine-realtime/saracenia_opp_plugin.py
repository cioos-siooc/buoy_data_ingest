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
        """Imports have to be here..
        See https://github.com/MetPX/sarracenia/blob/master/doc/Prog.rst#why-doesnt-import-work

        """

        from msc_ingest.ingest_to_db import ingest_buoy_xml_file

        new_file = parent.msg.new_file
        parent.logger.info("Buoy ingest file: " + new_file)
        ingest_buoy_xml_file(new_file)

        return True


db_ingest = DB_ingest(self)

self.on_file = db_ingest.perform
