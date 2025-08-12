# Claude Conversation Extractor

A powerful command-line tool to extract specific conversations from Claude export files and convert them to readable markdown format.

## Features

- 🎯 **UUID-based Extraction**: Find and extract conversations by their unique identifier
- 📝 **Markdown Conversion**: Convert conversations to clean, readable markdown
- 🔍 **Conversation Discovery**: List available conversations in export files
- 🚀 **High Performance**: Efficiently handle large export files
- 🎨 **Rich CLI**: Beautiful terminal interface with progress indicators
- 🛡️ **Error Handling**: Graceful error handling and validation

## Quick Start

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd claude-conversation-extractor

# Install dependencies
uv sync
```

### Basic Usage

```bash
# List available conversations
claude-extract list -i data/conversations.json

# Extract a specific conversation
claude-extract extract \
  -u 28d595a3-5db0-492d-a49a-af74f13de505 \
  -i data/conversations.json \
  -o my_conversation.md
```

## Available Commands

The tool can be invoked using any of these names:
- `claude-extract` (recommended)
- `cce` (shortest)
- `claude-conversation-extractor` (full name)

### Extract Command
Extract a conversation by UUID and convert to markdown:
```bash
claude-extract extract -u <uuid> -i <input.json> -o <output.md>
# or
cce extract -u <uuid> -i <input.json> -o <output.md>
```

### List Command
List available conversations in an export file:
```bash
claude-extract list -i <input.json> -l 10
# or
cce list -i <input.json> -l 10
```

## Input Format

The tool expects a JSON file with Claude export data containing:
- Conversation metadata (UUID, name, timestamps)
- Chat messages with sender information
- Content with timestamps and citations
- File attachments and references

## Output Format

Generated markdown includes:
- Conversation header with metadata
- Chronological message flow
- Clear sender identification (Human/Claude)
- Timestamps and formatting
- Attachment information

## Development

### Project Structure
```
claude-conversation-extractor/
├── src/claude_conversation_extractor/
│   ├── __init__.py
│   ├── models.py          # Data models
│   ├── extractor.py       # Core extraction logic
│   ├── markdown_converter.py # Markdown formatting
│   └── cli.py            # Command-line interface
├── tests/                 # Test suite
├── docs/                  # Documentation
└── pyproject.toml        # Project configuration
```

### Running Tests
```bash
uv run pytest
```

### Development Setup
```bash
# Install in development mode
uv sync --dev

# Run the tool
uv run claude-extract --help
```

## Requirements

- Python 3.12+
- UV package manager
- Claude export JSON file

## Dependencies

- **Click**: Command-line interface framework
- **Pydantic**: Data validation and serialization
- **Rich**: Enhanced terminal output
- **Pytest**: Testing framework

## Documentation

- [Requirements](docs/requirements.md) - Detailed project requirements
- [Usage Guide](docs/usage.md) - Comprehensive usage instructions

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## License

[Add your license information here]

## Support

For issues and questions, please open an issue on GitHub.
