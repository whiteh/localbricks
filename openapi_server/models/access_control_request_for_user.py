# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.permission_level import PermissionLevel


class AccessControlRequestForUser(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    AccessControlRequestForUser - a model defined in OpenAPI

        user_name: The user_name of this AccessControlRequestForUser [Optional].
        permission_level: The permission_level of this AccessControlRequestForUser [Optional].
    """

    user_name: Optional[str] = Field(alias="user_name", default=None)
    permission_level: Optional[PermissionLevel] = Field(
        alias="permission_level", default=None)


AccessControlRequestForUser.update_forward_refs()
