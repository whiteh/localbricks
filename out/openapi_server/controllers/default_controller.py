import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.jobs_create200_response import JobsCreate200Response  # noqa: E501
from openapi_server.models.jobs_create_request import JobsCreateRequest  # noqa: E501
from openapi_server.models.jobs_delete_request import JobsDeleteRequest  # noqa: E501
from openapi_server.models.jobs_get200_response import JobsGet200Response  # noqa: E501
from openapi_server.models.jobs_list200_response import JobsList200Response  # noqa: E501
from openapi_server.models.jobs_reset_request import JobsResetRequest  # noqa: E501
from openapi_server.models.jobs_run_now200_response import JobsRunNow200Response  # noqa: E501
from openapi_server.models.jobs_run_now_request import JobsRunNowRequest  # noqa: E501
from openapi_server.models.jobs_runs_cancel_request import JobsRunsCancelRequest  # noqa: E501
from openapi_server.models.jobs_runs_delete_request import JobsRunsDeleteRequest  # noqa: E501
from openapi_server.models.jobs_runs_export200_response import JobsRunsExport200Response  # noqa: E501
from openapi_server.models.jobs_runs_get200_response import JobsRunsGet200Response  # noqa: E501
from openapi_server.models.jobs_runs_get_output200_response import JobsRunsGetOutput200Response  # noqa: E501
from openapi_server.models.jobs_runs_list200_response import JobsRunsList200Response  # noqa: E501
from openapi_server.models.jobs_runs_repair200_response import JobsRunsRepair200Response  # noqa: E501
from openapi_server.models.jobs_runs_repair_request import JobsRunsRepairRequest  # noqa: E501
from openapi_server.models.jobs_runs_submit200_response import JobsRunsSubmit200Response  # noqa: E501
from openapi_server.models.jobs_runs_submit_request import JobsRunsSubmitRequest  # noqa: E501
from openapi_server.models.jobs_update_request import JobsUpdateRequest  # noqa: E501
from openapi_server.models.views_to_export import ViewsToExport  # noqa: E501
from openapi_server import util


