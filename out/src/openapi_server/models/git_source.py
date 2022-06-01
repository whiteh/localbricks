# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.git_snapshot import GitSnapshot


class GitSource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    GitSource - a model defined in OpenAPI

        git_url: The git_url of this GitSource [Optional].
        git_provider: The git_provider of this GitSource [Optional].
        git_branch: The git_branch of this GitSource [Optional].
        git_tag: The git_tag of this GitSource [Optional].
        git_commit: The git_commit of this GitSource [Optional].
        git_snapshot: The git_snapshot of this GitSource [Optional].
    """

    git_url: Optional[str] = Field(alias="git_url", default=None)
    git_provider: Optional[str] = Field(alias="git_provider", default=None)
    git_branch: Optional[str] = Field(alias="git_branch", default=None)
    git_tag: Optional[str] = Field(alias="git_tag", default=None)
    git_commit: Optional[str] = Field(alias="git_commit", default=None)
    git_snapshot: Optional[GitSnapshot] = Field(alias="git_snapshot", default=None)

GitSource.update_forward_refs()
