# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.spark_node_aws_attributes import SparkNodeAwsAttributes


class SparkNode(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SparkNode - a model defined in OpenAPI

        private_ip: The private_ip of this SparkNode [Optional].
        public_dns: The public_dns of this SparkNode [Optional].
        node_id: The node_id of this SparkNode [Optional].
        instance_id: The instance_id of this SparkNode [Optional].
        start_timestamp: The start_timestamp of this SparkNode [Optional].
        node_aws_attributes: The node_aws_attributes of this SparkNode [Optional].
        host_private_ip: The host_private_ip of this SparkNode [Optional].
    """

    private_ip: Optional[str] = Field(alias="private_ip", default=None)
    public_dns: Optional[str] = Field(alias="public_dns", default=None)
    node_id: Optional[str] = Field(alias="node_id", default=None)
    instance_id: Optional[str] = Field(alias="instance_id", default=None)
    start_timestamp: Optional[int] = Field(alias="start_timestamp", default=None)
    node_aws_attributes: Optional[SparkNodeAwsAttributes] = Field(alias="node_aws_attributes", default=None)
    host_private_ip: Optional[str] = Field(alias="host_private_ip", default=None)

SparkNode.update_forward_refs()