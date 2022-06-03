# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.job_settings import JobSettings


class Job(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Job - a model defined in OpenAPI

        job_id: The job_id of this Job [Optional].
        creator_user_name: The creator_user_name of this Job [Optional].
        run_as_user_name: The run_as_user_name of this Job [Optional].
        settings: The settings of this Job [Optional].
        created_time: The created_time of this Job [Optional].
    """

    job_id: Optional[int] = Field(alias="job_id", default=None)
    creator_user_name: Optional[str] = Field(alias="creator_user_name", default=None)
    run_as_user_name: Optional[str] = Field(alias="run_as_user_name", default=None)
    settings: Optional[JobSettings] = Field(alias="settings", default=None)
    created_time: Optional[int] = Field(alias="created_time", default=None)


Job.update_forward_refs()
