from ..models.text import TextGenerationRequest, TextGenerationResponse
from .base import BaseClient
from ..exceptions import APIError, ValidationError


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
        try:
            raw_response = await self._request(
                "POST", "/", json=request.model_dump(exclude_none=True)
            )
            try:
                response = TextGenerationResponse(
                    content=raw_response.text,
                    model=request.model,
                    seed=request.seed,
                    temperature=request.temperature,
                    frequency_penalty=request.frequency_penalty,
                    presence_penalty=request.presence_penalty,
                    top_p=request.top_p,
                )
                return response

            except ValidationError as validation_error:
                raise ValidationError(message=validation_error.message)

        except APIError as api_error:
            raise APIError(status_code=api_error.status_code, message=api_error.message)

    async def list_models(self) -> list[dict]:
        try:
            response = await self._request("GET", "/models")
            return response.json()

        except APIError as api_error:
            raise APIError(status_code=api_error.status_code, message=api_error.message)
