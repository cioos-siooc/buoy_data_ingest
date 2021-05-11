#!/usr/bin/env python3

from distutils.core import setup

setup(
    name="msc_ingest",
    version="1.0",
    description="MSC SWOB-ML buoy data to database",
    author="Nate Rosenstock",
    author_email="nate.rosenstock@hakai.org",
    packages=["msc_ingest"],
    url="",
    include_package_data=True,
    install_requires=[
        "metpx-sarracenia",
        "psycopg2-binary",
        "xmltodict",
        "sqlalchemy",
        "paramiko",
        "click",
        "python-dotenv"
    ],
)
