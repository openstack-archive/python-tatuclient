# Copyright 2014 Hewlett-Packard Development Company, L.P.
#
# Author: Endre Karlson <endre.karlson@hp.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""OpenStackClient plugin for SSH service."""

from osc_lib import utils as oscutils

from tatuclient import shell


DEFAULT_API_VERSION = '1'

API_NAME = 'ssh'
API_VERSION_OPTION = 'os_ssh_api_version'
API_VERSIONS = {
    '1': 'tatuclient.v1.client.Client',
}


def make_client(instance):
    cls = oscutils.get_client_class(
        API_NAME, instance._api_version[API_NAME],
        API_VERSIONS)
    kwargs = oscutils.build_kwargs_dict('endpoint_type', instance._interface)

    return cls(session=instance.session,
               region_name=instance._region_name, **kwargs)


def build_option_parser(parser):
    """Hook to add global options."""
    parser.add_argument(
        '--os-ssh-api-version',
        metavar='<ssh-api-version>',
        default=shell.env('OS_SSH_API_VERSION', default="1"),
        help='SSH API version, default=' +
             DEFAULT_API_VERSION +
             ' (Env: OS_SSH_API_VERSION)')

    return parser
