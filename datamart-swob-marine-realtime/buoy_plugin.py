#!/usr/bin/env python3

import logging
import sarracenia.flowcb

logger = logging.getLogger(__name__)

import sentry_sdk

"""
    Basic Sarracenia plugin to load the buoy data ingestion script

    See https://github.com/MetPX/sarracenia/blob/master/doc/Prog.rst

"""


class BuoyPlugin(sarracenia.flowcb.FlowCB):
    def __init__(self, options):
        super().__init__(options, logger)
        logger.debug("Buoy plugin initialized")

    def on_start(self):
        logger.info("Buoy DB plugin started")

    def after_work(self, worklist):
        """Imports have to be here..
        See https://github.com/MetPX/sarracenia/blob/master/doc/Prog.rst#why-doesnt-import-work

        """

        from msc_ingest.ingest_to_db import ingest_buoy_xml_file

        for msg in worklist.ok:
            new_file = msg["new_file"]
            ingest_buoy_xml_file(new_file, logger)

        return True
