# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Lint as: python3
"""Stub API calls used in kms.py for testing.

Instead of doing real API calls, we return test JSON data.
"""

# pylint: disable=unused-argument
# pylint: disable=invalid-name

import json
import pathlib

from gcp_doctor import utils

PREFIX_GKE1 = pathlib.Path(__file__).parents[2] / 'test-data/gke1/json-dumps'


class KmsApiStub:
  """Mock object to simulate container api calls."""

  def projects(self):
    return self

  def locations(self):
    return self

  def keyRings(self):
    return self

  def cryptoKeys(self):
    return self

  def get(self, name=None):
    self.name = name
    return self

  def execute(self, num_retries=0):
    name = '{}{}'.format(
        utils.extract_value_from_res_name(self.name, 'cryptoKeys'), '.json')
    with open(PREFIX_GKE1 / name) as json_file:
      return json.load(json_file)


def get_api_stub(service_name: str, version: str, project_id: str = None):
  del project_id
  return KmsApiStub()
