# Copyright (c) 2021-2021 Mediapills HttpFoundation.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
import typing as t
import unittest

from mediapills.http_foundation import requests


class TestRequestsImport(unittest.TestCase):
    def test_constructor(self) -> None:
        class TestRequest(requests.BaseRequest):
            def __init__(self, *args: t.Any, **kwargs: t.Any) -> None:
                super().__init__(*args, **kwargs)

        query = {"param_q": "value_q"}
        request = {"param_r": "value_r"}
        attributes = {"param_a": "value_a"}
        cookies = {"param_c": "value_c"}
        server = {"param_c": "value_s"}
        content = "Raw dummy content"

        obj = TestRequest(query, request, attributes, cookies, server, content)

        self.assertEqual(obj.query, query)
        self.assertEqual(obj.request, request)
        self.assertEqual(obj.attributes, attributes)
        self.assertEqual(obj.cookies, cookies)
        self.assertEqual(obj.server, server)
        self.assertEqual(obj.content, content)
