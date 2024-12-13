from typing import Optional
from pydantic import BaseModel, Field
from .base import ImageModel

"""
Base models for the Pollinations API.

Attributes:
- ImageGenerationRequest: Model for image generation requests.
- ImageResponse: Model for image generation responses. 

"""

class ImageGenerationRequest(BaseModel):
    prompt: str
    model: Optional[ImageModel] = Field(default=ImageModel.FLUX)
    seed: Optional[int] = None
    width: Optional[int] = Field(default=1024, ge=64, le=2048)
    height: Optional[int] = Field(default=1024, ge=64, le=2048)
    nologo: Optional[bool] = False
    private: Optional[bool] = False
    enhance: Optional[bool] = False
    safe: Optional[bool] = False

class ImageResponse(BaseModel):
    url: str
    seed: Optional[int] = None
    image_bytes: bytes = None