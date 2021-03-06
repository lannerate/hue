#!/usr/bin/env python
# Licensed to Cloudera, Inc. under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  Cloudera, Inc. licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.utils.translation import ugettext_lazy as _t
from desktop.lib.conf import Config, UnspecifiedConfigSection,\
                             ConfigSection, coerce_json_dict
from desktop.conf import coerce_database


RDBMS = UnspecifiedConfigSection(
  key="databases",
  help=_t("RDBMS server configurations."),
  each=ConfigSection(
    help=_t("RDBMS server configuration."),
    members=dict(
      NICE_NAME=Config(
        key='nice_name',
        help=_t('Nice name of server.'),
        type=str,
        default=None,
      ),
      ENGINE=Config(
        key='engine',
        help=_t('Database engine, such as postgresql_psycopg2, mysql, or sqlite3.'),
        type=coerce_database,
        default='django.db.backends.sqlite3',
      ),
      USER=Config(
        key='user',
        help=_t('Database username.'),
        type=str,
        default='',
      ),
      PASSWORD=Config(
        key='password',
        help=_t('Database password.'),
        type=str,
        default='',
      ),
      HOST=Config(
        key='host',
        help=_t('Database host.'),
        type=str,
        default='',
      ),
      PORT=Config(
        key='port',
        help=_t('Database port.'),
        type=int,
        default=0,
      ),
      OPTIONS=Config(
        key='options',
        help=_t('Database options to send to the server when connecting.'),
        type=coerce_json_dict,
        default='{}'
      )
    )
  )
)


def config_validator(user):
  res = []
  return res


def get_server_choices():
  return [(alias, RDBMS[alias].NICE_NAME.get() or alias) for alias in RDBMS]
