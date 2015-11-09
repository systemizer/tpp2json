#!/usr/bin/env python

from distutils.core import setup

setup(
    name='tpp2json',
    version='1.0',
    description='Making the TPP machine readable',
    author='systemizer',
    author_email='dj@systemizer.me',
    url='djsystemizer.com',
    packages=["tpp2json"],
    scripts=["bin/scrape-tpp", "bin/parse-tpp"]
)
