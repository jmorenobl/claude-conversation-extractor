# Claude Chat Extractor

Fast, memory-efficient CLI to extract specific conversations from Claude export JSON files and convert them to clean Markdown.

> **Note:** Before using this tool, you must first export your conversations from Claude. Download your Claude conversation export as a JSON file from the Claude web interface, then use this tool to process it.

## Highlights

- UUID-based extraction and conversation discovery
- Streaming JSON parsing for constant memory usage
- Clean Markdown output with metadata and message formatting
- Friendly CLI with rich terminal output

## Quick start

```bash
# Install
pip install claude-chat-extractor

# List first 10 conversations
cce list-conversations -i path/to/conversations.json

# Extract by UUID to Markdown
cce extract -u <uuid> -i path/to/conversations.json -o <uuid>.md
```

## What next?

- Installation: see detailed steps in Installation
- Usage: examples and CLI reference
- API: browse the Python API docs generated from the source
- Development: requirements, implementation notes, distribution guides

