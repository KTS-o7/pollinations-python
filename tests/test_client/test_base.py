import pytest
import httpx
import pytest_asyncio
from unittest.mock import Mock, patch
from src.pollinations import APIError, PollinationsError
from src.pollinations.client.base import BaseClient

@pytest.fixture
def api_base():
    return "https://api.example.com"

@pytest_asyncio.fixture
async def client(api_base):
    client = BaseClient(api_base)
    yield client
    await client.close()

@pytest.mark.asyncio
async def test_init():
    """Test client initialization"""
    api_base = "https://api.example.com"
    client = BaseClient(api_base)
    assert client.api_base == api_base
    assert isinstance(client.client, httpx.AsyncClient)
    await client.close()

@pytest.mark.asyncio
async def test_context_manager():
    """Test async context manager"""
    async with BaseClient("https://api.example.com") as client:
        assert isinstance(client, BaseClient)

@pytest.mark.asyncio
async def test_close(client):
    """Test client close method"""
    with patch.object(client.client, 'aclose') as mock_aclose:
        await client.close()
        mock_aclose.assert_called_once()

@pytest.mark.asyncio
async def test_request_success(client):
    """Test successful request"""
    mock_response = Mock(spec=httpx.Response)
    mock_response.raise_for_status.return_value = None
    
    with patch.object(client.client, 'request', return_value=mock_response):
        response = await client._request(
            method="GET",
            path="/test",
            params={"key": "value"},
            json={"data": "test"},
            headers={"Authorization": "Bearer token"}
        )
        assert response == mock_response

@pytest.mark.asyncio
async def test_request_http_status_error(client):
    """Test request with HTTP status error"""
    mock_response = Mock(spec=httpx.Response)
    mock_response.status_code = 404
    mock_error = httpx.HTTPStatusError(
        message="404 Not Found",
        request=Mock(),
        response=mock_response
    )
    
    with patch.object(client.client, 'request', side_effect=mock_error):
        with pytest.raises(APIError) as exc_info:
            await client._request("GET", "/test")
        assert exc_info.value.status_code == 404

@pytest.mark.asyncio
async def test_request_http_error(client):
    """Test request with general HTTP error"""
    mock_error = httpx.HTTPError("Connection error")
    
    with patch.object(client.client, 'request', side_effect=mock_error):
        with pytest.raises(PollinationsError) as exc_info:
            await client._request("GET", "/test")
        assert str(exc_info.value) == "HTTP error: Connection error"

@pytest.mark.asyncio
async def test_request_url_construction(client):
    """Test URL construction in request"""
    mock_response = Mock(spec=httpx.Response)
    mock_response.raise_for_status.return_value = None
    
    with patch.object(client.client, 'request', return_value=mock_response) as mock_request:
        await client._request("GET", "/test")
        mock_request.assert_called_once()
        call_args = mock_request.call_args[1]
        assert call_args['url'] == f"{client.api_base}/test"