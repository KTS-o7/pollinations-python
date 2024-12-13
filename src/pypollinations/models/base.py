from enum import Enum
from pydantic import BaseModel

"""
Base models for the Pollinations API.

Attributes:
- ImageModel: Enum representing image models.
- TextModel: Enum representing text models.
- Message: Base model for messages.
 
"""

class ImageModel(str, Enum):
    FLUX = "flux"
    FLUX_REALISM = "flux-realism"
    FLUX_CABLYAI = "flux-cablyai"
    FLUX_ANIME = "flux-anime"
    FLUX_3D = "flux-3d"
    ANY_DARK = "any-dark"
    FLUX_PRO = "flux-pro"
    TURBO = "turbo"

class TextModel(str, Enum):
    OPENAI = "openai"
    MISTRAL = "mistral"
    MISTRAL_LARGE = "mistral-large"
    LLAMA = "llama"
    COMMAND_R = "command-r"
    UNITY = "unity"
    MIDIJOURNEY = "midijourney"
    RTIST = "rtist"
    SEARCHGPT = "searchgpt"
    EVIL = "evil"
    QWEN_CODER = "qwen-coder"
    P1 = "p1"

class Message(BaseModel):
    role: str
    content: str