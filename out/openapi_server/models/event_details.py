# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.aws_attributes import AwsAttributes
from openapi_server.models.cluster_size import ClusterSize
from openapi_server.models.resize_cause import ResizeCause
from openapi_server.models.termination_reason import TerminationReason
from openapi_server import util

from openapi_server.models.aws_attributes import AwsAttributes  # noqa: E501
from openapi_server.models.cluster_size import ClusterSize  # noqa: E501
from openapi_server.models.resize_cause import ResizeCause  # noqa: E501
from openapi_server.models.termination_reason import TerminationReason  # noqa: E501

class EventDetails(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, current_num_workers=None, target_num_workers=None, previous_attributes=None, attributes=None, previous_cluster_size=None, cluster_size=None, cause=None, reason=None, user=None):  # noqa: E501
        """EventDetails - a model defined in OpenAPI

        :param current_num_workers: The current_num_workers of this EventDetails.  # noqa: E501
        :type current_num_workers: int
        :param target_num_workers: The target_num_workers of this EventDetails.  # noqa: E501
        :type target_num_workers: int
        :param previous_attributes: The previous_attributes of this EventDetails.  # noqa: E501
        :type previous_attributes: AwsAttributes
        :param attributes: The attributes of this EventDetails.  # noqa: E501
        :type attributes: AwsAttributes
        :param previous_cluster_size: The previous_cluster_size of this EventDetails.  # noqa: E501
        :type previous_cluster_size: ClusterSize
        :param cluster_size: The cluster_size of this EventDetails.  # noqa: E501
        :type cluster_size: ClusterSize
        :param cause: The cause of this EventDetails.  # noqa: E501
        :type cause: ResizeCause
        :param reason: The reason of this EventDetails.  # noqa: E501
        :type reason: TerminationReason
        :param user: The user of this EventDetails.  # noqa: E501
        :type user: str
        """
        self.openapi_types = {
            'current_num_workers': int,
            'target_num_workers': int,
            'previous_attributes': AwsAttributes,
            'attributes': AwsAttributes,
            'previous_cluster_size': ClusterSize,
            'cluster_size': ClusterSize,
            'cause': ResizeCause,
            'reason': TerminationReason,
            'user': str
        }

        self.attribute_map = {
            'current_num_workers': 'current_num_workers',
            'target_num_workers': 'target_num_workers',
            'previous_attributes': 'previous_attributes',
            'attributes': 'attributes',
            'previous_cluster_size': 'previous_cluster_size',
            'cluster_size': 'cluster_size',
            'cause': 'cause',
            'reason': 'reason',
            'user': 'user'
        }

        self._current_num_workers = current_num_workers
        self._target_num_workers = target_num_workers
        self._previous_attributes = previous_attributes
        self._attributes = attributes
        self._previous_cluster_size = previous_cluster_size
        self._cluster_size = cluster_size
        self._cause = cause
        self._reason = reason
        self._user = user

    @classmethod
    def from_dict(cls, dikt) -> 'EventDetails':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EventDetails of this EventDetails.  # noqa: E501
        :rtype: EventDetails
        """
        return util.deserialize_model(dikt, cls)

    @property
    def current_num_workers(self):
        """Gets the current_num_workers of this EventDetails.

        The number of nodes in the cluster.  # noqa: E501

        :return: The current_num_workers of this EventDetails.
        :rtype: int
        """
        return self._current_num_workers

    @current_num_workers.setter
    def current_num_workers(self, current_num_workers):
        """Sets the current_num_workers of this EventDetails.

        The number of nodes in the cluster.  # noqa: E501

        :param current_num_workers: The current_num_workers of this EventDetails.
        :type current_num_workers: int
        """

        self._current_num_workers = current_num_workers

    @property
    def target_num_workers(self):
        """Gets the target_num_workers of this EventDetails.

        The targeted number of nodes in the cluster.  # noqa: E501

        :return: The target_num_workers of this EventDetails.
        :rtype: int
        """
        return self._target_num_workers

    @target_num_workers.setter
    def target_num_workers(self, target_num_workers):
        """Sets the target_num_workers of this EventDetails.

        The targeted number of nodes in the cluster.  # noqa: E501

        :param target_num_workers: The target_num_workers of this EventDetails.
        :type target_num_workers: int
        """

        self._target_num_workers = target_num_workers

    @property
    def previous_attributes(self):
        """Gets the previous_attributes of this EventDetails.


        :return: The previous_attributes of this EventDetails.
        :rtype: AwsAttributes
        """
        return self._previous_attributes

    @previous_attributes.setter
    def previous_attributes(self, previous_attributes):
        """Sets the previous_attributes of this EventDetails.


        :param previous_attributes: The previous_attributes of this EventDetails.
        :type previous_attributes: AwsAttributes
        """

        self._previous_attributes = previous_attributes

    @property
    def attributes(self):
        """Gets the attributes of this EventDetails.


        :return: The attributes of this EventDetails.
        :rtype: AwsAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this EventDetails.


        :param attributes: The attributes of this EventDetails.
        :type attributes: AwsAttributes
        """

        self._attributes = attributes

    @property
    def previous_cluster_size(self):
        """Gets the previous_cluster_size of this EventDetails.


        :return: The previous_cluster_size of this EventDetails.
        :rtype: ClusterSize
        """
        return self._previous_cluster_size

    @previous_cluster_size.setter
    def previous_cluster_size(self, previous_cluster_size):
        """Sets the previous_cluster_size of this EventDetails.


        :param previous_cluster_size: The previous_cluster_size of this EventDetails.
        :type previous_cluster_size: ClusterSize
        """

        self._previous_cluster_size = previous_cluster_size

    @property
    def cluster_size(self):
        """Gets the cluster_size of this EventDetails.


        :return: The cluster_size of this EventDetails.
        :rtype: ClusterSize
        """
        return self._cluster_size

    @cluster_size.setter
    def cluster_size(self, cluster_size):
        """Sets the cluster_size of this EventDetails.


        :param cluster_size: The cluster_size of this EventDetails.
        :type cluster_size: ClusterSize
        """

        self._cluster_size = cluster_size

    @property
    def cause(self):
        """Gets the cause of this EventDetails.


        :return: The cause of this EventDetails.
        :rtype: ResizeCause
        """
        return self._cause

    @cause.setter
    def cause(self, cause):
        """Sets the cause of this EventDetails.


        :param cause: The cause of this EventDetails.
        :type cause: ResizeCause
        """

        self._cause = cause

    @property
    def reason(self):
        """Gets the reason of this EventDetails.


        :return: The reason of this EventDetails.
        :rtype: TerminationReason
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this EventDetails.


        :param reason: The reason of this EventDetails.
        :type reason: TerminationReason
        """

        self._reason = reason

    @property
    def user(self):
        """Gets the user of this EventDetails.

        The user that caused the event to occur. (Empty if it was done by Databricks.)  # noqa: E501

        :return: The user of this EventDetails.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this EventDetails.

        The user that caused the event to occur. (Empty if it was done by Databricks.)  # noqa: E501

        :param user: The user of this EventDetails.
        :type user: str
        """

        self._user = user
