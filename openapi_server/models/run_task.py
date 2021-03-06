# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.cluster_instance import ClusterInstance
from openapi_server.models.git_source import GitSource
from openapi_server.models.library import Library
from openapi_server.models.new_cluster import NewCluster
from openapi_server.models.notebook_task import NotebookTask
from openapi_server.models.pipeline_task import PipelineTask
from openapi_server.models.python_wheel_task import PythonWheelTask
from openapi_server.models.run_state import RunState
from openapi_server.models.spark_jar_task import SparkJarTask
from openapi_server.models.spark_python_task import SparkPythonTask
from openapi_server.models.spark_submit_task import SparkSubmitTask
from openapi_server.models.task_dependencies_inner import TaskDependenciesInner


class RunTask(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    RunTask - a model defined in OpenAPI

        run_id: The run_id of this RunTask [Optional].
        task_key: The task_key of this RunTask [Optional].
        description: The description of this RunTask [Optional].
        state: The state of this RunTask [Optional].
        depends_on: The depends_on of this RunTask [Optional].
        existing_cluster_id: The existing_cluster_id of this RunTask [Optional].
        new_cluster: The new_cluster of this RunTask [Optional].
        libraries: The libraries of this RunTask [Optional].
        notebook_task: The notebook_task of this RunTask [Optional].
        spark_jar_task: The spark_jar_task of this RunTask [Optional].
        spark_python_task: The spark_python_task of this RunTask [Optional].
        spark_submit_task: The spark_submit_task of this RunTask [Optional].
        pipeline_task: The pipeline_task of this RunTask [Optional].
        python_wheel_task: The python_wheel_task of this RunTask [Optional].
        start_time: The start_time of this RunTask [Optional].
        setup_duration: The setup_duration of this RunTask [Optional].
        execution_duration: The execution_duration of this RunTask [Optional].
        cleanup_duration: The cleanup_duration of this RunTask [Optional].
        end_time: The end_time of this RunTask [Optional].
        attempt_number: The attempt_number of this RunTask [Optional].
        cluster_instance: The cluster_instance of this RunTask [Optional].
        git_source: The git_source of this RunTask [Optional].
    """

    run_id: Optional[int] = Field(alias="run_id", default=None)
    task_key: Optional[str] = Field(alias="task_key", default=None)
    description: Optional[str] = Field(alias="description", default=None)
    state: Optional[RunState] = Field(alias="state", default=None)
    depends_on: Optional[List[TaskDependenciesInner]
                         ] = Field(alias="depends_on", default=None)
    existing_cluster_id: Optional[str] = Field(
        alias="existing_cluster_id", default=None)
    new_cluster: Optional[NewCluster] = Field(alias="new_cluster", default=None)
    libraries: Optional[List[Library]] = Field(alias="libraries", default=None)
    notebook_task: Optional[NotebookTask] = Field(alias="notebook_task", default=None)
    spark_jar_task: Optional[SparkJarTask] = Field(alias="spark_jar_task", default=None)
    spark_python_task: Optional[SparkPythonTask] = Field(
        alias="spark_python_task", default=None)
    spark_submit_task: Optional[SparkSubmitTask] = Field(
        alias="spark_submit_task", default=None)
    pipeline_task: Optional[PipelineTask] = Field(alias="pipeline_task", default=None)
    python_wheel_task: Optional[PythonWheelTask] = Field(
        alias="python_wheel_task", default=None)
    start_time: Optional[int] = Field(alias="start_time", default=None)
    setup_duration: Optional[int] = Field(alias="setup_duration", default=None)
    execution_duration: Optional[int] = Field(alias="execution_duration", default=None)
    cleanup_duration: Optional[int] = Field(alias="cleanup_duration", default=None)
    end_time: Optional[int] = Field(alias="end_time", default=None)
    attempt_number: Optional[int] = Field(alias="attempt_number", default=None)
    cluster_instance: Optional[ClusterInstance] = Field(
        alias="cluster_instance", default=None)
    git_source: Optional[GitSource] = Field(alias="git_source", default=None)

    @validator("task_key")
    def task_key_min_length(cls, value):
        assert len(value) >= 1
        return value

    @validator("task_key")
    def task_key_max_length(cls, value):
        assert len(value) <= 100
        return value

    @validator("task_key")
    def task_key_pattern(cls, value):
        assert value is not None and re.match(r"^[\w\-]+$", value)
        return value

    @validator("description")
    def description_max_length(cls, value):
        assert len(value) <= 4096
        return value


RunTask.update_forward_refs()
