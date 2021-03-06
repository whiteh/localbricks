# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class JobsDeleteRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    JobsDeleteRequest - a model defined in OpenAPI

        job_id: The job_id of this JobsDeleteRequest.
    """

    job_id: int = Field(alias="job_id")


JobsDeleteRequest.update_forward_refs()
