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
import os
import unittest

from random import randint


class ScenarioTests(unittest.TestCase):

    def test_fails_5_10_runs(self):
        build_num = int(os.environ.get("BUILD_NUMBER"))
        if build_num >= 5 and build_num <= 10:
            self.assertEqual("Fail", "Success")

    def test_fails_2_3_runs(self):
        build_num = int(os.environ.get("BUILD_NUMBER"))
        if build_num == 2 or build_num == 3:
            self.assertEqual("Fail", "Success")

    def test_fails_every_5_runs(self):
        build_num = int(os.environ.get("BUILD_NUMBER"))
        if build_num % 5 == 0:
            self.assertEqual("Fail", "Success")

    def test_staging_env_failures(self):
        job_name = os.environ.get("JOB_NAME")
        if "Staging" in job_name:
            if randint(0, 4) == 1:
                self.fail("A staging environment related failure")

    def test_testing_env_failures(self):
        job_name = os.environ.get("JOB_NAME")
        if "Testing" in job_name:
            if randint(0, 4) == 1:
                self.fail("A testing environment related failure")
