from ..models.image import ImageGenerationRequest, ImageResponse
from .base import BaseClient
class ImageClient(BaseClient):
    """
    Client for the Pollinations Image API.
    
    Methods:
    - generate: Generate an image.
        Returns:
        - ImageResponse: A pydantic model representing the image response.
    - list_models: List available models.
     
    """
    def __init__(self):
        super().__init__("https://image.pollinations.ai")
    
    async def generate(self, request: ImageGenerationRequest) -> ImageResponse:
        params = request.model_dump(exclude_none=True)
        response = await self._request(
            "GET",
            f"/prompt/{request.prompt}",
            params={k: str(v).lower() if isinstance(v, bool) else v 
                   for k, v in params.items() if k != "prompt"}
        )
        
        return ImageResponse(url=str(response.url),seed=request.seed, image_bytes=response.content)
    
    async def list_models(self) -> list[str]:
        response = await self._request("GET", "/models")
        return response.json()