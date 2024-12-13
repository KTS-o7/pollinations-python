import pytest
from unittest.mock import AsyncMock, patch, Mock
import aiohttp
from typing import Optional
from src.pypollinations.models.base import Message
from src.pypollinations.models.text import TextGenerationRequest, TextGenerationResponse
from src.pypollinations.client.text import TextClient

@pytest.fixture
async def text_client():
    client = TextClient()
    yield client
    await client.close()  # Cleanup

@pytest.mark.asyncio
async def test_generate_text():
    # Arrange
    client = TextClient()
    mock_response = AsyncMock()
    mock_response.text = "Generated text response"
    
    request = TextGenerationRequest(
         messages=[
                Message(role="system", content="You are a helpful assistant"),
                Message(role="user", content="What is artificial intelligence?")
            ],
        model="openai",
        seed=42
    )
    
    with patch.object(client, '_request', return_value=mock_response) as mock_request:
        # Act
        response = await client.generate(request)
        
        # Assert
        assert isinstance(response, TextGenerationResponse)
        assert response.content == "Generated text response"
        assert response.model == "openai"
        assert response.seed == 42
        
        mock_request.assert_called_once_with(
            "POST",
            "/",
            json=request.model_dump(exclude_none=True)
        )

@pytest.mark.asyncio
async def test_list_models():
    # Arrange
    client = TextClient()
    expected_models = [{'name': 'openai', 'type': 'chat', 'censored': True, 'description': 'OpenAI GPT-4o', 'baseModel': True}, {'name': 'mistral', 'type': 'chat', 'censored': False, 'description': 'Mistral Nemo', 'baseModel': True}, {'name': 'mistral-large', 'type': 'chat', 'censored': False, 'description': 'Mistral Large (v2)', 'baseModel': True}, {'name': 'llama', 'type': 'completion', 'censored': True, 'description': 'Llama 3.1', 'baseModel': True}, {'name': 'command-r', 'type': 'chat', 'censored': False, 'description': 'Command-R', 'baseModel': False}, {'name': 'unity', 'type': 'chat', 'censored': False, 'description': 'Unity with Mistral Large by Unity AI Lab', 'baseModel': False}, {'name': 'midijourney', 'type': 'chat', 'censored': True, 'description': 'Midijourney musical transformer', 'baseModel': False}, {'name': 'rtist', 'type': 'chat', 'censored': True, 'description': 'Rtist image generator by @bqrio', 'baseModel': False}, {'name': 'searchgpt', 'type': 'chat', 'censored': True, 'description': 'SearchGPT with realtime news and web search', 'baseModel': False}, {'name': 'evil', 'type': 'chat', 'censored': False, 'description': 'Evil Mode - Experimental', 'baseModel': False}, {'name': 'qwen-coder', 'type': 'chat', 'censored': True, 'description': 'Qwen Coder 32b Instruct (Supposedly better than GPT-4o at coding)', 'baseModel': True}, {'name': 'p1', 'type': 'chat', 'censored': False, 'description': 'Pollinations 1 (OptiLLM)', 'baseModel': False}]
 # Create a mock response where json() returns the expected models immediately
    mock_response = AsyncMock()
    mock_response.json = Mock(return_value=expected_models)  # Use regular Mock instead of AsyncMock
    
    with patch.object(client, '_request', return_value=mock_response) as mock_request:
        # Act
        response = await client.list_models()
        
        # Assert
        assert response == expected_models
        mock_request.assert_called_once_with("GET", "/models")

@pytest.mark.asyncio
async def test_generate_text_with_optional_params():
    # Arrange
    client = TextClient()
    mock_response = AsyncMock()
    mock_response.text = "Generated text response"
    
    request = TextGenerationRequest(
        messages=[
                Message(role="system", content="You are a helpful assistant"),
                Message(role="user", content="What is artificial intelligence?")
            ],
        model="openai",
        seed=None  # Testing with optional parameter
    )
    
    with patch.object(client, '_request', return_value=mock_response) as mock_request:
        # Act
        response = await client.generate(request)
        
        # Assert
        assert isinstance(response, TextGenerationResponse)
        assert isinstance(response.content, str)
        assert response.model == "openai"
        assert response.seed is None
