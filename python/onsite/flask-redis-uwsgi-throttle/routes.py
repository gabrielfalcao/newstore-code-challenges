#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from __future__ import unicode_literals

from flask import render_template
from tumbler import tumbler, json_response

route = tumbler.module(__name__)


@route.get('/')
def frontend():
    return render_template('index.html')


def generate_hello_world():
    payload = {'hello': 'world'}
    return payload


@route.get('/api/example')
def api_example_route_get():
    payload = generate_hello_world()
    return json_response(payload, 200)