def jobs_create(jobs_create_request):  # noqa: E501
    """Create a new job

    Create a new job. # noqa: E501

    :param jobs_create_request: 
    :type jobs_create_request: dict | bytes

    :rtype: Union[JobsCreate200Response, Tuple[JobsCreate200Response, int], Tuple[JobsCreate200Response, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        jobs_create_request = JobsCreateRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def jobs_delete(jobs_delete_request):  # noqa: E501
    """Delete a job

    Deletes a job. # noqa: E501

    :param jobs_delete_request: 
    :type jobs_delete_request: dict | bytes

    :rtype: Union[object, Tuple[object, int], Tuple[object, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        jobs_delete_request = JobsDeleteRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def jobs_get(job_id):  # noqa: E501
    """Get a single job

    Retrieves the details for a single job. # noqa: E501

    :param job_id: The canonical identifier of the job to retrieve information about. This field is required.
    :type job_id: int

    :rtype: Union[JobsGet200Response, Tuple[JobsGet200Response, int], Tuple[JobsGet200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def jobs_list(limit=None, offset=None, expand_tasks=None):  # noqa: E501
    """List all jobs

    Retrieves a list of jobs. # noqa: E501

    :param limit: The number of jobs to return. This value must be greater than 0 and less or equal to 25. The default value is 20.
    :type limit: int
    :param offset: The offset of the first job to return, relative to the most recently created job.
    :type offset: int
    :param expand_tasks: Whether to include task and cluster details in the response.
    :type expand_tasks: bool

    :rtype: Union[JobsList200Response, Tuple[JobsList200Response, int], Tuple[JobsList200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def jobs_reset(jobs_reset_request):  # noqa: E501
    """Overwrites all settings for a job

    Overwrites all the settings for a specific job. Use the Update endpoint to update job settings partially. # noqa: E501

    :param jobs_reset_request: 
    :type jobs_reset_request: dict | bytes

    :rtype: Union[object, Tuple[object, int], Tuple[object, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        jobs_reset_request = JobsResetRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def jobs_run_now(jobs_run_now_request):  # noqa: E501
    """Trigger a new job run

    Run a job and return the &#x60;run_id&#x60; of the triggered run. # noqa: E501

    :param jobs_run_now_request: 
    :type jobs_run_now_request: dict | bytes

    :rtype: Union[JobsRunNow200Response, Tuple[JobsRunNow200Response, int], Tuple[JobsRunNow200Response, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        jobs_run_now_request = JobsRunNowRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def jobs_runs_cancel(jobs_runs_cancel_request):  # noqa: E501
    """Cancel a job run

    Cancels a run. The run is canceled asynchronously, so when this request completes, the run may still be running. The run are terminated shortly. If the run is already in a terminal &#x60;life_cycle_state&#x60;, this method is a no-op. # noqa: E501

    :param jobs_runs_cancel_request: 
    :type jobs_runs_cancel_request: dict | bytes

    :rtype: Union[object, Tuple[object, int], Tuple[object, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        jobs_runs_cancel_request = JobsRunsCancelRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def jobs_runs_delete(jobs_runs_delete_request):  # noqa: E501
    """Delete a job run

    Deletes a non-active run. Returns an error if the run is active. # noqa: E501

    :param jobs_runs_delete_request: 
    :type jobs_runs_delete_request: dict | bytes

    :rtype: Union[object, Tuple[object, int], Tuple[object, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        jobs_runs_delete_request = JobsRunsDeleteRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def jobs_runs_export(run_id, views_to_export=None):  # noqa: E501
    """Export and retrieve a job run

    Export and retrieve the job run task. # noqa: E501

    :param run_id: The canonical identifier for the run. This field is required.
    :type run_id: int
    :param views_to_export: Which views to export (CODE, DASHBOARDS, or ALL). Defaults to CODE.
    :type views_to_export: dict | bytes

    :rtype: Union[JobsRunsExport200Response, Tuple[JobsRunsExport200Response, int], Tuple[JobsRunsExport200Response, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        views_to_export =  ViewsToExport.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def jobs_runs_get(run_id, include_history=None):  # noqa: E501
    """Get a single job run

    Retrieve the metadata of a run. # noqa: E501

    :param run_id: The canonical identifier of the run for which to retrieve the metadata. This field is required.
    :type run_id: int
    :param include_history: Whether to include the repair history in the response.
    :type include_history: bool

    :rtype: Union[JobsRunsGet200Response, Tuple[JobsRunsGet200Response, int], Tuple[JobsRunsGet200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def jobs_runs_get_output(run_id):  # noqa: E501
    """Get the output for a single run

    Retrieve the output and metadata of a run. When a notebook task returns a value through the dbutils.notebook.exit() call, you can use this endpoint to retrieve that value. Databricks restricts this API to return the first 5 MB of the output. To return a larger result, you can store job results in a cloud storage service. This endpoint validates that the run_id parameter is valid and returns an HTTP status code 400 if the run_id parameter is invalid. Runs are automatically removed after 60 days. If you to want to reference them beyond 60 days, you must save old run results before they expire. To export using the UI, see Export job run results. To export using the Jobs API, see Runs export. # noqa: E501

    :param run_id: The canonical identifier for the run. This field is required.
    :type run_id: int

    :rtype: Union[JobsRunsGetOutput200Response, Tuple[JobsRunsGetOutput200Response, int], Tuple[JobsRunsGetOutput200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def jobs_runs_list(active_only=None, completed_only=None, job_id=None, offset=None, limit=None, run_type=None, expand_tasks=None, start_time_from=None, start_time_to=None):  # noqa: E501
    """List runs for a job

    List runs in descending order by start time. # noqa: E501

    :param active_only: If active_only is &#x60;true&#x60;, only active runs are included in the results; otherwise, lists both active and completed runs. An active run is a run in the &#x60;PENDING&#x60;, &#x60;RUNNING&#x60;, or &#x60;TERMINATING&#x60;. This field cannot be &#x60;true&#x60; when completed_only is &#x60;true&#x60;.
    :type active_only: bool
    :param completed_only: If completed_only is &#x60;true&#x60;, only completed runs are included in the results; otherwise, lists both active and completed runs. This field cannot be &#x60;true&#x60; when active_only is &#x60;true&#x60;.
    :type completed_only: bool
    :param job_id: The job for which to list runs. If omitted, the Jobs service lists runs from all jobs.
    :type job_id: int
    :param offset: The offset of the first run to return, relative to the most recent run.
    :type offset: int
    :param limit: The number of runs to return. This value must be greater than 0 and less than 25\\. The default value is 25\\. If a request specifies a limit of 0, the service instead uses the maximum limit.
    :type limit: int
    :param run_type: The type of runs to return. For a description of run types, see [Run](https://docs.databricks.com/dev-tools/api/latest/jobs.html#operation/JobsRunsGet).
    :type run_type: str
    :param expand_tasks: Whether to include task and cluster details in the response.
    :type expand_tasks: bool
    :param start_time_from: Show runs that started _at or after_ this value. The value must be a UTC timestamp in milliseconds. Can be combined with _start_time_to_ to filter by a time range.
    :type start_time_from: int
    :param start_time_to: Show runs that started _at or before_ this value. The value must be a UTC timestamp in milliseconds. Can be combined with _start_time_from_ to filter by a time range.
    :type start_time_to: int

    :rtype: Union[JobsRunsList200Response, Tuple[JobsRunsList200Response, int], Tuple[JobsRunsList200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def jobs_runs_repair(jobs_runs_repair_request):  # noqa: E501
    """Repair a job run

    Re-run one or more tasks. Tasks are re-run as part of the original job run, use the current job and task settings, and can be viewed in the history for the original job run. # noqa: E501

    :param jobs_runs_repair_request: 
    :type jobs_runs_repair_request: dict | bytes

    :rtype: Union[JobsRunsRepair200Response, Tuple[JobsRunsRepair200Response, int], Tuple[JobsRunsRepair200Response, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        jobs_runs_repair_request = JobsRunsRepairRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def jobs_runs_submit(jobs_runs_submit_request):  # noqa: E501
    """Create and trigger a one-time run

    Submit a one-time run. This endpoint allows you to submit a workload directly without creating a job. Runs submitted using this endpoint don’t display in the UI. Use the &#x60;jobs/runs/get&#x60; API to check the run state after the job is submitted. # noqa: E501

    :param jobs_runs_submit_request: 
    :type jobs_runs_submit_request: dict | bytes

    :rtype: Union[JobsRunsSubmit200Response, Tuple[JobsRunsSubmit200Response, int], Tuple[JobsRunsSubmit200Response, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        jobs_runs_submit_request = JobsRunsSubmitRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def jobs_update(jobs_update_request):  # noqa: E501
    """Partially updates a job

    Add, update, or remove specific settings of an existing job. Use the Reset endpoint to overwrite all job settings. # noqa: E501

    :param jobs_update_request: 
    :type jobs_update_request: dict | bytes

    :rtype: Union[object, Tuple[object, int], Tuple[object, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        jobs_update_request = JobsUpdateRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
