import pytest
from pollinations.client.image import ImageClient
from pollinations.models.image import ImageGenerationRequest

@pytest.mark.asyncio
async def test_image_generation():
    client = ImageClient()
    request = ImageGenerationRequest(
        prompt="test image",
        width=512,
        height=512
    )
    
    response = await client.generate(request)
    assert response.url is not None
    assert response.url.startswith("https://")
    assert isinstance(response.image_bytes, bytes)

@pytest.mark.asyncio
async def test_list_models():
    client = ImageClient()
    models = await client.list_models()
    assert isinstance(models, list)