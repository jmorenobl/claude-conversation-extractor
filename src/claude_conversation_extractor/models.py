"""Data models for Claude conversation extraction."""

from datetime import datetime
from typing import List, Optional
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
    citations: List[Citation] = Field(default_factory=list)


class ChatMessage(BaseModel):
    """Individual chat message."""
    uuid: str
    text: str
    content: List[Content]
    sender: str  # "human" or "assistant"
    created_at: datetime
    updated_at: datetime
    attachments: List[str] = Field(default_factory=list)
    files: List[str] = Field(default_factory=list)


class Conversation(BaseModel):
    """Complete conversation with messages."""
    uuid: str
    name: str
    created_at: datetime
    updated_at: datetime
    account: Account
    chat_messages: List[ChatMessage] = Field(default_factory=list)


class ClaudeExport(RootModel[List[Conversation]]):
    """Root structure of Claude export file."""
    
    @property
    def conversations(self) -> List[Conversation]:
        """Get the list of conversations."""
        return self.root
