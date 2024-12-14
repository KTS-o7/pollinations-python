import pytest
from pydantic import ValidationError
from src.pypollinations.models.text import TextGenerationRequest, TextGenerationResponse
from src.pypollinations.models.base import TextModel, Message


def test_text_generation_request_valid():
    messages = [Message(role="user", content="Hello")]
    request = TextGenerationRequest(messages=messages)
    assert request.messages == messages
    assert request.model == TextModel.OPENAI
    assert request.seed is None
    assert request.jsonMode is False


def test_text_generation_request_all_fields():
    messages = [Message(role="user", content="Hello")]
    request = TextGenerationRequest(
        messages=messages,
        model=TextModel.OPENAI,
        seed=42,
        jsonMode=True,
        temperature=0.5,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        top_p=1.0,
    )
    assert request.messages == messages
    assert request.model == TextModel.OPENAI
    assert request.seed == 42
    assert request.jsonMode is True
    assert request.temperature == 0.5
    assert request.frequency_penalty == 0.0
    assert request.presence_penalty == 0.0
    assert request.top_p == 1.0


def test_text_generation_request_missing_required():
    with pytest.raises(ValidationError):
        TextGenerationRequest()


def test_text_generation_response_valid():
    response = TextGenerationResponse(content="Hello world", model="openai")
    assert response.content == "Hello world"
    assert response.model == "openai"
    assert response.seed is None


def test_text_generation_response_all_fields():
    response = TextGenerationResponse(
        content="Hello world",
        model="openai",
        seed=42,
        temperature=0.5,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        top_p=1.0,
    )
    assert response.content == "Hello world"
    assert response.model == "openai"
    assert response.seed == 42
    assert response.temperature == 0.5
    assert response.frequency_penalty == 0.0
    assert response.presence_penalty == 0.0
    assert response.top_p == 1.0


def test_text_generation_response_missing_required():
    with pytest.raises(ValidationError):
        TextGenerationResponse()
