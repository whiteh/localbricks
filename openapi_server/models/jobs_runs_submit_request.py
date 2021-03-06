# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.access_control_list import AccessControlList
from openapi_server.models.access_control_request import AccessControlRequest
from openapi_server.models.git_source import GitSource
from openapi_server.models.run_submit_settings import RunSubmitSettings
from openapi_server.models.run_submit_task_settings import RunSubmitTaskSettings


class JobsRunsSubmitRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    JobsRunsSubmitRequest - a model defined in OpenAPI

        tasks: The tasks of this JobsRunsSubmitRequest [Optional].
        run_name: The run_name of this JobsRunsSubmitRequest [Optional].
        git_source: The git_source of this JobsRunsSubmitRequest [Optional].
        timeout_seconds: The timeout_seconds of this JobsRunsSubmitRequest [Optional].
        idempotency_token: The idempotency_token of this JobsRunsSubmitRequest [Optional].
        access_control_list: The access_control_list of this JobsRunsSubmitRequest [Optional].
    """

    tasks: Optional[List[RunSubmitTaskSettings]] = Field(alias="tasks", default=None)
    run_name: Optional[str] = Field(alias="run_name", default=None)
    git_source: Optional[GitSource] = Field(alias="git_source", default=None)
    timeout_seconds: Optional[int] = Field(alias="timeout_seconds", default=None)
    idempotency_token: Optional[str] = Field(alias="idempotency_token", default=None)
    access_control_list: Optional[List[AccessControlRequest]] = Field(
        alias="access_control_list", default=None)


JobsRunsSubmitRequest.update_forward_refs()
