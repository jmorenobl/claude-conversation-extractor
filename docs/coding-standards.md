# Python Coding Standards

## 🚨 **Version Management (CRITICAL)**
- **Version-Tag Alignment**: NEVER create Git tags without updating project version in `pyproject.toml`
- **Pre-release Checklist**: Always follow the complete workflow: Update Code → Build → Commit → Tag → Push
- **Version Consistency**: Ensure `pyproject.toml` version matches Git tag version exactly
- **See**: [Version Management Guide](version-management.md) for complete workflow

## Type Safety & Annotations
- **Always use type hints**: Every function parameter and return value must have type annotations
- **Use Pydantic models**: For data validation and serialization, use the models in [models.py](src/claude_conversation_extractor/models.py)
- **Strict MyPy settings**: Follow the configuration in [pyproject.toml](pyproject.toml) with strict type checking

## Code Style & Formatting
- **Ruff formatting**: Use Ruff for consistent code formatting (configured in [pyproject.toml](pyproject.toml))
- **Line length**: Maximum 88 characters per line
- **Quotes**: Use double quotes for strings
- **Imports**: Use absolute imports from the package root

## Error Handling
- **Comprehensive exception handling**: Always catch specific exceptions, never use bare `except:`
- **User-friendly error messages**: Provide clear, actionable error descriptions
- **Graceful degradation**: Handle errors gracefully when possible
- **Logging**: Use structured logging for debugging and monitoring

## Function Design
- **Single responsibility**: Each function should do one thing well
- **Descriptive names**: Use clear, descriptive names that communicate intent
- **Documentation**: Add docstrings explaining the "why" not just the "what"
- **Default values**: Use `Field(default_factory=list)` for mutable defaults

## Memory Efficiency
- **Streaming processing**: Use generators and iterators for large data processing
- **Avoid loading entire files**: Use `ijson` for streaming JSON parsing as shown in [extractor.py](src/claude_conversation_extractor/extractor.py)
- **Constant memory usage**: Design for predictable memory consumption regardless of input size

## Release & Deployment
- **Version bumping**: Follow semantic versioning (MAJOR.MINOR.PATCH)
- **Release notes**: Document all changes in commit messages and release notes
- **Testing**: Always test package builds before creating tags
- **CI/CD**: Ensure all automated checks pass before deployment

---

**Remember**: Version management is critical for successful releases. Always check [version-management.md](version-management.md) before creating tags!
