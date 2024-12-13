import asyncio
from pypollinations import ImageClient, ImageGenerationRequest 
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