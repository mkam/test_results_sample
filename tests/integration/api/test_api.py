"""
Copyright 2017 Rackspace

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import requests
import unittest

from random import randint


class APITests(unittest.TestCase):

    def test_post(self):
        if randint(1, 20) == 1:
            requests.get("http://notaurl.fail")

    def test_put(self):
        if randint(1, 20) == 1:
            requests.get("http://notaurl.fail")

    def test_get(self):
        if randint(1, 20) == 1:
            requests.get("http://notaurl.fail")

    def test_get_all(self):
        if randint(1, 20) == 1:
            requests.get("http://notaurl.fail")

    def test_delete(self):
        if randint(1, 20) == 1:
            requests.get("http://notaurl.fail")

    def test_flaky_failure(self):
        if randint(1, 3) == 1:
            requests.get("http://notaurl.fail")
