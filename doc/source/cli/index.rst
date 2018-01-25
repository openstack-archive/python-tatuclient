.. ###################################################
.. ##  WARNING  ######################################
.. ##############  WARNING  ##########################
.. ##########################  WARNING  ##############
.. ######################################  WARNING  ##
.. ###################################################
.. ###################################################
.. ##
.. This file is tool-generated. Do not edit manually.
.. http://docs.openstack.org/contributor-guide/
.. doc-tools/cli-reference.html
..                                                  ##
.. ##  WARNING  ######################################
.. ##############  WARNING  ##########################
.. ##########################  WARNING  ##############
.. ######################################  WARNING  ##
.. ###################################################

===========================================
SSH service (tatu) command-line client
===========================================

The tatu client is the command-line interface (CLI) for
the SSH service (tatu) API and its extensions.

This chapter documents :command:`tatu` version ``2.6.0``.

For help on a specific :command:`tatu` command, enter:

.. code-block:: console

   $ tatu help COMMAND

.. _tatu_command_usage:

tatu usage
~~~~~~~~~~~~~~~

.. code-block:: console

   usage: tatu [--version] [-v | -q] [--log-file LOG_FILE] [-h] [--debug]
                    [--os-username OS_USERNAME] [--os-user-id OS_USER_ID]
                    [--os-user-domain-id OS_USER_DOMAIN_ID]
                    [--os-user-domain-name OS_USER_DOMAIN_NAME]
                    [--os-password OS_PASSWORD] [--os-tenant-name OS_TENANT_NAME]
                    [--os-tenant-id OS_TENANT_ID]
                    [--os-project-name OS_PROJECT_NAME]
                    [--os-domain-name OS_DOMAIN_NAME]
                    [--os-domain-id OS_DOMAIN_ID] [--os-project-id OS_PROJECT_ID]
                    [--os-project-domain-id OS_PROJECT_DOMAIN_ID]
                    [--os-project-domain-name OS_PROJECT_DOMAIN_NAME]
                    [--os-auth-url OS_AUTH_URL] [--os-region-name OS_REGION_NAME]
                    [--os-token OS_TOKEN] [--os-endpoint OS_ENDPOINT]
                    [--os-endpoint-type OS_ENDPOINT_TYPE]
                    [--os-service-type OS_SERVICE_TYPE] [--os-cacert OS_CACERT]
                    [--insecure] [--all-tenants] [--edit-managed]

.. _tatu_command_options:

tatu optional arguments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``--version``
  show program's version number and exit

``-v, --verbose``
  Increase verbosity of output. Can be repeated.

``-q, --quiet``
  Suppress output except warnings and errors.

``--log-file LOG_FILE``
  Specify a file to log output. Disabled by default.

``-h, --help``
  Show help message and exit.

``--debug``
  Show tracebacks on errors.

``--os-username OS_USERNAME``
  Name used for authentication with the OpenStack
  Identity service. Defaults to ``env[OS_USERNAME]``.

``--os-user-id OS_USER_ID``
  User ID used for authentication with the OpenStack
  Identity service. Defaults to ``env[OS_USER_ID]``.

``--os-user-domain-id OS_USER_DOMAIN_ID``
  Defaults to ``env[OS_USER_DOMAIN_ID]``.

``--os-user-domain-name OS_USER_DOMAIN_NAME``
  Defaults to ``env[OS_USER_DOMAIN_NAME]``.

``--os-password OS_PASSWORD``
  Password used for authentication with the OpenStack
  Identity service. Defaults to ``env[OS_PASSWORD]``.

``--os-tenant-name OS_TENANT_NAME``
  Tenant to request authorization on. Defaults to
  ``env[OS_TENANT_NAME]``.

``--os-tenant-id OS_TENANT_ID``
  Tenant to request authorization on. Defaults to
  ``env[OS_TENANT_ID]``.

``--os-project-name OS_PROJECT_NAME``
  Project to request authorization on. Defaults to
  ``env[OS_PROJECT_NAME]``.

``--os-domain-name OS_DOMAIN_NAME``
  Project to request authorization on. Defaults to
  ``env[OS_DOMAIN_NAME]``.

``--os-domain-id OS_DOMAIN_ID``
  Defaults to ``env[OS_DOMAIN_ID]``.

``--os-project-id OS_PROJECT_ID``
  Project to request authorization on. Defaults to
  ``env[OS_PROJECT_ID]``.

``--os-project-domain-id OS_PROJECT_DOMAIN_ID``
  Defaults to ``env[OS_PROJECT_DOMAIN_ID]``.

