# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class IsOwner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    IS_OWNER = "IS_OWNER"
    def __init__(self):  # noqa: E501
        """IsOwner - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'IsOwner':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The IsOwner of this IsOwner.  # noqa: E501
        :rtype: IsOwner
        """
        return util.deserialize_model(dikt, cls)
