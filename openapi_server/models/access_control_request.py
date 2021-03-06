# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.access_control_request_for_group import AccessControlRequestForGroup
from openapi_server.models.access_control_request_for_user import AccessControlRequestForUser
from openapi_server.models.permission_level_for_group import PermissionLevelForGroup


class AccessControlRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    AccessControlRequest - a model defined in OpenAPI

        user_name: The user_name of this AccessControlRequest [Optional].
        permission_level: The permission_level of this AccessControlRequest [Optional].
        group_name: The group_name of this AccessControlRequest [Optional].
    """

    user_name: Optional[str] = Field(alias="user_name", default=None)
    permission_level: Optional[PermissionLevelForGroup] = Field(
        alias="permission_level", default=None)
    group_name: Optional[str] = Field(alias="group_name", default=None)


AccessControlRequest.update_forward_refs()
