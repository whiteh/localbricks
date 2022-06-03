# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class SparkSubmitTask(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SparkSubmitTask - a model defined in OpenAPI

        parameters: The parameters of this SparkSubmitTask [Optional].
    """

    parameters: Optional[List[str]] = Field(alias="parameters", default=None)

SparkSubmitTask.update_forward_refs()