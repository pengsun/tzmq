#!/usr/bin/env python
""" copied from https://github.com/tensorflow/ecosystem """
from __future__ import print_function

import jinja2
import sys

if len(sys.argv) != 2:
  print("usage: {} [template-file]".format(sys.argv[0]), file=sys.stderr)
  sys.exit(1)
with open(sys.argv[1], "r") as f:
  print(jinja2.Template(f.read()).render())
