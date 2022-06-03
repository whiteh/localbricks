# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.auto_scale import AutoScale
from openapi_server.models.aws_attributes import AwsAttributes
from openapi_server.models.cluster_log_conf import ClusterLogConf
from openapi_server.models.cluster_source import ClusterSource
from openapi_server.models.cluster_state import ClusterState
from openapi_server.models.docker_image import DockerImage
from openapi_server.models.init_script_info import InitScriptInfo
from openapi_server.models.log_sync_status import LogSyncStatus
from openapi_server.models.spark_node import SparkNode
from openapi_server.models.termination_reason import TerminationReason


class ClusterInfo(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ClusterInfo - a model defined in OpenAPI

        num_workers: The num_workers of this ClusterInfo [Optional].
        autoscale: The autoscale of this ClusterInfo [Optional].
        cluster_id: The cluster_id of this ClusterInfo [Optional].
        creator_user_name: The creator_user_name of this ClusterInfo [Optional].
        driver: The driver of this ClusterInfo [Optional].
        executors: The executors of this ClusterInfo [Optional].
        spark_context_id: The spark_context_id of this ClusterInfo [Optional].
        jdbc_port: The jdbc_port of this ClusterInfo [Optional].
        cluster_name: The cluster_name of this ClusterInfo [Optional].
        spark_version: The spark_version of this ClusterInfo [Optional].
        spark_conf: The spark_conf of this ClusterInfo [Optional].
        aws_attributes: The aws_attributes of this ClusterInfo [Optional].
        node_type_id: The node_type_id of this ClusterInfo [Optional].
        driver_node_type_id: The driver_node_type_id of this ClusterInfo [Optional].
        ssh_public_keys: The ssh_public_keys of this ClusterInfo [Optional].
        custom_tags: The custom_tags of this ClusterInfo [Optional].
        cluster_log_conf: The cluster_log_conf of this ClusterInfo [Optional].
        init_scripts: The init_scripts of this ClusterInfo [Optional].
        docker_image: The docker_image of this ClusterInfo [Optional].
        spark_env_vars: The spark_env_vars of this ClusterInfo [Optional].
        autotermination_minutes: The autotermination_minutes of this ClusterInfo [Optional].
        enable_elastic_disk: The enable_elastic_disk of this ClusterInfo [Optional].
        instance_pool_id: The instance_pool_id of this ClusterInfo [Optional].
        cluster_source: The cluster_source of this ClusterInfo [Optional].
        state: The state of this ClusterInfo [Optional].
        state_message: The state_message of this ClusterInfo [Optional].
        start_time: The start_time of this ClusterInfo [Optional].
        terminated_time: The terminated_time of this ClusterInfo [Optional].
        last_state_loss_time: The last_state_loss_time of this ClusterInfo [Optional].
        last_activity_time: The last_activity_time of this ClusterInfo [Optional].
        cluster_memory_mb: The cluster_memory_mb of this ClusterInfo [Optional].
        cluster_cores: The cluster_cores of this ClusterInfo [Optional].
        default_tags: The default_tags of this ClusterInfo [Optional].
        cluster_log_status: The cluster_log_status of this ClusterInfo [Optional].
        termination_reason: The termination_reason of this ClusterInfo [Optional].
    """

    num_workers: Optional[int] = Field(alias="num_workers", default=None)
    autoscale: Optional[AutoScale] = Field(alias="autoscale", default=None)
    cluster_id: Optional[str] = Field(alias="cluster_id", default=None)
    creator_user_name: Optional[str] = Field(alias="creator_user_name", default=None)
    driver: Optional[SparkNode] = Field(alias="driver", default=None)
    executors: Optional[List[SparkNode]] = Field(alias="executors", default=None)
    spark_context_id: Optional[int] = Field(alias="spark_context_id", default=None)
    jdbc_port: Optional[int] = Field(alias="jdbc_port", default=None)
    cluster_name: Optional[str] = Field(alias="cluster_name", default=None)
    spark_version: Optional[str] = Field(alias="spark_version", default=None)
    spark_conf: Optional[Dict[str, Any]] = Field(alias="spark_conf", default=None)
    aws_attributes: Optional[AwsAttributes] = Field(alias="aws_attributes", default=None)
    node_type_id: Optional[str] = Field(alias="node_type_id", default=None)
    driver_node_type_id: Optional[str] = Field(alias="driver_node_type_id", default=None)
    ssh_public_keys: Optional[List[str]] = Field(alias="ssh_public_keys", default=None)
    custom_tags: Optional[List[Dict]] = Field(alias="custom_tags", default=None)
    cluster_log_conf: Optional[ClusterLogConf] = Field(alias="cluster_log_conf", default=None)
    init_scripts: Optional[List[InitScriptInfo]] = Field(alias="init_scripts", default=None)
    docker_image: Optional[DockerImage] = Field(alias="docker_image", default=None)
    spark_env_vars: Optional[Dict[str, Any]] = Field(alias="spark_env_vars", default=None)
    autotermination_minutes: Optional[int] = Field(alias="autotermination_minutes", default=None)
    enable_elastic_disk: Optional[bool] = Field(alias="enable_elastic_disk", default=None)
    instance_pool_id: Optional[str] = Field(alias="instance_pool_id", default=None)
    cluster_source: Optional[ClusterSource] = Field(alias="cluster_source", default=None)
    state: Optional[ClusterState] = Field(alias="state", default=None)
    state_message: Optional[str] = Field(alias="state_message", default=None)
    start_time: Optional[int] = Field(alias="start_time", default=None)
    terminated_time: Optional[int] = Field(alias="terminated_time", default=None)
    last_state_loss_time: Optional[int] = Field(alias="last_state_loss_time", default=None)
    last_activity_time: Optional[int] = Field(alias="last_activity_time", default=None)
    cluster_memory_mb: Optional[int] = Field(alias="cluster_memory_mb", default=None)
    cluster_cores: Optional[float] = Field(alias="cluster_cores", default=None)
    default_tags: Optional[Dict[str, str]] = Field(alias="default_tags", default=None)
    cluster_log_status: Optional[LogSyncStatus] = Field(alias="cluster_log_status", default=None)
    termination_reason: Optional[TerminationReason] = Field(alias="termination_reason", default=None)

ClusterInfo.update_forward_refs()