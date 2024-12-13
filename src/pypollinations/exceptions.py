class PollinationsError(Exception):
    """Base exception for all Pollinations errors"""
    pass

class ValidationError(PollinationsError):
    """Raised when request validation fails"""
    pass

class APIError(PollinationsError):
    """Raised when API returns an error"""
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        super().__init__(f"{status_code}: {message}")