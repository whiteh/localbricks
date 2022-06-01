# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.auto_scale import AutoScale
from openapi_server import util

from openapi_server.models.auto_scale import AutoScale  # noqa: E501

class ClusterSize(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, num_workers=None, autoscale=None):  # noqa: E501
        """ClusterSize - a model defined in OpenAPI

        :param num_workers: The num_workers of this ClusterSize.  # noqa: E501
        :type num_workers: int
        :param autoscale: The autoscale of this ClusterSize.  # noqa: E501
        :type autoscale: AutoScale
        """
        self.openapi_types = {
            'num_workers': int,
            'autoscale': AutoScale
        }

        self.attribute_map = {
            'num_workers': 'num_workers',
            'autoscale': 'autoscale'
        }

        self._num_workers = num_workers
        self._autoscale = autoscale

    @classmethod
    def from_dict(cls, dikt) -> 'ClusterSize':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ClusterSize of this ClusterSize.  # noqa: E501
        :rtype: ClusterSize
        """
        return util.deserialize_model(dikt, cls)

    @property
    def num_workers(self):
        """Gets the num_workers of this ClusterSize.

        If num_workers, number of worker nodes that this cluster must have. A cluster has one Spark driver and num_workers executors for a total of num_workers + 1 Spark nodes. When reading the properties of a cluster, this field reflects the desired number of workers rather than the actual number of workers. For instance, if a cluster is resized from 5 to 10 workers, this field is updated to reflect the target size of 10 workers, whereas the workers listed in executors gradually increase from 5 to 10 as the new nodes are provisioned.  # noqa: E501

        :return: The num_workers of this ClusterSize.
        :rtype: int
        """
        return self._num_workers

    @num_workers.setter
    def num_workers(self, num_workers):
        """Sets the num_workers of this ClusterSize.

        If num_workers, number of worker nodes that this cluster must have. A cluster has one Spark driver and num_workers executors for a total of num_workers + 1 Spark nodes. When reading the properties of a cluster, this field reflects the desired number of workers rather than the actual number of workers. For instance, if a cluster is resized from 5 to 10 workers, this field is updated to reflect the target size of 10 workers, whereas the workers listed in executors gradually increase from 5 to 10 as the new nodes are provisioned.  # noqa: E501

        :param num_workers: The num_workers of this ClusterSize.
        :type num_workers: int
        """

        self._num_workers = num_workers

    @property
    def autoscale(self):
        """Gets the autoscale of this ClusterSize.


        :return: The autoscale of this ClusterSize.
        :rtype: AutoScale
        """
        return self._autoscale

    @autoscale.setter
    def autoscale(self, autoscale):
        """Sets the autoscale of this ClusterSize.


        :param autoscale: The autoscale of this ClusterSize.
        :type autoscale: AutoScale
        """

        self._autoscale = autoscale
