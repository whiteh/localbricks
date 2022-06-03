# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.run import Run


class JobsRunsList200Response(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    JobsRunsList200Response - a model defined in OpenAPI

        runs: The runs of this JobsRunsList200Response [Optional].
        has_more: The has_more of this JobsRunsList200Response [Optional].
    """

    runs: Optional[List[Run]] = Field(alias="runs", default=None)
    has_more: Optional[bool] = Field(alias="has_more", default=None)


JobsRunsList200Response.update_forward_refs()
