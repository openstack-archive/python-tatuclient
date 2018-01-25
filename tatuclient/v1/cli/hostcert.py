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
'host_id': host.host_id,
'fingerprint': host.fingerprint,
'auth_id': host.auth_id,
'cert': host.cert,
item = {
    'host_id': host.host_id,
    'fingerprint': host.fingerprint,
    'auth_id': host.auth_id,
    'cert': host.cert,
    'hostname': host.hostname,
}
if CONF.tatu.use_pat_bastions:
    item['pat_bastions'] = ','.join(
        '{}:{}'.format(t[1], t[0]) for t in
        get_port_ip_tuples(host.host_id, 22))
    item['srv_url'] = get_srv_url(host.hostname, host.auth_id)

_columns = ['host_id', 'srv_url', 'pat_bastions', 'fingerprint', 'cert']
_names = ['Instance ID', 'SRV URL', 'PAT Bastions', 'Fingerprint', 'SSH Certificate']


class ListHostCertCommand(command.Lister):
    """List HostCerts"""

    def get_parser(self, prog_name):
        parser = super(ListHostCertCommand, self).get_parser(prog_name)
        common.add_all_common_options(parser)
        return parser

    def take_action(self, parsed_args):
        client = self.app.client_manager.ssh
        common.set_all_common_headers(client, parsed_args)
        data = get_all(client.hostcert.list)
        return _names, (utils.get_item_properties(s, _columns) for s in data)


class ShowHostCertCommand(command.ShowOne):
    """Show HostCert details"""

    def get_parser(self, prog_name):
        parser = super(ShowHostCertCommand, self).get_parser(prog_name)
        parser.add_argument('serial', help="Serial Number")
        common.add_all_common_options(parser)
        return parser

    def take_action(self, parsed_args):
        client = self.app.client_manager.ssh
        common.set_all_common_headers(client, parsed_args)
        data = client.hostcert.get(parsed_args.serial)
        return _names, utils.get_item_properties(data, _columns)
