# coding: utf-8

from typing import Dict, List  # noqa: F401

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from openapi_server.models.error import Error
from openapi_server.models.jobs_create200_response import JobsCreate200Response
from openapi_server.models.jobs_create_request import JobsCreateRequest
from openapi_server.models.jobs_delete_request import JobsDeleteRequest
from openapi_server.models.jobs_get200_response import JobsGet200Response
from openapi_server.models.jobs_list200_response import JobsList200Response
from openapi_server.models.jobs_reset_request import JobsResetRequest
from openapi_server.models.jobs_run_now200_response import JobsRunNow200Response
from openapi_server.models.jobs_run_now_request import JobsRunNowRequest
from openapi_server.models.jobs_runs_cancel_request import JobsRunsCancelRequest
from openapi_server.models.jobs_runs_delete_request import JobsRunsDeleteRequest
from openapi_server.models.jobs_runs_export200_response import JobsRunsExport200Response
from openapi_server.models.jobs_runs_get200_response import JobsRunsGet200Response
from openapi_server.models.jobs_runs_get_output200_response import JobsRunsGetOutput200Response
from openapi_server.models.jobs_runs_list200_response import JobsRunsList200Response
from openapi_server.models.jobs_runs_repair200_response import JobsRunsRepair200Response
from openapi_server.models.jobs_runs_repair_request import JobsRunsRepairRequest
from openapi_server.models.jobs_runs_submit200_response import JobsRunsSubmit200Response
from openapi_server.models.jobs_runs_submit_request import JobsRunsSubmitRequest
from openapi_server.models.jobs_update_request import JobsUpdateRequest
from openapi_server.models.views_to_export import ViewsToExport
from openapi_server.security_api import get_token_bearerAuth

router = APIRouter()


