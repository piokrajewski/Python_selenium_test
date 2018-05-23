#!/usr/bin/env bash
set -e

. ~ /usr/bin/python3.6

PYTHONPATH=. python -m pystache.commands.test
