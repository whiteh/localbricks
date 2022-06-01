# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class MavenLibrary(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, coordinates=None, repo=None, exclusions=None):  # noqa: E501
        """MavenLibrary - a model defined in OpenAPI

        :param coordinates: The coordinates of this MavenLibrary.  # noqa: E501
        :type coordinates: str
        :param repo: The repo of this MavenLibrary.  # noqa: E501
        :type repo: str
        :param exclusions: The exclusions of this MavenLibrary.  # noqa: E501
        :type exclusions: List[str]
        """
        self.openapi_types = {
            'coordinates': str,
            'repo': str,
            'exclusions': List[str]
        }

        self.attribute_map = {
            'coordinates': 'coordinates',
            'repo': 'repo',
            'exclusions': 'exclusions'
        }

        self._coordinates = coordinates
        self._repo = repo
        self._exclusions = exclusions

    @classmethod
    def from_dict(cls, dikt) -> 'MavenLibrary':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MavenLibrary of this MavenLibrary.  # noqa: E501
        :rtype: MavenLibrary
        """
        return util.deserialize_model(dikt, cls)

    @property
    def coordinates(self):
        """Gets the coordinates of this MavenLibrary.

        Gradle-style Maven coordinates. For example: `org.jsoup:jsoup:1.7.2`. This field is required.  # noqa: E501

        :return: The coordinates of this MavenLibrary.
        :rtype: str
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """Sets the coordinates of this MavenLibrary.

        Gradle-style Maven coordinates. For example: `org.jsoup:jsoup:1.7.2`. This field is required.  # noqa: E501

        :param coordinates: The coordinates of this MavenLibrary.
        :type coordinates: str
        """
        if coordinates is None:
            raise ValueError("Invalid value for `coordinates`, must not be `None`")  # noqa: E501

        self._coordinates = coordinates

    @property
    def repo(self):
        """Gets the repo of this MavenLibrary.

        Maven repo to install the Maven package from. If omitted, both Maven Central Repository and Spark Packages are searched.  # noqa: E501

        :return: The repo of this MavenLibrary.
        :rtype: str
        """
        return self._repo

    @repo.setter
    def repo(self, repo):
        """Sets the repo of this MavenLibrary.

        Maven repo to install the Maven package from. If omitted, both Maven Central Repository and Spark Packages are searched.  # noqa: E501

        :param repo: The repo of this MavenLibrary.
        :type repo: str
        """

        self._repo = repo

    @property
    def exclusions(self):
        """Gets the exclusions of this MavenLibrary.

        List of dependences to exclude. For example: `[\"slf4j:slf4j\", \"*:hadoop-client\"]`.  Maven dependency exclusions: <https://maven.apache.org/guides/introduction/introduction-to-optional-and-excludes-dependencies.html>.  # noqa: E501

        :return: The exclusions of this MavenLibrary.
        :rtype: List[str]
        """
        return self._exclusions

    @exclusions.setter
    def exclusions(self, exclusions):
        """Sets the exclusions of this MavenLibrary.

        List of dependences to exclude. For example: `[\"slf4j:slf4j\", \"*:hadoop-client\"]`.  Maven dependency exclusions: <https://maven.apache.org/guides/introduction/introduction-to-optional-and-excludes-dependencies.html>.  # noqa: E501

        :param exclusions: The exclusions of this MavenLibrary.
        :type exclusions: List[str]
        """

        self._exclusions = exclusions
