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
            seed=41
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