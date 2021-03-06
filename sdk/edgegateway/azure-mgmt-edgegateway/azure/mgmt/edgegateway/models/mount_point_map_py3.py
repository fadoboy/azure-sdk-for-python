# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MountPointMap(Model):
    """The share mount point.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param share_id: Required. ID of the share mounted to the role VM.
    :type share_id: str
    :ivar role_id: ID of the role to which share is mounted.
    :vartype role_id: str
    :ivar mount_point: Mount point for the share.
    :vartype mount_point: str
    :ivar role_type: Role type. Possible values include: 'IOT', 'ASA',
     'Functions', 'Cognitive'
    :vartype role_type: str or ~azure.mgmt.edgegateway.models.RoleTypes
    """

    _validation = {
        'share_id': {'required': True},
        'role_id': {'readonly': True},
        'mount_point': {'readonly': True},
        'role_type': {'readonly': True},
    }

    _attribute_map = {
        'share_id': {'key': 'shareId', 'type': 'str'},
        'role_id': {'key': 'roleId', 'type': 'str'},
        'mount_point': {'key': 'mountPoint', 'type': 'str'},
        'role_type': {'key': 'roleType', 'type': 'str'},
    }

    def __init__(self, *, share_id: str, **kwargs) -> None:
        super(MountPointMap, self).__init__(**kwargs)
        self.share_id = share_id
        self.role_id = None
        self.mount_point = None
        self.role_type = None
