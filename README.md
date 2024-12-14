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

#### Code Example
```python
import asyncio
from pypollinations import ImageClient, ImageGenerationRequest
from PIL import Image
from io import BytesIO
```

#### Client Setup and Image Generation
```python
async def generate_image(
    save_image_path: str = "./examples/generated_images/", 
    image_name: str = "image.png"
):
    client = ImageClient()
    try:
        request = ImageGenerationRequest(
            prompt="A beautiful sunset over mountains with snow peaks",
            width=1024,
            height=768,
            model="flux",
            nologo=True,
        )
        response = await client.generate(request)
        print(f"Image URL: {response.url}")
        print(f"Seed: {response.seed}")
```

#### Image Saving
```python
        image_data = response.image_bytes
        try:
            image_data = Image.open(BytesIO(image_data))
            image_data.save(save_image_path + image_name)
            print(f"Image saved to {save_image_path}")
        except Exception as e:
            print(f"Error: {e}")
```

#### Model Listing and Main Execution
```python
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

> Output
> [![Generated Image](./examples/generated_images/image.png)](./examples/generated_images/image.png)

### Text Generation

#### Basic Setup
```python
import asyncio
from pypollinations import TextClient, TextGenerationRequest
from pypollinations.models.base import Message
from pypollinations.exceptions import PollinationsError
```

#### Text Generation Implementation
```python
async def generate_text():
    client = TextClient()
    try:
        request = TextGenerationRequest(
            messages=[Message(role="user", content="What is artificial intelligence?")],
            model="openai",
            jsonMode=True,
            seed=41,
            temperature=0.5,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            top_p=1.0,
            system="You are a helpful AI assistant.",
        )
```

#### Response Handling
```python
        print("Generating response...\n")
        try:
            response = await client.generate(request)
            print(f"Response: {response.content}")
            print(f"Model: {response.model}")
            print(f"Seed: {response.seed}")
            print(f"Temperature: {response.temperature}")
            print(f"Frequency penalty: {response.frequency_penalty}")
            print(f"Presence penalty: {response.presence_penalty}")
            print(f"Top p: {response.top_p}")
```

#### Error Handling and Model Listing
```python
        except Exception as e:
            print(f"Failed to generate response: {e}")
            raise

        print("\nFetching available models...")
        try:
            models = await client.list_models()
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

> Output

```text
Generating response...

Response: Artificial Intelligence (AI) is a broad field of computer science dedicated to creating smart machines capable of performing tasks that typically require human intelligence. These tasks include learning, reasoning, problem-solving, perception, and language understanding. Here are some key aspects of AI:

1. **Machine Learning (ML)**: A subset of AI that involves training algorithms to learn from data, make predictions, or improve performance over time.

2. **Deep Learning (DL)**: A subset of machine learning that uses neural networks with many layers to analyze and classify data, often used for tasks like image and speech recognition.

3. **Natural Language Processing (NLP)**: A branch of AI focused on enabling computers to understand, interpret, and generate human language.

4. **Computer Vision**: A field of AI that deals with enabling computers to interpret and understand the visual world, often using data from cameras and sensors.

5. **Robotics**: AI is used to develop robots that can perform tasks autonomously or with guidance, often incorporating computer vision and other AI subfields.

6. **Expert Systems**: These are AI systems that use knowledge and inference rules to provide explanations or make decisions in specific domains.

AI has a wide range of applications, from voice assistants like Siri and Alexa to self-driving cars, medical diagnosis, fraud detection, and more. The goal of AI is to augment and enhance human capabilities, automate routine tasks, and solve complex problems efficiently.
Model: openai
Seed: 41
Temperature: 0.5
Frequency penalty: 0.0
Presence penalty: 0.0
Top p: 1.0

Fetching available models...

Available models:
- openai: chat
- mistral: chat
- mistral-large: chat
- llama: completion
- command-r: chat
- unity: chat
- midijourney: chat
- rtist: chat
- searchgpt: chat
- evil: chat
- qwen-coder: chat
- p1: chat
```

## Features

- Easy integration with Pollinations AI services
- Support for various AI models
- Asynchronous requests support

## License

This project is licensed under the [Apache License 2.0](LICENSE).
