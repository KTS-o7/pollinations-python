
import pytest
from pydantic import ValidationError
from src.pypollinations.models.image import ImageGenerationRequest, ImageResponse
from src.pypollinations.models.base import ImageModel

def test_image_generation_request_defaults():
    request = ImageGenerationRequest(prompt="test prompt")
    assert request.prompt == "test prompt"
    assert request.model == ImageModel.FLUX
    assert request.seed is None
    assert request.width == 1024
    assert request.height == 1024
    assert request.nologo is False
    assert request.private is False
    assert request.enhance is False
    assert request.safe is False

def test_image_generation_request_custom():
    request = ImageGenerationRequest(
        prompt="custom prompt",
        model=ImageModel.FLUX,
        seed=42,
        width=512,
        height=512,
        nologo=True,
        private=True,
        enhance=True,
        safe=True
    )
    assert request.prompt == "custom prompt"
    assert request.model == ImageModel.FLUX
    assert request.seed == 42
    assert request.width == 512
    assert request.height == 512
    assert request.nologo is True
    assert request.private is True
    assert request.enhance is True
    assert request.safe is True

def test_image_generation_request_validation():
    with pytest.raises(ValidationError):
        ImageGenerationRequest(prompt="test", width=32)  # width too small
    
    with pytest.raises(ValidationError):
        ImageGenerationRequest(prompt="test", height=3000)  # height too large

def test_image_response_minimal():
    response = ImageResponse(url="https://example.com/image.jpg")
    assert response.url == "https://example.com/image.jpg"
    assert response.seed is None
    assert response.image_bytes is None

def test_image_response_full():
    response = ImageResponse(
        url="https://example.com/image.jpg",
        seed=42,
        image_bytes=b"fake_image_data"
    )
    assert response.url == "https://example.com/image.jpg"
    assert response.seed == 42
    assert response.image_bytes == b"fake_image_data"