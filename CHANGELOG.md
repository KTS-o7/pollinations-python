# Changelog

## Version 0.2.0

### Added

- Added `TextClient` and `ImageClient` for text and image generation respectively.
- Implemented `TextGenerationRequest` and `TextGenerationResponse` models.
- Implemented `ImageGenerationRequest` and `ImageResponse` models.
- Added example scripts for image generation (`examples/image_generation.py`) and text generation (`examples/text_generation.py`).
- Added unit tests for text generation client in `tests/test_client/test_text.py`.
- Added unit tests for text generation models in `tests/test_models/test_text.py`.
- Added API documentation in `docs/api.md`.

### Changed

- Updated `README.md` with usage examples for image and text generation.

### Fixed

- Fixed various issues related to model validation in `TextGenerationRequest` and `ImageGenerationRequest`.

### Added

- Initial release with basic functionality for text and image generation.
