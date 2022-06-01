# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.library_full_status import LibraryFullStatus


class ClusterLibraryStatuses(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ClusterLibraryStatuses - a model defined in OpenAPI

        cluster_id: The cluster_id of this ClusterLibraryStatuses [Optional].
        library_statuses: The library_statuses of this ClusterLibraryStatuses [Optional].
    """

    cluster_id: Optional[str] = Field(alias="cluster_id", default=None)
    library_statuses: Optional[List[LibraryFullStatus]] = Field(alias="library_statuses", default=None)

ClusterLibraryStatuses.update_forward_refs()
