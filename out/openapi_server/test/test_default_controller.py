# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

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
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_jobs_create(self):
        """Test case for jobs_create

        Create a new job
        """
        jobs_create_request = openapi_server.JobsCreateRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/2.1/jobs/create',
            method='POST',
            headers=headers,
            data=json.dumps(jobs_create_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_jobs_delete(self):
        """Test case for jobs_delete

        Delete a job
        """
        jobs_delete_request = openapi_server.JobsDeleteRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/2.1/jobs/delete',
            method='POST',
            headers=headers,
            data=json.dumps(jobs_delete_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_jobs_get(self):
        """Test case for jobs_get

        Get a single job
        """
        query_string = [('job_id', 11223344)]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/2.1/jobs/get',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_jobs_list(self):
        """Test case for jobs_list

        List all jobs
        """
        query_string = [('limit', 20),
                        ('offset', 0),
                        ('expand_tasks', False)]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/2.1/jobs/list',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_jobs_reset(self):
        """Test case for jobs_reset

        Overwrites all settings for a job
        """
        jobs_reset_request = openapi_server.JobsResetRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/2.1/jobs/reset',
            method='POST',
            headers=headers,
            data=json.dumps(jobs_reset_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_jobs_run_now(self):
        """Test case for jobs_run_now

        Trigger a new job run
        """
        jobs_run_now_request = openapi_server.JobsRunNowRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/2.1/jobs/run-now',
            method='POST',
            headers=headers,
            data=json.dumps(jobs_run_now_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_jobs_runs_cancel(self):
        """Test case for jobs_runs_cancel

        Cancel a job run
        """
        jobs_runs_cancel_request = openapi_server.JobsRunsCancelRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/2.1/jobs/runs/cancel',
            method='POST',
            headers=headers,
            data=json.dumps(jobs_runs_cancel_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_jobs_runs_delete(self):
        """Test case for jobs_runs_delete

        Delete a job run
        """
        jobs_runs_delete_request = openapi_server.JobsRunsDeleteRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/2.1/jobs/runs/delete',
            method='POST',
            headers=headers,
            data=json.dumps(jobs_runs_delete_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_jobs_runs_export(self):
        """Test case for jobs_runs_export

        Export and retrieve a job run
        """
        query_string = [('run_id', 455644833),
                        ('views_to_export', openapi_server.ViewsToExport())]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/2.0/jobs/runs/export',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_jobs_runs_get(self):
        """Test case for jobs_runs_get

        Get a single job run
        """
        query_string = [('run_id', 455644833),
                        ('include_history', true)]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/2.1/jobs/runs/get',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_jobs_runs_get_output(self):
        """Test case for jobs_runs_get_output

        Get the output for a single run
        """
        query_string = [('run_id', 455644833)]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/2.1/jobs/runs/get-output',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_jobs_runs_list(self):
        """Test case for jobs_runs_list

        List runs for a job
        """
        query_string = [('active_only', False),
                        ('completed_only', False),
                        ('job_id', 11223344),
                        ('offset', 0),
                        ('limit', 25),
                        ('run_type', 'JOB_RUN'),
                        ('expand_tasks', False),
                        ('start_time_from', 1642521600000),
                        ('start_time_to', 1642608000000)]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/2.1/jobs/runs/list',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_jobs_runs_repair(self):
        """Test case for jobs_runs_repair

        Repair a job run
        """
        jobs_runs_repair_request = openapi_server.JobsRunsRepairRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/2.1/jobs/runs/repair',
            method='POST',
            headers=headers,
            data=json.dumps(jobs_runs_repair_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_jobs_runs_submit(self):
        """Test case for jobs_runs_submit

        Create and trigger a one-time run
        """
        jobs_runs_submit_request = openapi_server.JobsRunsSubmitRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/2.1/jobs/runs/submit',
            method='POST',
            headers=headers,
            data=json.dumps(jobs_runs_submit_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_jobs_update(self):
        """Test case for jobs_update

        Partially updates a job
        """
        jobs_update_request = openapi_server.JobsUpdateRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/2.1/jobs/update',
            method='POST',
            headers=headers,
            data=json.dumps(jobs_update_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
