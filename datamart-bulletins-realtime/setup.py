#!/usr/bin/env python3

from setuptools import setup

setup(
    name="fm13_ingest",
    version="1.0",
    description="",
    author="",
    author_email="",
    packages=["fm13_ingest"],
    url="",
    install_requires=[
        "xmltodict",
        "python-benedict",
        "metpx-sarracenia",
        "psycopg2-binary",
        "xmltodict",
        "sqlalchemy",
        "paramiko",
        "click",
        "arrow",
        "python-dotenv",
    ],
)
