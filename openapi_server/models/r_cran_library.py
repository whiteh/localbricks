# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class RCranLibrary(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    RCranLibrary - a model defined in OpenAPI

        package: The package of this RCranLibrary.
        repo: The repo of this RCranLibrary [Optional].
    """

    package: str = Field(alias="package")
    repo: Optional[str] = Field(alias="repo", default=None)


RCranLibrary.update_forward_refs()
