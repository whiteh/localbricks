# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.notebook_output import NotebookOutput
from openapi_server.models.run import Run


class JobsRunsGetOutput200Response(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    JobsRunsGetOutput200Response - a model defined in OpenAPI

        notebook_output: The notebook_output of this JobsRunsGetOutput200Response [Optional].
        logs: The logs of this JobsRunsGetOutput200Response [Optional].
        logs_truncated: The logs_truncated of this JobsRunsGetOutput200Response [Optional].
        error: The error of this JobsRunsGetOutput200Response [Optional].
        error_trace: The error_trace of this JobsRunsGetOutput200Response [Optional].
        metadata: The metadata of this JobsRunsGetOutput200Response [Optional].
    """

    notebook_output: Optional[NotebookOutput] = Field(
        alias="notebook_output", default=None)
    logs: Optional[str] = Field(alias="logs", default=None)
    logs_truncated: Optional[bool] = Field(alias="logs_truncated", default=None)
    error: Optional[str] = Field(alias="error", default=None)
    error_trace: Optional[str] = Field(alias="error_trace", default=None)
    metadata: Optional[Run] = Field(alias="metadata", default=None)


JobsRunsGetOutput200Response.update_forward_refs()
