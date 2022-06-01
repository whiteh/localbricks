# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class Error(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Error - a model defined in OpenAPI

        error_code: The error_code of this Error [Optional].
        message: The message of this Error [Optional].
    """

    error_code: Optional[str] = Field(alias="error_code", default=None)
    message: Optional[str] = Field(alias="message", default=None)

Error.update_forward_refs()