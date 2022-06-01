# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.dbfs_storage_info import DbfsStorageInfo
from openapi_server.models.s3_storage_info import S3StorageInfo
from openapi_server import util

from openapi_server.models.dbfs_storage_info import DbfsStorageInfo  # noqa: E501
from openapi_server.models.s3_storage_info import S3StorageInfo  # noqa: E501

class ClusterLogConf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, dbfs=None, s3=None):  # noqa: E501
        """ClusterLogConf - a model defined in OpenAPI

        :param dbfs: The dbfs of this ClusterLogConf.  # noqa: E501
        :type dbfs: DbfsStorageInfo
        :param s3: The s3 of this ClusterLogConf.  # noqa: E501
        :type s3: S3StorageInfo
        """
        self.openapi_types = {
            'dbfs': DbfsStorageInfo,
            's3': S3StorageInfo
        }

        self.attribute_map = {
            'dbfs': 'dbfs',
            's3': 's3'
        }

        self._dbfs = dbfs
        self._s3 = s3

    @classmethod
    def from_dict(cls, dikt) -> 'ClusterLogConf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ClusterLogConf of this ClusterLogConf.  # noqa: E501
        :rtype: ClusterLogConf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def dbfs(self):
        """Gets the dbfs of this ClusterLogConf.


        :return: The dbfs of this ClusterLogConf.
        :rtype: DbfsStorageInfo
        """
        return self._dbfs

    @dbfs.setter
    def dbfs(self, dbfs):
        """Sets the dbfs of this ClusterLogConf.


        :param dbfs: The dbfs of this ClusterLogConf.
        :type dbfs: DbfsStorageInfo
        """

        self._dbfs = dbfs

    @property
    def s3(self):
        """Gets the s3 of this ClusterLogConf.


        :return: The s3 of this ClusterLogConf.
        :rtype: S3StorageInfo
        """
        return self._s3

    @s3.setter
    def s3(self, s3):
        """Sets the s3 of this ClusterLogConf.


        :param s3: The s3 of this ClusterLogConf.
        :type s3: S3StorageInfo
        """

        self._s3 = s3