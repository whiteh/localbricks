# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.dbfs_storage_info import DbfsStorageInfo
from openapi_server.models.s3_storage_info import S3StorageInfo


class ClusterLogConf(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ClusterLogConf - a model defined in OpenAPI

        dbfs: The dbfs of this ClusterLogConf [Optional].
        s3: The s3 of this ClusterLogConf [Optional].
    """

    dbfs: Optional[DbfsStorageInfo] = Field(alias="dbfs", default=None)
    s3: Optional[S3StorageInfo] = Field(alias="s3", default=None)

ClusterLogConf.update_forward_refs()
