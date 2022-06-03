# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class S3StorageInfo(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    S3StorageInfo - a model defined in OpenAPI

        destination: The destination of this S3StorageInfo [Optional].
        region: The region of this S3StorageInfo [Optional].
        endpoint: The endpoint of this S3StorageInfo [Optional].
        enable_encryption: The enable_encryption of this S3StorageInfo [Optional].
        encryption_type: The encryption_type of this S3StorageInfo [Optional].
        kms_key: The kms_key of this S3StorageInfo [Optional].
        canned_acl: The canned_acl of this S3StorageInfo [Optional].
    """

    destination: Optional[str] = Field(alias="destination", default=None)
    region: Optional[str] = Field(alias="region", default=None)
    endpoint: Optional[str] = Field(alias="endpoint", default=None)
    enable_encryption: Optional[bool] = Field(alias="enable_encryption", default=None)
    encryption_type: Optional[str] = Field(alias="encryption_type", default=None)
    kms_key: Optional[str] = Field(alias="kms_key", default=None)
    canned_acl: Optional[str] = Field(alias="canned_acl", default=None)


S3StorageInfo.update_forward_refs()
