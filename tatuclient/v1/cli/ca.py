#   Copyright 2017 Huawei, Inc. All rights reserved.
#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.

import argparse
import logging

from osc_lib.command import command

from tatuclient import utils
from tatuclient.v1.cli import common
from tatuclient.v1.utils import get_all


LOG = logging.getLogger(__name__)


_columns = ['auth_id', 'user_pub_key', 'host_pub_key']
_names = ['Project/CA ID', 'User Public Key', 'Host Public Key']


class ListCACommand(command.Lister):
    """List CAs"""

    def get_parser(self, prog_name):
        parser = super(ListCACommand, self).get_parser(prog_name)
        common.add_all_common_options(parser)
        return parser

    def take_action(self, parsed_args):
        client = self.app.client_manager.ssh
        common.set_all_common_headers(client, parsed_args)
        data = get_all(client.ca.list)
        return _names, (utils.get_item_properties(s, _columns) for s in data)


class ShowCACommand(command.ShowOne):
    """Show CA details"""

    def get_parser(self, prog_name):
        parser = super(ShowCACommand, self).get_parser(prog_name)
        parser.add_argument('auth_id', help="Project/CA ID")
        common.add_all_common_options(parser)
        return parser

    def take_action(self, parsed_args):
        client = self.app.client_manager.ssh
        common.set_all_common_headers(client, parsed_args)
        data = client.ca.get(parsed_args.auth_id)
        return _names, utils.get_item_properties(data, _columns)


class CreateCACommand(command.ShowOne):
    """Create new CA"""

    def get_parser(self, prog_name):
        parser = super(CreateCACommand, self).get_parser(prog_name)
        parser.add_argument('auth_id', help="Project/CA ID")
        common.add_all_common_options(parser)
        return parser

    def take_action(self, parsed_args):
        client = self.app.client_manager.ssh
        common.set_all_common_headers(client, parsed_args)
        data = client.ca.create(parsed_args.auth_id)
        return _names, utils.get_item_properties(data, _columns)
