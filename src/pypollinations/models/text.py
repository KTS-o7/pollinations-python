from typing import Optional
from pydantic import BaseModel, Field
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
    contextual: Optional[bool] = False
    jsonMode: Optional[bool] = False
    system: Optional[str] = None
    temperature: Optional[float] = Field(default=0.5, ge=0.0, le=1.0)
    frequency_penalty: Optional[float] = Field(default=0.0, ge=0.0, le=1.0)
    presence_penalty: Optional[float] = Field(default=0.0, ge=0.0, le=1.0)
    top_p: Optional[float] = Field(default=1.0, ge=0.0, le=1.0)


class TextGenerationResponse(BaseModel):
    content: str
    model: str
    seed: Optional[int] = None
    temperature: Optional[float] = None
    frequency_penalty: Optional[float] = None
    presence_penalty: Optional[float] = None
    top_p: Optional[float] = None
