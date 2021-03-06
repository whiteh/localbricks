# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.repair_history_item import RepairHistoryItem


class RepairHistory(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    RepairHistory - a model defined in OpenAPI

        repair_history: The repair_history of this RepairHistory [Optional].
    """

    repair_history: Optional[List[RepairHistoryItem]] = Field(
        alias="repair_history", default=None)


RepairHistory.update_forward_refs()
