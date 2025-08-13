# Claude Conversation Extractor

Fast, memory-efficient CLI to extract specific conversations from Claude export JSON files and convert them to clean Markdown.

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

