# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.access_control_request import AccessControlRequest
from openapi_server import util

from openapi_server.models.access_control_request import AccessControlRequest  # noqa: E501

class AccessControlList(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, access_control_list=None):  # noqa: E501
        """AccessControlList - a model defined in OpenAPI

        :param access_control_list: The access_control_list of this AccessControlList.  # noqa: E501
        :type access_control_list: List[AccessControlRequest]
        """
        self.openapi_types = {
            'access_control_list': List[AccessControlRequest]
        }

        self.attribute_map = {
            'access_control_list': 'access_control_list'
        }

        self._access_control_list = access_control_list

    @classmethod
    def from_dict(cls, dikt) -> 'AccessControlList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AccessControlList of this AccessControlList.  # noqa: E501
        :rtype: AccessControlList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def access_control_list(self):
        """Gets the access_control_list of this AccessControlList.

        List of permissions to set on the job.  # noqa: E501

        :return: The access_control_list of this AccessControlList.
        :rtype: List[AccessControlRequest]
        """
        return self._access_control_list

    @access_control_list.setter
    def access_control_list(self, access_control_list):
        """Sets the access_control_list of this AccessControlList.

        List of permissions to set on the job.  # noqa: E501

        :param access_control_list: The access_control_list of this AccessControlList.
        :type access_control_list: List[AccessControlRequest]
        """

        self._access_control_list = access_control_list