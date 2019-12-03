#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# flake8: noqa
#

from __future__ import unicode_literals
from tumbler.core import Web
from sure import scenario
import routes


def before_each_test(context):
    context.web = Web()
    context.http = context.web.flask_app.test_client()


def after_each_test(context):
    # I would clean up the database here, if I had one
    pass

restful_api_test = scenario(before_each_test, after_each_test)
