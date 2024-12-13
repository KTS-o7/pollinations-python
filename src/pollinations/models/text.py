from typing import Optional
from pydantic import BaseModel
from .base import TextModel, Message

"""
Base models for the Pollinations API.

Attributes:
- TextGenerationRequest: Model for text generation requests.
- TextGenerationResponse: Model for text generation responses.
"""

class TextGenerationRequest(BaseModel):
    messages: list[Message]
    model: Optional[TextModel] = TextModel.OPENAI
    seed: Optional[int] = None
    jsonMode: Optional[bool] = False

class TextGenerationResponse(BaseModel):
    content: str
    model: str
    seed: Optional[int] = None