``--os-project-domain-name OS_PROJECT_DOMAIN_NAME``
  Defaults to ``env[OS_PROJECT_DOMAIN_NAME]``.

``--os-auth-url OS_AUTH_URL``
  Specify the Identity endpoint to use for
  authentication. Defaults to ``env[OS_AUTH_URL]``.

``--os-region-name OS_REGION_NAME``
  Specify the region to use. Defaults to
  ``env[OS_REGION_NAME]``.

``--os-token OS_TOKEN``
  Specify an existing token to use instead of retrieving
  one via authentication (e.g. with username &
  password). Defaults to ``env[OS_SERVICE_TOKEN]``.

``--os-endpoint OS_ENDPOINT``
  Specify an endpoint to use instead of retrieving one
  from the service catalog (via authentication).
  Defaults to ``env[OS_SSH_ENDPOINT]``.

``--os-endpoint-type OS_ENDPOINT_TYPE``
  Defaults to ``env[OS_ENDPOINT_TYPE]``.

``--os-service-type OS_SERVICE_TYPE``
  Defaults to ``env[OS_SSH_SERVICE_TYPE]``, or 'ssh'.

``--os-cacert OS_CACERT``
  CA certificate bundle file. Defaults to
  ``env[OS_CACERT]``.

``--insecure``
  Explicitly allow 'insecure' SSL requests.

``--all-tenants``
  Allows to list all domains from all tenants.

``--edit-managed``
  Allows to edit records that are marked as managed.

.. _tatu_diagnostics-ping:

tatu diagnostics-ping
--------------------------

.. code-block:: console

   usage: tatu diagnostics-ping [-h] [-f {html,json,shell,table,value,yaml}]
                                     [-c COLUMN] [--max-width <integer>]
                                     [--print-empty] [--noindent]
                                     [--prefix PREFIX] --service SERVICE --host
                                     HOST

Ping a service on a given host

**Optional arguments:**

``-h, --help``
  show this help message and exit

``--service SERVICE``
  Service name (e.g. central)

``--host HOST``
  Hostname

.. _tatu_domain-create:

tatu domain-create
-----------------------

.. code-block:: console

   usage: tatu domain-create [-h] [-f {html,json,shell,table,value,yaml}]
                                  [-c COLUMN] [--max-width <integer>]
                                  [--print-empty] [--noindent] [--prefix PREFIX]
                                  --name NAME --email EMAIL [--ttl TTL]
                                  [--description DESCRIPTION]

Create Domain

**Optional arguments:**

``-h, --help``
  show this help message and exit

``--name NAME``
  Domain name.

``--email EMAIL``
  Domain email.

``--ttl TTL``
  Time to live (seconds).

``--description DESCRIPTION``
  Description.

.. _tatu_domain-delete:

tatu domain-delete
-----------------------

.. code-block:: console

   usage: tatu domain-delete [-h] [-f {html,json,shell,table,value,yaml}]
                                  [-c COLUMN] [--max-width <integer>]
                                  [--print-empty] [--noindent] [--prefix PREFIX]
                                  id

Delete Domain

**Positional arguments:**

``id``
  Domain ID or name.

**Optional arguments:**

``-h, --help``
  show this help message and exit

.. _tatu_domain-get:

tatu domain-get
--------------------

.. code-block:: console

   usage: tatu domain-get [-h] [-f {html,json,shell,table,value,yaml}]
                               [-c COLUMN] [--max-width <integer>]
                               [--print-empty] [--noindent] [--prefix PREFIX]
                               id

Get Domain

**Positional arguments:**

``id``
  Domain ID or name.

**Optional arguments:**

``-h, --help``
  show this help message and exit

.. _tatu_domain-list:

tatu domain-list
---------------------

.. code-block:: console

   usage: tatu domain-list [-h] [-f {csv,html,json,table,value,yaml}]
                                [-c COLUMN] [--max-width <integer>]
                                [--print-empty] [--noindent]
                                [--quote {all,minimal,none,nonnumeric}]

List Domains

**Optional arguments:**

``-h, --help``
  show this help message and exit

.. _tatu_domain-servers-list:

tatu domain-servers-list
-----------------------------

.. code-block:: console

   usage: tatu domain-servers-list [-h]
                                        [-f {csv,html,json,table,value,yaml}]
                                        [-c COLUMN] [--max-width <integer>]
                                        [--print-empty] [--noindent]
                                        [--quote {all,minimal,none,nonnumeric}]
                                        id

