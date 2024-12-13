# pollinations-python

A Python wrapper for accessing Pollinations AI API endpoints.

## Installation

```bash
pip install pypollinations
```

## API documentation

[API documentation](docs/api.md)

## Usage

### Image Generation

```python
import asyncio
from pollinations import ImageClient, ImageGenerationRequest
from PIL import Image
from io import BytesIO

async def generate_image(save_image_path: str = './examples/generated_images/',image_name: str = 'image.png'):
    # Initialize client
    client = ImageClient()

    try:
        # Create request
        request = ImageGenerationRequest(
            prompt="A beautiful sunset over mountains with snow peaks",
            width=1024,
            height=768,
            model="flux",
            nologo=True
        )

        # Generate image
        response = await client.generate(request)
        print(f"Image URL: {response.url}")
        print(f"Seed: {response.seed}")
        image_data = response.image_bytes
        try:
            image_data = Image.open(BytesIO(image_data))
            image_data.save(save_image_path + image_name)
            print(f"Image saved to {save_image_path}")
        except Exception as e:
            print(f"Error: {e}")



        # List available models
        models = await client.list_models()
        print("\nAvailable models:")
        print("\n".join(models))

    except Exception as e:
        print(f"Error: {e}")
    finally:
        await client.close()

if __name__ == "__main__":
    asyncio.run(generate_image())
```

### Text Generation

```python
import asyncio
from pollinations import TextClient, TextGenerationRequest
from pollinations.models.base import Message
from pollinations.exceptions import PollinationsError


async def generate_text():
    # Initialize client
    client = TextClient()

    try:
        request = TextGenerationRequest(
            messages=[
                Message(role="system", content="You are a helpful assistant"),
                Message(role="user", content="What is artificial intelligence?")
            ],
            model="openai",
            jsonMode=True,
            seed=42

        )

        # Generate text
        print("Generating response...\n")
        try:
            response = await client.generate(request)
            print(f"Response: {response.content}")
            print(f"Model: {response.model}")
            print(f"Seed: {response.seed}")

        except Exception as e:
            print(f"Failed to generate response: {e}")
            raise

        # List available models
        print("\nFetching available models...")
        try:
            models = await client.list_models()
            print("\n")
            print(models)
            print("\n")
            print("\nAvailable models:")
            for model in models:
                print(f"- {model['name']}: {model.get('type', 'unknown')}")
        except Exception as e:
            print(f"Failed to fetch models: {e}")

    except PollinationsError as e:
        print(f"API Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {type(e).__name__}: {e}")
    finally:
        await client.close()

if __name__ == "__main__":
    asyncio.run(generate_text())
```

## Features

- Easy integration with Pollinations AI services
- Support for various AI models
- Asynchronous requests support

## License

This project is licensed under the [Apache License 2.0](LICENSE).
