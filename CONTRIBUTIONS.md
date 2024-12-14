# Contributing to pollinations-python

Thank you for your interest in contributing to pollinations-python! This document outlines the guidelines for contributing to this project.

## Code of Conduct

Please note that this project follows a Code of Conduct. By participating, you are expected to uphold this code.

## How to Contribute

1. **Fork the Repository**
    - Fork the repository on GitHub
    - Clone your fork locally

2. **Create a Branch**
    - Create a branch for your changes
    - Use descriptive branch names (e.g., `feature/new-model-support`, `fix/image-generation-bug`)

3. **Make Your Changes**
    - Follow the existing code style
    - Add tests for new functionality
    - Update documentation as needed

4. **Test Your Changes**
    - Run the existing test suite
    - Add new tests for your changes
    - Ensure all tests pass

5. **Commit Your Changes**
    - Write clear, concise commit messages
    - Reference any relevant issues

6. **Submit a Pull Request**
    - Push your changes to your fork
    - Open a pull request against the main repository
    - Describe your changes in detail
    - Link any related issues

## Development Setup

1. Install dependencies:
```bash
poetry install
```

2. Run tests:
```bash
poetry run pytest
```

3. Format code:
```bash
poetry run black .
```

## Pull Request Guidelines

- Include tests for new functionality
- Update documentation for API changes
- Follow the existing code style
- Keep changes focused and atomic
- Add entries to CHANGELOG.md

## License

By contributing, you agree that your contributions will be licensed under the Apache License 2.0.
