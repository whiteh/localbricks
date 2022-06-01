# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class SparkJarTask(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, main_class_name=None, parameters=None, jar_uri=None):  # noqa: E501
        """SparkJarTask - a model defined in OpenAPI

        :param main_class_name: The main_class_name of this SparkJarTask.  # noqa: E501
        :type main_class_name: str
        :param parameters: The parameters of this SparkJarTask.  # noqa: E501
        :type parameters: List[str]
        :param jar_uri: The jar_uri of this SparkJarTask.  # noqa: E501
        :type jar_uri: str
        """
        self.openapi_types = {
            'main_class_name': str,
            'parameters': List[str],
            'jar_uri': str
        }

        self.attribute_map = {
            'main_class_name': 'main_class_name',
            'parameters': 'parameters',
            'jar_uri': 'jar_uri'
        }

        self._main_class_name = main_class_name
        self._parameters = parameters
        self._jar_uri = jar_uri

    @classmethod
    def from_dict(cls, dikt) -> 'SparkJarTask':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SparkJarTask of this SparkJarTask.  # noqa: E501
        :rtype: SparkJarTask
        """
        return util.deserialize_model(dikt, cls)

    @property
    def main_class_name(self):
        """Gets the main_class_name of this SparkJarTask.

        The full name of the class containing the main method to be executed. This class must be contained in a JAR provided as a library.  The code must use `SparkContext.getOrCreate` to obtain a Spark context; otherwise, runs of the job fail.  # noqa: E501

        :return: The main_class_name of this SparkJarTask.
        :rtype: str
        """
        return self._main_class_name

    @main_class_name.setter
    def main_class_name(self, main_class_name):
        """Sets the main_class_name of this SparkJarTask.

        The full name of the class containing the main method to be executed. This class must be contained in a JAR provided as a library.  The code must use `SparkContext.getOrCreate` to obtain a Spark context; otherwise, runs of the job fail.  # noqa: E501

        :param main_class_name: The main_class_name of this SparkJarTask.
        :type main_class_name: str
        """

        self._main_class_name = main_class_name

    @property
    def parameters(self):
        """Gets the parameters of this SparkJarTask.

        Parameters passed to the main method.  Use [Task parameter variables](https://docs.databricks.com/jobs.html#parameter-variables) to set parameters containing information about job runs.  # noqa: E501

        :return: The parameters of this SparkJarTask.
        :rtype: List[str]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this SparkJarTask.

        Parameters passed to the main method.  Use [Task parameter variables](https://docs.databricks.com/jobs.html#parameter-variables) to set parameters containing information about job runs.  # noqa: E501

        :param parameters: The parameters of this SparkJarTask.
        :type parameters: List[str]
        """

        self._parameters = parameters

    @property
    def jar_uri(self):
        """Gets the jar_uri of this SparkJarTask.

        Deprecated since 04/2016\\. Provide a `jar` through the `libraries` field instead. For an example, see [Create](https://docs.databricks.com/dev-tools/api/latest/jobs.html#operation/JobsCreate).  # noqa: E501

        :return: The jar_uri of this SparkJarTask.
        :rtype: str
        """
        return self._jar_uri

    @jar_uri.setter
    def jar_uri(self, jar_uri):
        """Sets the jar_uri of this SparkJarTask.

        Deprecated since 04/2016\\. Provide a `jar` through the `libraries` field instead. For an example, see [Create](https://docs.databricks.com/dev-tools/api/latest/jobs.html#operation/JobsCreate).  # noqa: E501

        :param jar_uri: The jar_uri of this SparkJarTask.
        :type jar_uri: str
        """

        self._jar_uri = jar_uri
