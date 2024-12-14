import asyncio
from pypollinations import TextClient, TextGenerationRequest
from pypollinations.models.base import Message
from pypollinations.exceptions import PollinationsError


async def generate_text():
    # Initialize client
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

        # Generate text
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

        except Exception as e:
            print(f"Failed to generate response: {e}")
            raise

        # List available models
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
