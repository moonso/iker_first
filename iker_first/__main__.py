#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
iker_first.__main__
~~~~~~~~~~~~~~~~~~~~~
The main entry point for the command line interface.
Invoke as ``iker`` (if installed)
or ``python -m iker`` (no install required).
"""
import sys

from iker_first.cli import cli


if __name__ == '__main__':
    # exit using whatever exit code the CLI returned
    sys.exit(cli())