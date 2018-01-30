#   Copyright 2018 Huawei, Inc. All rights reserved.
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

_columns = ['serial', 'revoked', 'user_id', 'auth_id', 'fingerprint']
_names = ['Serial Number', 'Revoked', 'User ID', 'Project/CA ID', 'Fingerprint']


class ListUserCertCommand(command.Lister):
    """List UserCerts"""

    def get_parser(self, prog_name):
        parser = super(ListUserCertCommand, self).get_parser(prog_name)
        common.add_all_common_options(parser)
        return parser

    def take_action(self, parsed_args):
        client = self.app.client_manager.ssh
        common.set_all_common_headers(client, parsed_args)
        data = get_all(client.usercert.list)
        return _names, (utils.get_item_properties(s, _columns) for s in data)


class ShowUserCertCommand(command.ShowOne):
    """Show UserCert details"""

    def get_parser(self, prog_name):
        parser = super(ShowUserCertCommand, self).get_parser(prog_name)
        parser.add_argument('serial', help="Serial Number")
        common.add_all_common_options(parser)
        return parser

    def _get_data(self, parsed_args):
        client = self.app.client_manager.ssh
        common.set_all_common_headers(client, parsed_args)
        return client.usercert.get(parsed_args.serial)

    def take_action(self, parsed_args):
        data = self._get_data(parsed_args)
        return (_names + ['Certificate'],
                utils.get_item_properties(data, _columns + ['cert']))


class CreateUserCertCommand(command.ShowOne):
    """Create new UserCert"""

    def get_parser(self, prog_name):
        parser = super(CreateUserCertCommand, self).get_parser(prog_name)
        parser.add_argument('pub_key', help="Public Key")
        common.add_all_common_options(parser)
        return parser

    def take_action(self, parsed_args):
        client = self.app.client_manager.ssh
        common.set_all_common_headers(client, parsed_args)
        data = client.usercert.create(client.session.get_user_id(),
                                      client.session.get_project_id(),
                                      parsed_args.pub_key)
        return (_names + ['Certificate'],
                utils.get_item_properties(data, _columns + ['cert']))


class RevokeUserCertCommand(command.ShowOne):
    """Create new UserCert"""

    def get_parser(self, prog_name):
        parser = super(RevokeUserCertCommand, self).get_parser(prog_name)
        parser.add_argument('auth_id', help="Project/CA ID")
        parser.add_argument('serial', help="Serial Number")
        common.add_all_common_options(parser)
        return parser

    def take_action(self, parsed_args):
        client = self.app.client_manager.ssh
        common.set_all_common_headers(client, parsed_args)
        data = client.usercert.revoke(parsed_args.auth_id, parsed_args.serial)
        return _names, utils.get_item_properties(data, _columns)
