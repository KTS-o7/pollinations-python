from typing import Optional, Any
import httpx
from ..exceptions import PollinationsError, APIError


class BaseClient:
    """
    Base class for Pollinations API clients.

    Attributes:
    - api_base: The base URL of the API.
    - client: An httpx.AsyncClient instance.

    Methods:
    - close: Close the client.
    - _request: Make an HTTP request to the API.
    - __aenter__: Enter an async context.
    - __aexit__: Exit an async context.
    - __init__: Initialize the client.
    """

    def __init__(self, api_base: str, timeout: int = 30):
        self.api_base = api_base
        self.client = httpx.AsyncClient(timeout=timeout)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    async def close(self):
        await self.client.aclose()

    async def _request(
        self,
        method: str,
        path: str,
        params: Optional[dict[str, Any]] = None,
        json: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> Any:
        try:
            response = await self.client.request(
                method=method,
                url=f"{self.api_base}{path}",
                params=params,
                json=json,
                headers=headers,
            )
            response.raise_for_status()
            return response

        except httpx.HTTPStatusError as e:
            raise APIError(e.response.status_code, str(e))

        except httpx.HTTPError as e:
            raise PollinationsError(f"HTTP error: {str(e)}")