@router.post(
    "/2.1/jobs/create",
    responses={
        200: {"model": JobsCreate200Response, "description": "Job was created successfully"},
        400: {"model": Error, "description": "The request was malformed. See JSON response for error details."},
        401: {"model": Error, "description": "The request was unauthorized."},
        500: {"model": Error, "description": "The request was not handled correctly due to a server error."},
    },
    tags=["default"],
    summary="Create a new job",
    response_model_by_alias=True,
)
async def jobs_create(
    jobs_create_request: JobsCreateRequest = Body(None, description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> JobsCreate200Response:
    """Create a new job."""
    ...


@router.post(
    "/2.1/jobs/delete",
    responses={
        200: {"model": Dict, "description": "Job was deleted successfully."},
        400: {"model": Error, "description": "The request was malformed. See JSON response for error details."},
        401: {"model": Error, "description": "The request was unauthorized."},
        500: {"model": Error, "description": "The request was not handled correctly due to a server error."},
    },
    tags=["default"],
    summary="Delete a job",
    response_model_by_alias=True,
)
async def jobs_delete(
    jobs_delete_request: JobsDeleteRequest = Body(None, description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> object:
    """Deletes a job."""
    ...


@router.get(
    "/2.1/jobs/get",
    responses={
        200: {"model": JobsGet200Response, "description": "Job was retrieved successfully."},
        400: {"model": Error, "description": "The request was malformed. See JSON response for error details."},
        401: {"model": Error, "description": "The request was unauthorized."},
        500: {"model": Error, "description": "The request was not handled correctly due to a server error."},
    },
    tags=["default"],
    summary="Get a single job",
    response_model_by_alias=True,
)
async def jobs_get(
    job_id: int = Query(
        None, description="The canonical identifier of the job to retrieve information about. This field is required."),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> JobsGet200Response:
    """Retrieves the details for a single job."""
    ...


@router.get(
    "/2.1/jobs/list",
    responses={
        200: {"model": JobsList200Response, "description": "List of jobs was retrieved successfully."},
        400: {"model": Error, "description": "The request was malformed. See JSON response for error details."},
        401: {"model": Error, "description": "The request was unauthorized."},
        500: {"model": Error, "description": "The request was not handled correctly due to a server error."},
    },
    tags=["default"],
    summary="List all jobs",
    response_model_by_alias=True,
)
async def jobs_list(
    limit: int = Query(
        20, description="The number of jobs to return. This value must be greater than 0 and less or equal to 25. The default value is 20.", ge=1, le=25),
    offset: int = Query(
        0, description="The offset of the first job to return, relative to the most recently created job.", ge=0),
    expand_tasks: bool = Query(
        False, description="Whether to include task and cluster details in the response."),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> JobsList200Response:
    """Retrieves a list of jobs."""
    ...


@router.post(
    "/2.1/jobs/reset",
    responses={
        200: {"model": Dict, "description": "Job was overwritten successfully."},
        400: {"model": Error, "description": "The request was malformed. See JSON response for error details."},
        401: {"model": Error, "description": "The request was unauthorized."},
        500: {"model": Error, "description": "The request was not handled correctly due to a server error."},
    },
    tags=["default"],
    summary="Overwrites all settings for a job",
    response_model_by_alias=True,
)
async def jobs_reset(
    jobs_reset_request: JobsResetRequest = Body(None, description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> object:
    """Overwrites all the settings for a specific job. Use the Update endpoint to update job settings partially."""
    ...


@router.post(
    "/2.1/jobs/run-now",
    responses={
        200: {"model": JobsRunNow200Response, "description": "Run was started successfully."},
        400: {"model": Error, "description": "The request was malformed. See JSON response for error details."},
        401: {"model": Error, "description": "The request was unauthorized."},
        500: {"model": Error, "description": "The request was not handled correctly due to a server error."},
    },
    tags=["default"],
    summary="Trigger a new job run",
    response_model_by_alias=True,
)
async def jobs_run_now(
    jobs_run_now_request: JobsRunNowRequest = Body(None, description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> JobsRunNow200Response:
    """Run a job and return the &#x60;run_id&#x60; of the triggered run."""
    ...


@router.post(
    "/2.1/jobs/runs/cancel",
    responses={
        200: {"model": Dict, "description": "Run was cancelled successfully."},
        400: {"model": Error, "description": "The request was malformed. See JSON response for error details."},
        401: {"model": Error, "description": "The request was unauthorized."},
        500: {"model": Error, "description": "The request was not handled correctly due to a server error."},
    },
    tags=["default"],
    summary="Cancel a job run",
    response_model_by_alias=True,
)
async def jobs_runs_cancel(
    jobs_runs_cancel_request: JobsRunsCancelRequest = Body(None, description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> object:
    """Cancels a run. The run is canceled asynchronously, so when this request completes, the run may still be running. The run are terminated shortly. If the run is already in a terminal &#x60;life_cycle_state&#x60;, this method is a no-op."""
    ...


@router.post(
    "/2.1/jobs/runs/delete",
    responses={
        200: {"model": Dict, "description": "Run was deleted successfully."},
        400: {"model": Error, "description": "The request was malformed. See JSON response for error details."},
        401: {"model": Error, "description": "The request was unauthorized."},
        500: {"model": Error, "description": "The request was not handled correctly due to a server error."},
    },
    tags=["default"],
    summary="Delete a job run",
    response_model_by_alias=True,
)
async def jobs_runs_delete(
    jobs_runs_delete_request: JobsRunsDeleteRequest = Body(None, description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> object:
    """Deletes a non-active run. Returns an error if the run is active."""
    ...


@router.get(
    "/2.0/jobs/runs/export",
    responses={
        200: {"model": JobsRunsExport200Response, "description": "Run was exported successfully."},
        400: {"model": Error, "description": "The request was malformed. See JSON response for error details."},
        401: {"model": Error, "description": "The request was unauthorized."},
        500: {"model": Error, "description": "The request was not handled correctly due to a server error."},
    },
    tags=["default"],
    summary="Export and retrieve a job run",
    response_model_by_alias=True,
)
async def jobs_runs_export(
    run_id: int = Query(
        None, description="The canonical identifier for the run. This field is required."),
    views_to_export: int = Query(
        None, description="Which views to export (CODE, DASHBOARDS, or ALL). Defaults to CODE."),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> JobsRunsExport200Response:
    """Export and retrieve the job run task."""
    ...


@router.get(
    "/2.1/jobs/runs/get",
    responses={
        200: {"model": JobsRunsGet200Response, "description": "Run was retrieved successfully"},
        400: {"model": Error, "description": "The request was malformed. See JSON response for error details."},
        401: {"model": Error, "description": "The request was unauthorized."},
        500: {"model": Error, "description": "The request was not handled correctly due to a server error."},
    },
    tags=["default"],
    summary="Get a single job run",
    response_model_by_alias=True,
)
async def jobs_runs_get(
    run_id: int = Query(
        None, description="The canonical identifier of the run for which to retrieve the metadata. This field is required."),
    include_history: bool = Query(
        None, description="Whether to include the repair history in the response."),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> JobsRunsGet200Response:
    """Retrieve the metadata of a run."""
    ...


@router.get(
    "/2.1/jobs/runs/get-output",
    responses={
        200: {"model": JobsRunsGetOutput200Response, "description": "Run output was retrieved successfully."},
        400: {"model": Error, "description": "The request was malformed. See JSON response for error details."},
        401: {"model": Error, "description": "The request was unauthorized."},
        500: {"model": Error, "description": "The request was not handled correctly due to a server error."},
    },
    tags=["default"],
    summary="Get the output for a single run",
    response_model_by_alias=True,
)
async def jobs_runs_get_output(
    run_id: int = Query(
        None, description="The canonical identifier for the run. This field is required."),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> JobsRunsGetOutput200Response:
    """Retrieve the output and metadata of a run. When a notebook task returns a value through the dbutils.notebook.exit() call, you can use this endpoint to retrieve that value. Databricks restricts this API to return the first 5 MB of the output. To return a larger result, you can store job results in a cloud storage service. This endpoint validates that the run_id parameter is valid and returns an HTTP status code 400 if the run_id parameter is invalid. Runs are automatically removed after 60 days. If you to want to reference them beyond 60 days, you must save old run results before they expire. To export using the UI, see Export job run results. To export using the Jobs API, see Runs export."""
    ...


@router.get(
    "/2.1/jobs/runs/list",
    responses={
        200: {"model": JobsRunsList200Response, "description": "List of runs was retrieved successfully."},
        400: {"model": Error, "description": "The request was malformed. See JSON response for error details."},
        401: {"model": Error, "description": "The request was unauthorized."},
        500: {"model": Error, "description": "The request was not handled correctly due to a server error."},
    },
    tags=["default"],
    summary="List runs for a job",
    response_model_by_alias=True,
)
async def jobs_runs_list(
    active_only: bool = Query(False, description="If active_only is &#x60;true&#x60;, only active runs are included in the results; otherwise, lists both active and completed runs. An active run is a run in the &#x60;PENDING&#x60;, &#x60;RUNNING&#x60;, or &#x60;TERMINATING&#x60;. This field cannot be &#x60;true&#x60; when completed_only is &#x60;true&#x60;."),
    completed_only: bool = Query(
        False, description="If completed_only is &#x60;true&#x60;, only completed runs are included in the results; otherwise, lists both active and completed runs. This field cannot be &#x60;true&#x60; when active_only is &#x60;true&#x60;."),
    job_id: int = Query(
        None, description="The job for which to list runs. If omitted, the Jobs service lists runs from all jobs."),
    offset: int = Query(
        0, description="The offset of the first run to return, relative to the most recent run."),
    limit: int = Query(25, description="The number of runs to return. This value must be greater than 0 and less than 25\\. The default value is 25\\. If a request specifies a limit of 0, the service instead uses the maximum limit.", ge=1, le=25),
    run_type: str = Query(
        None, description="The type of runs to return. For a description of run types, see [Run](https://docs.databricks.com/dev-tools/api/latest/jobs.html#operation/JobsRunsGet)."),
    expand_tasks: bool = Query(
        False, description="Whether to include task and cluster details in the response."),
    start_time_from: int = Query(
        None, description="Show runs that started _at or after_ this value. The value must be a UTC timestamp in milliseconds. Can be combined with _start_time_to_ to filter by a time range."),
    start_time_to: int = Query(
        None, description="Show runs that started _at or before_ this value. The value must be a UTC timestamp in milliseconds. Can be combined with _start_time_from_ to filter by a time range."),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> JobsRunsList200Response:
    """List runs in descending order by start time."""
    ...


@router.post(
    "/2.1/jobs/runs/repair",
    responses={
        200: {"model": JobsRunsRepair200Response, "description": "Run repair was initiated."},
        400: {"model": Error, "description": "The request was malformed. See JSON response for error details."},
        401: {"model": Error, "description": "The request was unauthorized."},
        500: {"model": Error, "description": "The request was not handled correctly due to a server error."},
    },
    tags=["default"],
    summary="Repair a job run",
    response_model_by_alias=True,
)
async def jobs_runs_repair(
    jobs_runs_repair_request: JobsRunsRepairRequest = Body(None, description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> JobsRunsRepair200Response:
    """Re-run one or more tasks. Tasks are re-run as part of the original job run, use the current job and task settings, and can be viewed in the history for the original job run."""
    ...


@router.post(
    "/2.1/jobs/runs/submit",
    responses={
        200: {"model": JobsRunsSubmit200Response, "description": "Run was created and started successfully."},
        400: {"model": Error, "description": "The request was malformed. See JSON response for error details."},
        401: {"model": Error, "description": "The request was unauthorized."},
        500: {"model": Error, "description": "The request was not handled correctly due to a server error."},
    },
    tags=["default"],
    summary="Create and trigger a one-time run",
    response_model_by_alias=True,
)
async def jobs_runs_submit(
    jobs_runs_submit_request: JobsRunsSubmitRequest = Body(None, description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> JobsRunsSubmit200Response:
    """Submit a one-time run. This endpoint allows you to submit a workload directly without creating a job. Runs submitted using this endpoint don’t display in the UI. Use the &#x60;jobs/runs/get&#x60; API to check the run state after the job is submitted."""
    ...


@router.post(
    "/2.1/jobs/update",
    responses={
        200: {"model": Dict, "description": "Job was updated successfully."},
        400: {"model": Error, "description": "The request was malformed. See JSON response for error details."},
        401: {"model": Error, "description": "The request was unauthorized."},
        500: {"model": Error, "description": "The request was not handled correctly due to a server error."},
    },
    tags=["default"],
    summary="Partially updates a job",
    response_model_by_alias=True,
)
async def jobs_update(
    jobs_update_request: JobsUpdateRequest = Body(None, description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> object:
    """Add, update, or remove specific settings of an existing job. Use the Reset endpoint to overwrite all job settings."""
    ...
