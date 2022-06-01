# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class PythonPyPiLibrary(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, package=None, repo=None):  # noqa: E501
        """PythonPyPiLibrary - a model defined in OpenAPI

        :param package: The package of this PythonPyPiLibrary.  # noqa: E501
        :type package: str
        :param repo: The repo of this PythonPyPiLibrary.  # noqa: E501
        :type repo: str
        """
        self.openapi_types = {
            'package': str,
            'repo': str
        }

        self.attribute_map = {
            'package': 'package',
            'repo': 'repo'
        }

        self._package = package
        self._repo = repo

    @classmethod
    def from_dict(cls, dikt) -> 'PythonPyPiLibrary':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PythonPyPiLibrary of this PythonPyPiLibrary.  # noqa: E501
        :rtype: PythonPyPiLibrary
        """
        return util.deserialize_model(dikt, cls)

    @property
    def package(self):
        """Gets the package of this PythonPyPiLibrary.

        The name of the PyPI package to install. An optional exact version specification is also supported. Examples: `simplejson` and `simplejson==3.8.0`. This field is required.  # noqa: E501

        :return: The package of this PythonPyPiLibrary.
        :rtype: str
        """
        return self._package

    @package.setter
    def package(self, package):
        """Sets the package of this PythonPyPiLibrary.

        The name of the PyPI package to install. An optional exact version specification is also supported. Examples: `simplejson` and `simplejson==3.8.0`. This field is required.  # noqa: E501

        :param package: The package of this PythonPyPiLibrary.
        :type package: str
        """
        if package is None:
            raise ValueError("Invalid value for `package`, must not be `None`")  # noqa: E501

        self._package = package

    @property
    def repo(self):
        """Gets the repo of this PythonPyPiLibrary.

        The repository where the package can be found. If not specified, the default pip index is used.  # noqa: E501

        :return: The repo of this PythonPyPiLibrary.
        :rtype: str
        """
        return self._repo

    @repo.setter
    def repo(self, repo):
        """Sets the repo of this PythonPyPiLibrary.

        The repository where the package can be found. If not specified, the default pip index is used.  # noqa: E501

        :param repo: The repo of this PythonPyPiLibrary.
        :type repo: str
        """

        self._repo = repo