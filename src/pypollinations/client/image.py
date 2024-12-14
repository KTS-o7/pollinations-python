from ..models.image import ImageGenerationRequest, ImageResponse
from .base import BaseClient
from ..exceptions import APIError, ValidationError


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
        try:
            raw_response = await self._request(
                "GET",
                f"/prompt/{request.prompt}",
                params={
                    k: str(v).lower() if isinstance(v, bool) else v
                    for k, v in params.items()
                    if k != "prompt"
                },
            )

            try:
                response = ImageResponse(
                    url=str(raw_response.url),
                    seed=request.seed,
                    image_bytes=raw_response.content,
                )
                return response

            except ValidationError as validation_error:
                raise ValidationError(message=validation_error.message)

        except APIError as api_error:
            raise APIError(status_code=api_error.status_code, message=api_error.message)

    async def list_models(self) -> list[str]:
        try:
            response = await self._request("GET", "/models")
            return response.json()

        except APIError as api_error:
            raise APIError(status_code=api_error.status_code, message=api_error.message)
