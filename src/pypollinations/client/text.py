
from typing import Optional
from ..models.text import TextGenerationRequest, TextGenerationResponse
from .base import BaseClient

class TextClient(BaseClient):
    """
    Client for the Pollinations Text API.
    
    Methods:
    - generate: Generate text.
        Returns:
        - TextGenerationResponse: A pydantic model representing the text response.
    - list_models: List available models. 
    """
    def __init__(self):
        super().__init__("https://text.pollinations.ai")
    
    async def generate(self, request: TextGenerationRequest) -> TextGenerationResponse:
        raw_response = await self._request(
            "POST",
            "/",
            json=request.model_dump(exclude_none=True)
        )
        response = TextGenerationResponse(content=raw_response.text,model=request.model,seed=request.seed)
        return response
    
    async def list_models(self) -> list[dict]:
        response = await self._request("GET", "/models")
        return response.json()