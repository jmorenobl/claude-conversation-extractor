# Coding Standards

## General

- Python 3.12+
- Follow PEP 8; enforce with Ruff (`py312` target)
- Use type hints for all public functions and classes
- Prefer clear, descriptive names

## Docstrings

- Comprehensive docstrings for public APIs
- Google style (rendered via mkdocstrings)

## Linting & Types

- Ruff for lint/format
- MyPy in strict mode

## Testing

- Pytest with focused unit tests; cover critical paths and errors
