# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.can_manage import CanManage
from openapi_server.models.can_manage_run import CanManageRun
from openapi_server.models.can_view import CanView
from openapi_server.models.is_owner import IsOwner


class PermissionLevel(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    PermissionLevel - a model defined in OpenAPI

    """


PermissionLevel.update_forward_refs()
