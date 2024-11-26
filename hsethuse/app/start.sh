#!/bin/bash

set -e

socat tcp-listen:5000,reuseaddr,fork SYSTEM:"python3 app.py"