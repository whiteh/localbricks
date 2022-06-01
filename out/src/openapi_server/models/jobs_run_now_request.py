# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.run_now_input import RunNowInput
from openapi_server.models.run_parameters import RunParameters


class JobsRunNowRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    JobsRunNowRequest - a model defined in OpenAPI

        job_id: The job_id of this JobsRunNowRequest [Optional].
        idempotency_token: The idempotency_token of this JobsRunNowRequest [Optional].
        jar_params: The jar_params of this JobsRunNowRequest [Optional].
        notebook_params: The notebook_params of this JobsRunNowRequest [Optional].
        python_params: The python_params of this JobsRunNowRequest [Optional].
        spark_submit_params: The spark_submit_params of this JobsRunNowRequest [Optional].
        python_named_params: The python_named_params of this JobsRunNowRequest [Optional].
    """

    job_id: Optional[int] = Field(alias="job_id", default=None)
    idempotency_token: Optional[str] = Field(alias="idempotency_token", default=None)
    jar_params: Optional[List[str]] = Field(alias="jar_params", default=None)
    notebook_params: Optional[Dict[str, Any]] = Field(alias="notebook_params", default=None)
    python_params: Optional[List[str]] = Field(alias="python_params", default=None)
    spark_submit_params: Optional[List[str]] = Field(alias="spark_submit_params", default=None)
    python_named_params: Optional[Dict[str, Any]] = Field(alias="python_named_params", default=None)

JobsRunNowRequest.update_forward_refs()
