"""Data models for Claude conversation extraction."""

from datetime import datetime

from pydantic import BaseModel, Field, RootModel


class Account(BaseModel):
    """Account information."""

    uuid: str


class Citation(BaseModel):
    """Citation information."""

    # Add citation fields as needed based on the actual data structure
    pass


class Content(BaseModel):
    """Message content with timestamps."""

    start_timestamp: datetime
    stop_timestamp: datetime
    type: str
    text: str
    citations: list[Citation] = Field(default_factory=list)


class ChatMessage(BaseModel):
    """Individual chat message."""

    uuid: str
    text: str
    content: list[Content]
    sender: str  # "human" or "assistant"
    created_at: datetime
    updated_at: datetime
    attachments: list[str] = Field(default_factory=list)
    files: list[str] = Field(default_factory=list)


class Conversation(BaseModel):
    """Complete conversation with messages."""

    uuid: str
    name: str
    created_at: datetime
    updated_at: datetime
    account: Account
    chat_messages: list[ChatMessage] = Field(default_factory=list)


class ClaudeExport(RootModel[list[Conversation]]):
    """Root structure of Claude export file."""

    @property
    def conversations(self) -> list[Conversation]:
        """Get the list of conversations."""
        return self.root
