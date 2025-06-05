from unittest import TestCase
from unittest.mock import patch, Mock
from requests.exceptions import HTTPError, RequestException

from wmata_api.core.exceptions import WmataApiException
from wmata_api.core.rest_adapter import RestAdapter


class TestRestAdapter(TestCase):

    def setUp(self):
        self.adapter = RestAdapter('api.wmata.test', api_key='therailskeepgoing', ssl_verify=False)

    @patch("wmata_api.core.rest_adapter.requests.get")
    def test_get_successful_response(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.reason = "OK"
        mock_response.json.return_value = {"key": "value"}

        mock_get.return_value = mock_response

        result = self.adapter.get(endpoint="/TestEndpoint")
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data, {"key": "value"})

    @patch("wmata_api.core.rest_adapter.requests.get")
    def test_get_http_error(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.reason = "Not Found"
        mock_response.raise_for_status.side_effect = HTTPError("404 Not Found")
        mock_response.json.return_value = {}

        mock_get.return_value = mock_response

        with self.assertRaises(WmataApiException) as context:
            self.adapter.get(endpoint="/NotFound")

        self.assertIn("HTTP error", str(context.exception))

    @patch("wmata_api.core.rest_adapter.requests.get")
    def test_get_request_exception(self, mock_get):
        mock_get.side_effect = RequestException("Connection failed")

        with self.assertRaises(WmataApiException) as context:
            self.adapter.get(endpoint="/Fail")

        self.assertIn("Request failed", str(context.exception))

    @patch("wmata_api.core.rest_adapter.requests.get")
    def test_get_invalid_json(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.reason = "OK"
        mock_response.json.side_effect = ValueError("Invalid JSON")

        mock_get.return_value = mock_response

        with self.assertRaises(WmataApiException) as context:
            self.adapter.get(endpoint="/InvalidJson")

        self.assertIn("Invalid JSON", str(context.exception))