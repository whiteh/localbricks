# coding: utf-8

from fastapi.testclient import TestClient

from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.jobs_create200_response import JobsCreate200Response  # noqa: F401
from openapi_server.models.jobs_create_request import JobsCreateRequest  # noqa: F401
from openapi_server.models.jobs_delete_request import JobsDeleteRequest  # noqa: F401
from openapi_server.models.jobs_get200_response import JobsGet200Response  # noqa: F401
from openapi_server.models.jobs_list200_response import JobsList200Response  # noqa: F401
from openapi_server.models.jobs_reset_request import JobsResetRequest  # noqa: F401
from openapi_server.models.jobs_run_now200_response import JobsRunNow200Response  # noqa: F401
from openapi_server.models.jobs_run_now_request import JobsRunNowRequest  # noqa: F401
from openapi_server.models.jobs_runs_cancel_request import JobsRunsCancelRequest  # noqa: F401
from openapi_server.models.jobs_runs_delete_request import JobsRunsDeleteRequest  # noqa: F401
from openapi_server.models.jobs_runs_export200_response import JobsRunsExport200Response  # noqa: F401
from openapi_server.models.jobs_runs_get200_response import JobsRunsGet200Response  # noqa: F401
from openapi_server.models.jobs_runs_get_output200_response import JobsRunsGetOutput200Response  # noqa: F401
from openapi_server.models.jobs_runs_list200_response import JobsRunsList200Response  # noqa: F401
from openapi_server.models.jobs_runs_repair200_response import JobsRunsRepair200Response  # noqa: F401
from openapi_server.models.jobs_runs_repair_request import JobsRunsRepairRequest  # noqa: F401
from openapi_server.models.jobs_runs_submit200_response import JobsRunsSubmit200Response  # noqa: F401
from openapi_server.models.jobs_runs_submit_request import JobsRunsSubmitRequest  # noqa: F401
from openapi_server.models.jobs_update_request import JobsUpdateRequest  # noqa: F401
from openapi_server.models.views_to_export import ViewsToExport  # noqa: F401


def test_jobs_create(client: TestClient):
    """Test case for jobs_create

    Create a new job
    """
    jobs_create_request = JobsCreateRequest().dict()

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/2.1/jobs/create",
        headers=headers,
        json=jobs_create_request,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code == 200


def test_jobs_delete(client: TestClient):
    """Test case for jobs_delete

    Delete a job
    """
    jobs_delete_request = JobsDeleteRequest(job_id=1).dict()

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/2.1/jobs/delete",
        headers=headers,
        json=jobs_delete_request,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code == 200


def test_jobs_get(client: TestClient):
    """Test case for jobs_get

    Get a single job
    """
    params = [("job_id", 11223344)]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "GET",
        "/2.1/jobs/get",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code == 200


def test_jobs_list(client: TestClient):
    """Test case for jobs_list

    List all jobs
    """
    params = [("limit", 20),     ("offset", 0),     ("expand_tasks", False)]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "GET",
        "/2.1/jobs/list",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code == 200


def test_jobs_reset(client: TestClient):
    """Test case for jobs_reset

    Overwrites all settings for a job
    """
    jobs_reset_request = JobsResetRequest(job_id=1).dict()

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/2.1/jobs/reset",
        headers=headers,
        json=jobs_reset_request,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code == 200


def test_jobs_run_now(client: TestClient):
    """Test case for jobs_run_now

    Trigger a new job run
    """
    jobs_run_now_request = JobsRunNowRequest().dict()

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/2.1/jobs/run-now",
        headers=headers,
        json=jobs_run_now_request,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code == 200


def test_jobs_runs_cancel(client: TestClient):
    """Test case for jobs_runs_cancel

    Cancel a job run
    """
    jobs_runs_cancel_request = JobsRunsCancelRequest(run_id=1).dict()

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/2.1/jobs/runs/cancel",
        headers=headers,
        json=jobs_runs_cancel_request,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code == 200


def test_jobs_runs_delete(client: TestClient):
    """Test case for jobs_runs_delete

    Delete a job run
    """
    jobs_runs_delete_request = JobsRunsDeleteRequest().dict()

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/2.1/jobs/runs/delete",
        headers=headers,
        json=jobs_runs_delete_request,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code == 200


def test_jobs_runs_export(client: TestClient):
    """Test case for jobs_runs_export

    Export and retrieve a job run
    """
    params = [("run_id", 455644833),     ("views_to_export", ViewsToExport())]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "GET",
        "/2.0/jobs/runs/export",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code == 200


def test_jobs_runs_get(client: TestClient):
    """Test case for jobs_runs_get

    Get a single job run
    """
    params = [("run_id", 455644833),     ("include_history", True)]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "GET",
        "/2.1/jobs/runs/get",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code == 200


def test_jobs_runs_get_output(client: TestClient):
    """Test case for jobs_runs_get_output

    Get the output for a single run
    """
    params = [("run_id", 455644833)]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "GET",
        "/2.1/jobs/runs/get-output",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code == 200


def test_jobs_runs_list(client: TestClient):
    """Test case for jobs_runs_list

    List runs for a job
    """
    params = [("active_only", False),     ("completed_only", False),     ("job_id", 11223344),     ("offset", 0),     ("limit", 25),     ("run_type", 'JOB_RUN'),     ("expand_tasks", False),     ("start_time_from", 1642521600000),     ("start_time_to", 1642608000000)]
    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "GET",
        "/2.1/jobs/runs/list",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code == 200


def test_jobs_runs_repair(client: TestClient):
    """Test case for jobs_runs_repair

    Repair a job run
    """
    jobs_runs_repair_request = JobsRunsRepairRequest().dict()

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/2.1/jobs/runs/repair",
        headers=headers,
        json=jobs_runs_repair_request,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code == 200


def test_jobs_runs_submit(client: TestClient):
    """Test case for jobs_runs_submit

    Create and trigger a one-time run
    """
    jobs_runs_submit_request = JobsRunsSubmitRequest().dict()

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/2.1/jobs/runs/submit",
        headers=headers,
        json=jobs_runs_submit_request,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code == 200


def test_jobs_update(client: TestClient):
    """Test case for jobs_update

    Partially updates a job
    """
    jobs_update_request = JobsUpdateRequest(job_id=1).dict()

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = client.request(
        "POST",
        "/2.1/jobs/update",
        headers=headers,
        json=jobs_update_request,
    )

    # uncomment below to assert the status code of the HTTP response
    assert response.status_code == 200