List Domain Servers

**Positional arguments:**

``id``
  Domain ID or name.

**Optional arguments:**

``-h, --help``
  show this help message and exit

.. _tatu_domain-update:

tatu domain-update
-----------------------

.. code-block:: console

   usage: tatu domain-update [-h] [-f {html,json,shell,table,value,yaml}]
                                  [-c COLUMN] [--max-width <integer>]
                                  [--print-empty] [--noindent] [--prefix PREFIX]
                                  [--name NAME] [--email EMAIL] [--ttl TTL]
                                  [--description DESCRIPTION | --no-description]
                                  id

Update Domain

**Positional arguments:**

``id``
  Domain ID or name.

**Optional arguments:**

``-h, --help``
  show this help message and exit

``--name NAME``
  Domain name.

``--email EMAIL``
  Domain email.

``--ttl TTL``
  Time to live (seconds).

``--description DESCRIPTION``
  Description.

``--no-description``

.. _tatu_quota-get:

tatu quota-get
-------------------

.. code-block:: console

   usage: tatu quota-get [-h] [-f {html,json,shell,table,value,yaml}]
                              [-c COLUMN] [--max-width <integer>] [--print-empty]
                              [--noindent] [--prefix PREFIX]
                              tenant_id

Get Quota

**Positional arguments:**

``tenant_id``
  Tenant ID

**Optional arguments:**

``-h, --help``
  show this help message and exit

.. _tatu_quota-reset:

tatu quota-reset
---------------------

.. code-block:: console

   usage: tatu quota-reset [-h] [-f {html,json,shell,table,value,yaml}]
                                [-c COLUMN] [--max-width <integer>]
                                [--print-empty] [--noindent] [--prefix PREFIX]
                                tenant_id

Reset Quota

**Positional arguments:**

``tenant_id``
  Tenant ID.

**Optional arguments:**

``-h, --help``
  show this help message and exit

.. _tatu_quota-update:

tatu quota-update
----------------------

.. code-block:: console

   usage: tatu quota-update [-h] [-f {html,json,shell,table,value,yaml}]
                                 [-c COLUMN] [--max-width <integer>]
                                 [--print-empty] [--noindent] [--prefix PREFIX]
                                 [--domains DOMAINS]
                                 [--domain-recordsets DOMAIN_RECORDSETS]
                                 [--recordset-records RECORDSET_RECORDS]
                                 [--domain-records DOMAIN_RECORDS]
                                 [--api-export-size API_EXPORT_SIZE]
                                 tenant_id

Update Quota

**Positional arguments:**

``tenant_id``
  Tenant ID.

**Optional arguments:**

``-h, --help``
  show this help message and exit

``--domains DOMAINS``
  Allowed domains.

``--domain-recordsets DOMAIN_RECORDSETS``
  Allowed domain records.

``--recordset-records RECORDSET_RECORDS``
  Allowed recordset records.

``--domain-records DOMAIN_RECORDS``
  Allowed domain records.

``--api-export-size API_EXPORT_SIZE``
  Allowed zone export recordsets.

.. _tatu_record-create:

tatu record-create
-----------------------

.. code-block:: console

   usage: tatu record-create [-h] [-f {html,json,shell,table,value,yaml}]
                                  [-c COLUMN] [--max-width <integer>]
                                  [--print-empty] [--noindent] [--prefix PREFIX]
                                  --name NAME --type TYPE --data DATA [--ttl TTL]
                                  [--priority PRIORITY]
                                  [--description DESCRIPTION]
                                  domain_id

Create Record

**Positional arguments:**

``domain_id``
  Domain ID or name.

**Optional arguments:**

``-h, --help``
  show this help message and exit

``--name NAME``
  Record (relative|absolute) name.

``--type TYPE``
  Record type.

``--data DATA``
  Record data.

``--ttl TTL``
  Record TTL.

``--priority PRIORITY``
  Record priority.

``--description DESCRIPTION``
  Description.

.. _tatu_record-delete:

tatu record-delete
-----------------------

.. code-block:: console

   usage: tatu record-delete [-h] [-f {html,json,shell,table,value,yaml}]
                                  [-c COLUMN] [--max-width <integer>]
                                  [--print-empty] [--noindent] [--prefix PREFIX]
                                  domain_id id

Delete Record

**Positional arguments:**

``domain_id``
  Domain ID or name.

``id``
  Record ID.

**Optional arguments:**

``-h, --help``
  show this help message and exit

