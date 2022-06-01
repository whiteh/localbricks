# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class JobEmailNotifications(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    JobEmailNotifications - a model defined in OpenAPI

        on_start: The on_start of this JobEmailNotifications [Optional].
        on_success: The on_success of this JobEmailNotifications [Optional].
        on_failure: The on_failure of this JobEmailNotifications [Optional].
        no_alert_for_skipped_runs: The no_alert_for_skipped_runs of this JobEmailNotifications [Optional].
    """

    on_start: Optional[List[str]] = Field(alias="on_start", default=None)
    on_success: Optional[List[str]] = Field(alias="on_success", default=None)
    on_failure: Optional[List[str]] = Field(alias="on_failure", default=None)
    no_alert_for_skipped_runs: Optional[bool] = Field(alias="no_alert_for_skipped_runs", default=None)

JobEmailNotifications.update_forward_refs()
