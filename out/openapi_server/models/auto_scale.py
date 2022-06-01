# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class AutoScale(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, min_workers=None, max_workers=None):  # noqa: E501
        """AutoScale - a model defined in OpenAPI

        :param min_workers: The min_workers of this AutoScale.  # noqa: E501
        :type min_workers: int
        :param max_workers: The max_workers of this AutoScale.  # noqa: E501
        :type max_workers: int
        """
        self.openapi_types = {
            'min_workers': int,
            'max_workers': int
        }

        self.attribute_map = {
            'min_workers': 'min_workers',
            'max_workers': 'max_workers'
        }

        self._min_workers = min_workers
        self._max_workers = max_workers

    @classmethod
    def from_dict(cls, dikt) -> 'AutoScale':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AutoScale of this AutoScale.  # noqa: E501
        :rtype: AutoScale
        """
        return util.deserialize_model(dikt, cls)

    @property
    def min_workers(self):
        """Gets the min_workers of this AutoScale.

        The minimum number of workers to which the cluster can scale down when underutilized. It is also the initial number of workers the cluster has after creation.  # noqa: E501

        :return: The min_workers of this AutoScale.
        :rtype: int
        """
        return self._min_workers

    @min_workers.setter
    def min_workers(self, min_workers):
        """Sets the min_workers of this AutoScale.

        The minimum number of workers to which the cluster can scale down when underutilized. It is also the initial number of workers the cluster has after creation.  # noqa: E501

        :param min_workers: The min_workers of this AutoScale.
        :type min_workers: int
        """

        self._min_workers = min_workers

    @property
    def max_workers(self):
        """Gets the max_workers of this AutoScale.

        The maximum number of workers to which the cluster can scale up when overloaded. max_workers must be strictly greater than min_workers.  # noqa: E501

        :return: The max_workers of this AutoScale.
        :rtype: int
        """
        return self._max_workers

    @max_workers.setter
    def max_workers(self, max_workers):
        """Sets the max_workers of this AutoScale.

        The maximum number of workers to which the cluster can scale up when overloaded. max_workers must be strictly greater than min_workers.  # noqa: E501

        :param max_workers: The max_workers of this AutoScale.
        :type max_workers: int
        """

        self._max_workers = max_workers