.. _tatu_record-get:

tatu record-get
--------------------

.. code-block:: console

   usage: tatu record-get [-h] [-f {html,json,shell,table,value,yaml}]
                               [-c COLUMN] [--max-width <integer>]
                               [--print-empty] [--noindent] [--prefix PREFIX]
                               domain_id id

Get Record

**Positional arguments:**

``domain_id``
  Domain ID or name.

``id``
  Record ID.

**Optional arguments:**

``-h, --help``
  show this help message and exit

.. _tatu_record-list:

tatu record-list
---------------------

.. code-block:: console

   usage: tatu record-list [-h] [-f {csv,html,json,table,value,yaml}]
                                [-c COLUMN] [--max-width <integer>]
                                [--print-empty] [--noindent]
                                [--quote {all,minimal,none,nonnumeric}]
                                domain_id

List Records

**Positional arguments:**

``domain_id``
  Domain ID or name.

**Optional arguments:**

``-h, --help``
  show this help message and exit

.. _tatu_record-update:

tatu record-update
-----------------------

.. code-block:: console

   usage: tatu record-update [-h] [-f {html,json,shell,table,value,yaml}]
                                  [-c COLUMN] [--max-width <integer>]
                                  [--print-empty] [--noindent] [--prefix PREFIX]
                                  [--name NAME] [--type TYPE] [--data DATA]
                                  [--description DESCRIPTION | --no-description]
                                  [--ttl TTL | --no-ttl]
                                  [--priority PRIORITY | --no-priority]
                                  domain_id id

Update Record

**Positional arguments:**

``domain_id``
  Domain ID or name.

``id``
  Record ID.

**Optional arguments:**

``-h, --help``
  show this help message and exit

``--name NAME``
  Record name.

``--type TYPE``
  Record type.

``--data DATA``
  Record data.

``--description DESCRIPTION``
  Description.

``--no-description``

``--ttl TTL``
  Record time to live (seconds).

``--no-ttl``

``--priority PRIORITY``
  Record priority.

``--no-priority``

.. _tatu_report-count-all:

tatu report-count-all
--------------------------

.. code-block:: console

   usage: tatu report-count-all [-h] [-f {html,json,shell,table,value,yaml}]
                                     [-c COLUMN] [--max-width <integer>]
                                     [--print-empty] [--noindent]
                                     [--prefix PREFIX]

Get count totals for all tenants, domains and records

**Optional arguments:**

``-h, --help``
  show this help message and exit

.. _tatu_report-count-domains:

tatu report-count-domains
------------------------------

.. code-block:: console

   usage: tatu report-count-domains [-h]
                                         [-f {html,json,shell,table,value,yaml}]
                                         [-c COLUMN] [--max-width <integer>]
                                         [--print-empty] [--noindent]
                                         [--prefix PREFIX]

Get counts for total domains

**Optional arguments:**

``-h, --help``
  show this help message and exit

.. _tatu_report-count-records:

tatu report-count-records
------------------------------

.. code-block:: console

   usage: tatu report-count-records [-h]
                                         [-f {html,json,shell,table,value,yaml}]
                                         [-c COLUMN] [--max-width <integer>]
                                         [--print-empty] [--noindent]
                                         [--prefix PREFIX]

Get counts for total records

**Optional arguments:**

``-h, --help``
  show this help message and exit

.. _tatu_report-count-tenants:

tatu report-count-tenants
------------------------------

.. code-block:: console

   usage: tatu report-count-tenants [-h]
                                         [-f {html,json,shell,table,value,yaml}]
                                         [-c COLUMN] [--max-width <integer>]
                                         [--print-empty] [--noindent]
                                         [--prefix PREFIX]

Get counts for total tenants

**Optional arguments:**

``-h, --help``
  show this help message and exit

.. _tatu_report-tenant-domains:

tatu report-tenant-domains
-------------------------------

.. code-block:: console

   usage: tatu report-tenant-domains [-h]
                                          [-f {csv,html,json,table,value,yaml}]
                                          [-c COLUMN] [--max-width <integer>]
                                          [--print-empty] [--noindent]
                                          [--quote {all,minimal,none,nonnumeric}]
                                          --report-tenant-id REPORT_TENANT_ID

Get a list of domains for given tenant

**Optional arguments:**

``-h, --help``
  show this help message and exit

``--report-tenant-id REPORT_TENANT_ID``
  The tenant_id being reported on.

.. _tatu_report-tenants-all:

tatu report-tenants-all
----------------------------

