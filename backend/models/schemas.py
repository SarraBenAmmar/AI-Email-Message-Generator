"""
Pydantic schemas for the AI Content Generator
"""
from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

class Tone(str, Enum):
    PROFESSIONAL = "professional"
    FRIENDLY = "friendly"
    DIRECT = "direct"
    STORYTELLING = "storytelling"

class Audience(str, Enum):
    PROSPECT = "prospect"
    CLIENT = "client"
    PARTNER = "partner"
    COLD = "cold"

class Channel(str, Enum):
    EMAIL = "email"
    BLOG_POST = "blog_post"
    SOCIAL_MEDIA = "social_media"
    AD_COPY = "ad_copy"
    PRODUCT_DESCRIPTION = "product_description"
    SCRIPT = "script"
    NEWSLETTER = "newsletter"
    CONTENT_IDEAS = "content_ideas"


class GenerationRequest(BaseModel):
    prompt: str
    tone: Tone = Tone.PROFESSIONAL
    audience: Audience = Audience.PROSPECT
    sequence_length: int = 3
    channel: Channel = Channel.EMAIL

class SequenceItem(BaseModel):
    subject: str
    body: str
    step: int
    purpose: str

class GenerationResponse(BaseModel):
    sequence: List[SequenceItem]
    metadata: dict

class ExportRequest(BaseModel):
    sequence: List[SequenceItem]
    format: str