"""
Configuration settings for the AI Content Generator
"""
from typing import List
from models.schemas import Tone, Audience, Channel

# OpenRouter Configuration
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_API_KEY = "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"  # Replace with your key
OPENROUTER_MODEL = "mistralai/mistral-7b-instruct"

# Available Content Types from Channel Enum
CHANNELS: List[str] = [channel.value for channel in Channel]

# Available Tones from Tone Enum
TONES: List[str] = [tone.value for tone in Tone]

# Available Audiences from Audience Enum
AUDIENCES: List[str] = [audience.value for audience in Audience]

# Export Formats
EXPORT_FORMATS: List[str] = ["csv", "txt"]