from . import FlaskTestCase
import json

class TestTeamsInterface(FlaskTestCase):
    def test_get_all_teams_data(self):
        result = self.app.get('/teams/')
        assert result.status_code == 200
        assert json.loads(result.data) == self.data['teams']

    def test_get_all_teams_data_with_params(self):
        query_data = {
            "failure": "assured"
        }
        result_data = {
            "type": "IllegalParameter",
            "reason": "Parameters are not allowed for this interface."
        }
        result = self.app.get('/teams/', data=json.dumps(query_data))
        assert result.status_code == 403
        assert json.loads(result.data) == result_data

    def test_get_specific_team_data(self):
        result = self.app.get('/teams/6')
        assert result.status_code == 200
        assert json.loads(result.data) == self.data['teams']['6']

    def test_get_specific_team_data_with_params(self):
        query_data = {
            "failure": "assured"
        }
        result_data = {
            "type": "IllegalParameter",
            "reason": "Parameters are not allowed for this interface."
        }
        result = self.app.get('/teams/6', data=json.dumps(query_data))
        assert result.status_code == 403
        assert json.loads(result.data) == result_data

    def test_create_team_data(self):
        query_data = {
            "name": "University of Washington, Tacoma",
            "id": "7"
        }
        result_data = {
            "name": "University of Washington, Tacoma",
            "score": 0
        }
        post = self.app.post('/teams/', data=json.dumps(query_data), follow_redirects=True)
        assert post.status_code == 201
        assert post.headers['Location'] == 'http://localhost/teams/7'
        result = self.app.get('/teams/7')
        assert result.status_code == 200
        assert json.loads(result.data) == result_data

    def test_create_team_data_invalid_param(self):
        query_data = {
            "name": "University of Washington, Tacoma",
            "id": "7",
            "failure": "assured"
        }
        post_data = {
            "type": "IllegalParameter",
            "reason": "Parameter 'failure' is not valid for this interface."
        }
        post = self.app.post('/teams/', data=json.dumps(query_data), follow_redirects=True)
        assert post.status_code == 403
        assert json.loads(post.data) == post_data
        result = self.app.get('/teams/7')
        assert result.status_code == 404

    def test_create_team_data_missing_param(self):
        query_data = {
            "name": "University of Washington, Tacoma"
        }
        post_data = {
            "type": "IllegalParameter",
            "reason": "Required parameter 'id' is not specified."
        }
        result_data = self.data['teams']
        post = self.app.post('/teams/', data=json.dumps(query_data), follow_redirects=True)
        assert post.status_code == 403
        assert json.loads(post.data) == post_data
        result = self.app.get('/teams/')
        assert result.status_code == 200
        assert json.loads(result.data) == result_data

    def test_create_team_data_no_data(self):
        post_data = {
            "type": "IllegalParameter",
            "reason": "No parameters were specified."
        }
        post = self.app.post('/teams/', follow_redirects=True)
        assert post.status_code == 403
        assert json.loads(post.data) == post_data

    def test_modify_team_data(self):
        query_data = {
            "name": "WWU"
        }
        result_data = {
            "name": "WWU",
            "score": 0
        }
        patch = self.app.patch('/teams/2', data=json.dumps(query_data))
        assert patch.status_code == 204
        result = self.app.get('/teams/2')
        assert result.status_code == 200
        assert json.loads(result.data) == result_data

    def test_modify_team_data_invalid_param(self):
        query_data = {
            "name": "WWU",
            "id": "7"
        }
        patch_data = {
            "type": "IllegalParameter",
            "reason": "Parameter 'id' is not valid for this interface."
        }
        result_data = self.data['teams']['2']
        patch = self.app.patch('/teams/2', data=json.dumps(query_data))
        assert patch.status_code == 403
        assert json.loads(patch.data) == patch_data
        result = self.app.get('/teams/2')
        assert result.status_code == 200
        assert json.loads(result.data) == result_data

    def test_modify_team_data_no_param(self):
        query_data = {}
        result_data = self.data['teams']['2']
        patch = self.app.patch('/teams/2', data=json.dumps(query_data))
        assert patch.status_code == 204
        result = self.app.get('/teams/2')
        assert result.status_code == 200
        assert json.loads(result.data) == result_data

    def test_modify_team_data_no_data(self):
        patch_data = {
            "type": "IllegalParameter",
            "reason": "No parameters were specified."
        }
        patch = self.app.patch('/teams/2')
        assert patch.status_code == 403
        assert json.loads(patch.data) == patch_data

    def test_delete_team_data(self):
        delete = self.app.delete('/teams/1')
        assert delete.status_code == 204
        result = self.app.get('/teams/1')
        assert result.status_code == 404

    def test_delete_team_data_with_params(self):
        query_data = {
            "failure": "assured"
        }
        delete_data = {
            "type": "IllegalParameter",
            "reason": "Parameters are not allowed for this interface."
        }
        delete = self.app.delete('/teams/1', data=json.dumps(query_data))
        assert delete.status_code == 403
        assert json.loads(delete.data) == delete_data