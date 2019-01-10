#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Akash Kothawale <akash@decached.com>
#
# Distributed under terms of the MIT license.

import json
import pystache
import sys

html = None
with open('template.html') as f:
    html = f.read()

mustache = None
with open('resume.json') as f:
    mustache = json.loads(f.read())

with open('resume.html', 'w') as f:
    f.write(pystache.render(html, mustache))