.. code-block:: console

   usage: tatu report-tenants-all [-h] [-f {csv,html,json,table,value,yaml}]
                                       [-c COLUMN] [--max-width <integer>]
                                       [--print-empty] [--noindent]
                                       [--quote {all,minimal,none,nonnumeric}]

Get list of tenants and domain count for each

**Optional arguments:**

``-h, --help``
  show this help message and exit

.. _tatu_server-create:

tatu server-create
-----------------------

.. code-block:: console

   usage: tatu server-create [-h] [-f {html,json,shell,table,value,yaml}]
                                  [-c COLUMN] [--max-width <integer>]
                                  [--print-empty] [--noindent] [--prefix PREFIX]
                                  --name NAME

Create Server

**Optional arguments:**

``-h, --help``
  show this help message and exit

``--name NAME``
  Server name.

.. _tatu_server-delete:

tatu server-delete
-----------------------

.. code-block:: console

   usage: tatu server-delete [-h] [-f {html,json,shell,table,value,yaml}]
                                  [-c COLUMN] [--max-width <integer>]
                                  [--print-empty] [--noindent] [--prefix PREFIX]
                                  id

Delete Server

**Positional arguments:**

``id``
  Server ID.

**Optional arguments:**

``-h, --help``
  show this help message and exit

.. _tatu_server-get:

tatu server-get
--------------------

.. code-block:: console

   usage: tatu server-get [-h] [-f {html,json,shell,table,value,yaml}]
                               [-c COLUMN] [--max-width <integer>]
                               [--print-empty] [--noindent] [--prefix PREFIX]
                               id

Get Server

**Positional arguments:**

``id``
  Server ID.

**Optional arguments:**

``-h, --help``
  show this help message and exit

.. _tatu_server-list:

tatu server-list
---------------------

.. code-block:: console

   usage: tatu server-list [-h] [-f {csv,html,json,table,value,yaml}]
                                [-c COLUMN] [--max-width <integer>]
                                [--print-empty] [--noindent]
                                [--quote {all,minimal,none,nonnumeric}]

List Servers

**Optional arguments:**

``-h, --help``
  show this help message and exit

.. _tatu_server-update:

tatu server-update
-----------------------

.. code-block:: console

   usage: tatu server-update [-h] [-f {html,json,shell,table,value,yaml}]
                                  [-c COLUMN] [--max-width <integer>]
                                  [--print-empty] [--noindent] [--prefix PREFIX]
                                  [--name NAME]
                                  id

Update Server

**Positional arguments:**

``id``
  Server ID.

**Optional arguments:**

``-h, --help``
  show this help message and exit

``--name NAME``
  Server name.

.. _tatu_sync-all:

tatu sync-all
------------------

.. code-block:: console

   usage: tatu sync-all [-h] [-f {html,json,shell,table,value,yaml}]
                             [-c COLUMN] [--max-width <integer>] [--print-empty]
                             [--noindent] [--prefix PREFIX]

Sync Everything

**Optional arguments:**

``-h, --help``
  show this help message and exit

.. _tatu_sync-domain:

tatu sync-domain
---------------------

.. code-block:: console

   usage: tatu sync-domain [-h] [-f {html,json,shell,table,value,yaml}]
                                [-c COLUMN] [--max-width <integer>]
                                [--print-empty] [--noindent] [--prefix PREFIX]
                                domain_id

Sync a single Domain

**Positional arguments:**

``domain_id``
  Domain ID

**Optional arguments:**

``-h, --help``
  show this help message and exit

.. _tatu_sync-record:

tatu sync-record
---------------------

.. code-block:: console

   usage: tatu sync-record [-h] [-f {html,json,shell,table,value,yaml}]
                                [-c COLUMN] [--max-width <integer>]
                                [--print-empty] [--noindent] [--prefix PREFIX]
                                domain_id record_id

Sync a single Record

**Positional arguments:**

``domain_id``
  Domain ID

``record_id``
  Record ID

**Optional arguments:**

``-h, --help``
  show this help message and exit

.. _tatu_touch-domain:

tatu touch-domain
----------------------

.. code-block:: console

   usage: tatu touch-domain [-h] [-f {html,json,shell,table,value,yaml}]
                                 [-c COLUMN] [--max-width <integer>]
                                 [--print-empty] [--noindent] [--prefix PREFIX]
                                 domain_id

Touch a single Domain

**Positional arguments:**

``domain_id``
  Domain ID

**Optional arguments:**

``-h, --help``
  show this help message and exit

