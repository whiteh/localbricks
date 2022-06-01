# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class JobsRunsRepair200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, repair_id=None):  # noqa: E501
        """JobsRunsRepair200Response - a model defined in OpenAPI

        :param repair_id: The repair_id of this JobsRunsRepair200Response.  # noqa: E501
        :type repair_id: int
        """
        self.openapi_types = {
            'repair_id': int
        }

        self.attribute_map = {
            'repair_id': 'repair_id'
        }

        self._repair_id = repair_id

    @classmethod
    def from_dict(cls, dikt) -> 'JobsRunsRepair200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The JobsRunsRepair_200_response of this JobsRunsRepair200Response.  # noqa: E501
        :rtype: JobsRunsRepair200Response
        """
        return util.deserialize_model(dikt, cls)

    @property
    def repair_id(self):
        """Gets the repair_id of this JobsRunsRepair200Response.

        The ID of the repair.  # noqa: E501

        :return: The repair_id of this JobsRunsRepair200Response.
        :rtype: int
        """
        return self._repair_id

    @repair_id.setter
    def repair_id(self, repair_id):
        """Sets the repair_id of this JobsRunsRepair200Response.

        The ID of the repair.  # noqa: E501

        :param repair_id: The repair_id of this JobsRunsRepair200Response.
        :type repair_id: int
        """

        self._repair_id = repair_id
