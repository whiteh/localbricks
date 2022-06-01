# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class JobsCreate200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, job_id=None):  # noqa: E501
        """JobsCreate200Response - a model defined in OpenAPI

        :param job_id: The job_id of this JobsCreate200Response.  # noqa: E501
        :type job_id: int
        """
        self.openapi_types = {
            'job_id': int
        }

        self.attribute_map = {
            'job_id': 'job_id'
        }

        self._job_id = job_id

    @classmethod
    def from_dict(cls, dikt) -> 'JobsCreate200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The JobsCreate_200_response of this JobsCreate200Response.  # noqa: E501
        :rtype: JobsCreate200Response
        """
        return util.deserialize_model(dikt, cls)

    @property
    def job_id(self):
        """Gets the job_id of this JobsCreate200Response.

        The canonical identifier for the newly created job.  # noqa: E501

        :return: The job_id of this JobsCreate200Response.
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this JobsCreate200Response.

        The canonical identifier for the newly created job.  # noqa: E501

        :param job_id: The job_id of this JobsCreate200Response.
        :type job_id: int
        """

        self._job_id = job_id