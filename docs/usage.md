# Usage Guide

## Installation

The tool is installed as a Python package and can be used in two ways:

### As a Command-Line Tool
```bash
# Extract a conversation
claude-extract extract --uuid <uuid> --input <file.json> --output <output.md>

# List conversations
claude-extract list --input <file.json>
```

### As a Python Module
```bash
python -m claude_conversation_extractor extract --uuid <uuid> --input <file.json> --output <output.md>
```

## Commands

### Extract Command
Extract a specific conversation by UUID and convert to markdown.

**Syntax:**
```bash
claude-conversation-extractor extract [OPTIONS]
```

**Options:**
- `--uuid, -u TEXT`: UUID of the conversation to extract (required)
- `--input, -i PATH`: Path to the Claude export JSON file (required)
- `--output, -o PATH`: Output markdown file path (optional, defaults to `<uuid>.md`)
- `--verbose, -v`: Enable verbose output
- `--help`: Show help message

**Examples:**
```bash
# Basic extraction
claude-extract extract -u 28d595a3-5db0-492d-a49a-af74f13de505 -i data/conversations.json

# With custom output path
claude-extract extract -u 28d595a3-5db0-492d-a49a-af74f13de505 -i data/conversations.json -o my_conversation.md

# Verbose mode
claude-extract extract -u 28d595a3-5db0-492d-a49a-af74f13de505 -i data/conversations.json -v
```

### List Command
List available conversations in an export file.

**Syntax:**
```bash
claude-conversation-extractor list [OPTIONS]
```

**Options:**
- `--input, -i PATH`: Path to the Claude export JSON file (required)
- `--limit, -l INTEGER`: Maximum number of conversations to list (default: 10)
- `--help`: Show help message

**Examples:**
```bash
# List first 10 conversations
claude-extract list -i data/conversations.json

# List first 5 conversations
claude-extract list -i data/conversations.json -l 5
```

## Input File Format

The tool expects a JSON file with the following structure:
```json
{
  "conversations": [
    {
      "uuid": "conversation-uuid",
      "name": "Conversation Name",
      "created_at": "2024-01-01T00:00:00Z",
      "updated_at": "2024-01-01T00:00:00Z",
      "account": {
        "uuid": "account-uuid"
      },
      "chat_messages": [
        {
          "uuid": "message-uuid",
          "text": "Message text",
          "sender": "human|assistant",
          "created_at": "2024-01-01T00:00:00Z",
          "content": [...],
          "attachments": [],
          "files": []
        }
      ]
    }
  ]
}
```

## Output Format

The tool generates markdown files with the following structure:

```markdown
# Conversation Name

## Conversation Details
- **UUID**: `conversation-uuid`
- **Created**: 2024-01-01 00:00:00 UTC
- **Updated**: 2024-01-01 00:00:00 UTC
- **Account**: `account-uuid`

## Messages

### 👤 Human - Message 1
*2024-01-01 00:00:00 UTC*

Message text content...

### 🤖 Claude - Message 2
*2024-01-01 00:00:00 UTC*

Response content...
```

## Error Handling

The tool provides clear error messages for common issues:

- **File not found**: When the input file doesn't exist
- **Invalid JSON**: When the input file isn't valid JSON
- **Conversation not found**: When the specified UUID doesn't exist
- **Validation errors**: When the JSON structure doesn't match expectations

## Verbose Mode

Enable verbose mode with `-v` flag to see:
- File loading progress
- UUID search status
- Conversion progress
- Detailed error information

## Examples

### Extract a Specific Conversation
```bash
# Find the conversation UUID first
claude-extract list -i data/conversations.json

# Extract the conversation
claude-extract extract \
  -u 28d595a3-5db0-492d-a49a-af74f13de505 \
  -i data/conversations.json \
  -o strategies_for_prompts.md
```

### Batch Processing
```bash
# Extract multiple conversations
for uuid in uuid1 uuid2 uuid3; do
  claude-extract extract -u $uuid -i data/conversations.json
done
```
