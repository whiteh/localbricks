# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class TerminationType(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    SUCCESS = "SUCCESS"
    CLIENT_ERROR = "CLIENT_ERROR"
    SERVICE_FAULT = "SERVICE_FAULT"
    CLOUD_FAILURE = "CLOUD_FAILURE"
    def __init__(self):  # noqa: E501
        """TerminationType - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'TerminationType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TerminationType of this TerminationType.  # noqa: E501
        :rtype: TerminationType
        """
        return util.deserialize_model(dikt, cls)
