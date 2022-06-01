# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.dbfs_storage_info import DbfsStorageInfo
from openapi_server.models.file_storage_info import FileStorageInfo
from openapi_server.models.s3_storage_info import S3StorageInfo
from openapi_server import util

from openapi_server.models.dbfs_storage_info import DbfsStorageInfo  # noqa: E501
from openapi_server.models.file_storage_info import FileStorageInfo  # noqa: E501
from openapi_server.models.s3_storage_info import S3StorageInfo  # noqa: E501

class InitScriptInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, dbfs=None, file=None, s3=None):  # noqa: E501
        """InitScriptInfo - a model defined in OpenAPI

        :param dbfs: The dbfs of this InitScriptInfo.  # noqa: E501
        :type dbfs: DbfsStorageInfo
        :param file: The file of this InitScriptInfo.  # noqa: E501
        :type file: FileStorageInfo
        :param s3: The s3 of this InitScriptInfo.  # noqa: E501
        :type s3: S3StorageInfo
        """
        self.openapi_types = {
            'dbfs': DbfsStorageInfo,
            'file': FileStorageInfo,
            's3': S3StorageInfo
        }

        self.attribute_map = {
            'dbfs': 'dbfs',
            'file': 'file',
            's3': 'S3'
        }

        self._dbfs = dbfs
        self._file = file
        self._s3 = s3

    @classmethod
    def from_dict(cls, dikt) -> 'InitScriptInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The InitScriptInfo of this InitScriptInfo.  # noqa: E501
        :rtype: InitScriptInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def dbfs(self):
        """Gets the dbfs of this InitScriptInfo.


        :return: The dbfs of this InitScriptInfo.
        :rtype: DbfsStorageInfo
        """
        return self._dbfs

    @dbfs.setter
    def dbfs(self, dbfs):
        """Sets the dbfs of this InitScriptInfo.


        :param dbfs: The dbfs of this InitScriptInfo.
        :type dbfs: DbfsStorageInfo
        """

        self._dbfs = dbfs

    @property
    def file(self):
        """Gets the file of this InitScriptInfo.


        :return: The file of this InitScriptInfo.
        :rtype: FileStorageInfo
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this InitScriptInfo.


        :param file: The file of this InitScriptInfo.
        :type file: FileStorageInfo
        """

        self._file = file

    @property
    def s3(self):
        """Gets the s3 of this InitScriptInfo.


        :return: The s3 of this InitScriptInfo.
        :rtype: S3StorageInfo
        """
        return self._s3

    @s3.setter
    def s3(self, s3):
        """Sets the s3 of this InitScriptInfo.


        :param s3: The s3 of this InitScriptInfo.
        :type s3: S3StorageInfo
        """

        self._s3 = s3