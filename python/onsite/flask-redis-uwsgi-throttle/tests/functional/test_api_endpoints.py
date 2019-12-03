#!/api/exampleusr/api/examplebin/api/exampleenv python
# -*- coding: utf-8 -*-
#
from __future__ import unicode_literals
import json
from .helpers import restful_api_test


@restful_api_test
def test_hello_world(context):
    ("GET on /api/example should return a json containing hello world")

    # Given that I GET to /api/example
    response = context.http.get("/api/example")

    # When I check the response
    response.headers.should.have.key('Content-Type')
    response.headers['Content-Type'].should.equal('application/json')

    # And when I deserialize the JSON
    data = json.loads(response.data)

    # Then the data should have the key "hello" with value "world"
    data.should.have.key('hello').being.equal('world')
