import requests
import requests.packages
import urllib3
import logging
from json import JSONDecodeError

from requests import HTTPError

from wmata_api.core.exceptions import WmataApiException
from wmata_api.core.result import Result

from typing import Dict, Optional


class RestAdapter:
    def __init__(self, api_key: str, logger: logging.Logger, ssl_verify: bool = True):
        """
        Constructor.
        :param api_key: Required for access to WMATA API
        :param ssl_verify: Normally set to True, but if having SSL/TLS cert validation issues, can turn off with False
        :param logger: If your app has a logger, pass it in here
        """
        self._api_key = api_key
        self._ssl_verify = ssl_verify
        self._logger = logger

        if not ssl_verify:
            urllib3.disable_warnings()

    def get(self, url: str, params: Optional[Dict] = None) -> Result:
        """
        Sends a GET request to the specified endpoint, ensuring JSON contentType.
        Handles connection errors, HTTP status errors, and invalid JSON responses

        :param url: full url to send request to
        :param params: Optional query parameters
        :return: A Result object
        :raises: WmataApiException for request or parsing issues
        """
        headers = {'api_key': self._api_key}

        log_line_pre = "method=GET, url={}, params={}".format(url, params)
        log_line_post = ', '.join([log_line_pre, "success={}, status_code={}, message={}"])

        try:
            self._logger.debug(log_line_pre)
            response = requests.get(url, verify=self._ssl_verify, headers=headers, params=params)

            try:
                response.raise_for_status()
            except HTTPError as e:
                self._logger.warning(log_line_post.format(False, response.status_code, response.reason))
                raise WmataApiException(f"HTTP error: {response.status_code} {response.reason}") from e

        except requests.exceptions.RequestException as e:
            self._logger.error((str(e)))
            raise WmataApiException("Request failed") from e

        try:
            data = response.json()
            print(data)
        except (ValueError, JSONDecodeError, TypeError) as e:
            self._logger.error(log_line_post.format(False, None, e))
            raise WmataApiException(f"Invalid JSON from {url}: {response.text}") from e

        log_line = f"{log_line_pre}, success=True, status_code={response.status_code}, message={data.keys()}"
        self._logger.debug(msg=log_line)
        return Result(response.status_code, message=response.reason, data=data)