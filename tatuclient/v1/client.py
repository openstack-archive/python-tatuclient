# Copyright 2015 Hewlett-Packard Development Company, L.P.
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
from keystoneauth1 import adapter

from tatuclient import exceptions
from tatuclient.v1.ca import CAController
from tatuclient.v1.hostcert import HostCeretController
from tatuclient.v1.usercert import UserCeretController
from tatuclient import version


class TatuAdapter(adapter.LegacyJsonAdapter):
    """Adapter around LegacyJsonAdapter.

    The user can pass a timeout keyword that will apply only to
    the Tatu Client, in order:

    - timeout keyword passed to ``request()``
    - timeout attribute on keystone session
    """
    def __init__(self, *args, **kwargs):
        self.timeout = kwargs.pop('timeout', None)
        self.all_projects = kwargs.pop('all_projects', False)
        self.sudo_project_id = kwargs.pop('sudo_project_id', None)
        super(self.__class__, self).__init__(*args, **kwargs)

    def request(self, *args, **kwargs):
        kwargs.setdefault('raise_exc', False)

        if self.timeout is not None:
            kwargs.setdefault('timeout', self.timeout)

        kwargs.setdefault('headers', {})

        if self.all_projects:
            kwargs['headers'].setdefault(
                'X-Auth-All-Projects',
                str(self.all_projects)
            )

        if self.sudo_project_id is not None:
            kwargs['headers'].setdefault(
                'X-Auth-Sudo-Project-ID',
                self.sudo_project_id
            )

        kwargs['headers'].setdefault(
            'Content-Type', 'application/json')

        response, body = super(self.__class__, self).request(*args, **kwargs)

        # Decode is response, if possible
        try:
            response_payload = response.json()
        except ValueError:
            response_payload = {}
            body = response.text

        if response.status_code == 400:
            raise exceptions.BadRequest(**response_payload)
        elif response.status_code in (401, 403):
            raise exceptions.Forbidden(**response_payload)
        elif response.status_code == 404:
            raise exceptions.NotFound(**response_payload)
        elif response.status_code == 409:
            raise exceptions.Conflict(**response_payload)
        elif response.status_code == 413:
            raise exceptions.OverQuota(**response_payload)
        elif response.status_code >= 500:
            raise exceptions.Unknown(**response_payload)
        return response, body


class Client(object):
    def __init__(self, region_name=None, endpoint_type='publicURL',
                 extensions=None, service_type='ssh', service_name=None,
                 http_log_debug=False, session=None, auth=None, timeout=None,
                 endpoint_override=None, all_projects=False,
                 sudo_project_id=None):
        if session is None:
            raise ValueError("A session instance is required")

        self.session = TatuAdapter(
            session,
            auth=auth,
            region_name=region_name,
            service_type=service_type,
            interface=endpoint_type.rstrip('URL'),
            user_agent='python-tatuclient-%s' % version.version_info,
            version=('1'),
            endpoint_override=endpoint_override,
            timeout=timeout,
            all_projects=all_projects,
            sudo_project_id=sudo_project_id
        )

        self.ca = CAController(self)
        self.hostcert = HostCertController(self)
        self.usercert = UserCertController(self)
