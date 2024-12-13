# Pollinations Library API Documentation

The Pollinations library is an asynchronous Python client that provides interfaces to the Pollinations Text and Image APIs. It allows users to generate text and images using various models offered by the Pollinations platform.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Core Components](#core-components)
  - [Image Generation API](#image-generation-api)
  - [Text Generation API](#text-generation-api)
- [Error Handling](#error-handling)

## Overview

The Pollinations library provides asynchronous Python clients for interacting with Pollinations AI's text and image generation services. The library offers two main clients:

- **ImageClient** for generating images from text prompts
- **TextClient** for generating text responses

## Installation

```bash
pip install pollinations
```

## Core Components

### Image Generation API

#### ImageClient

The client for generating images from text prompts.

```python
from pollinations import ImageClient, ImageGenerationRequest

client = ImageClient()
```

##### Methods

###### `async generate(request: ImageGenerationRequest) -> ImageResponse`

Generates an image based on the provided request parameters.

```python
response = await client.generate(ImageGenerationRequest(
        prompt="A beautiful sunset",
        width=1024,
        height=768,
        model="flux"
))
```

###### `async list_models() -> list[str]`

Returns a list of available image generation models.

```python
models = await client.list_models()
```

#### ImageGenerationRequest

Configuration model for image generation requests.

```python
class ImageGenerationRequest:
        prompt: str            # Text description of the desired image
        model: str            # Model to use (default: "flux")
        width: int           # Image width (64-2048px)
        height: int          # Image height (64-2048px)
        seed: int | None     # Optional seed for reproducible results
        nologo: bool         # Remove watermark if True
        private: bool        # Make generation private
        enhance: bool        # Apply image enhancement
        safe: bool          # Enable safety filters
```

#### ImageResponse

Response model containing the generated image data.

```python
class ImageResponse:
        url: str            # URL to the generated image
        seed: int | None    # Seed used for generation
        image_bytes: bytes  # Raw image data
```

### Text Generation API

#### TextClient

The client for generating text responses.

```python
from pollinations import TextClient, TextGenerationRequest
from pollinations.models.base import Message

client = TextClient()
```

##### Methods

###### `async generate(request: TextGenerationRequest) -> TextGenerationResponse`

Generates text based on the provided messages and parameters.

```python
response = await client.generate(TextGenerationRequest(
        messages=[
                Message(role="system", content="You are a helpful assistant"),
                Message(role="user", content="What is AI?")
        ],
        model="openai"
))
```

###### `async list_models() -> list[dict]`

Returns a list of available text generation models with their details.

```python
models = await client.list_models()
```

#### TextGenerationRequest

Configuration model for text generation requests.

```python
class TextGenerationRequest:
        messages: list[Message]  # List of conversation messages
        model: str              # Model to use (default: "openai")
        seed: int | None        # Optional seed for reproducible results
        jsonMode: bool          # Return response in JSON format
```

#### Message

Model representing a conversation message.

```python
class Message:
        role: str      # Role ("system", "user", "assistant")
        content: str   # Message content
```

#### TextGenerationResponse

Response model containing the generated text.

```python
class TextGenerationResponse:
        content: str    # Generated text response
        model: str      # Model used for generation
        seed: int      # Seed used (if provided)
```

## Error Handling

The library provides custom exceptions:

```python
from pollinations.exceptions import PollinationsError

try:
        response = await client.generate(request)
except PollinationsError as e:
        print(f"API Error: {e}")
```
