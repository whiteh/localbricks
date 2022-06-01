# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class PipelineTask(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, pipeline_id=None):  # noqa: E501
        """PipelineTask - a model defined in OpenAPI

        :param pipeline_id: The pipeline_id of this PipelineTask.  # noqa: E501
        :type pipeline_id: str
        """
        self.openapi_types = {
            'pipeline_id': str
        }

        self.attribute_map = {
            'pipeline_id': 'pipeline_id'
        }

        self._pipeline_id = pipeline_id

    @classmethod
    def from_dict(cls, dikt) -> 'PipelineTask':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PipelineTask of this PipelineTask.  # noqa: E501
        :rtype: PipelineTask
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pipeline_id(self):
        """Gets the pipeline_id of this PipelineTask.

        The full name of the pipeline task to execute.  # noqa: E501

        :return: The pipeline_id of this PipelineTask.
        :rtype: str
        """
        return self._pipeline_id

    @pipeline_id.setter
    def pipeline_id(self, pipeline_id):
        """Sets the pipeline_id of this PipelineTask.

        The full name of the pipeline task to execute.  # noqa: E501

        :param pipeline_id: The pipeline_id of this PipelineTask.
        :type pipeline_id: str
        """

        self._pipeline_id = pipeline_id