import pytest
import httpx
from unittest.mock import Mock

@pytest.fixture
def mock_response():
    response = Mock(spec=httpx.Response)
    response.status_code = 200
    return response

@pytest.fixture
def mock_client(mock_response):
    client = Mock(spec=httpx.AsyncClient)
    client.request.return_value = mock_response
    return client