#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from __future__ import unicode_literals
from routes import generate_hello_world


def test_generate_hello_world():
    ('calling routes.generate_hello_world should return a dictionary')

    # Given that I call generate_hello_world
    result = generate_hello_world()

    # When I check the result

    # Then it should be a dictionary
    result.should.be.a(dict)

    # And it should have one key: hello: world
    result.should.equal({'hello': 'world'})
