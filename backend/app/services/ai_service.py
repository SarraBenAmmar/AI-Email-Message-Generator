"""
AI Service for generating content using OpenRouter API
"""
from ssl import Purpose
import requests
import asyncio
from concurrent.futures import ThreadPoolExecutor
from config import OPENROUTER_API_URL, OPENROUTER_API_KEY, OPENROUTER_MODEL
from models.schemas import Channel, Tone, Audience

class AIService:
    def __init__(self):
        self.api_url = OPENROUTER_API_URL
        self.headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }
        self.executor = ThreadPoolExecutor(max_workers=3)
        print(f"🤖 Using model: {OPENROUTER_MODEL}")
        print(f"🌐 OpenRouter URL: {self.api_url}")

    async def generate_with_ai(self, prompt: str, channel: Channel, tone: Tone, audience: Audience, purpose: str):
        """Generate content using OpenRouter API for any channel"""
        try:
            # Create channel-specific instructions
            channel_instructions = self._get_channel_instructions(channel)
            
            messages = [
                {"role": "system", "content": f"You are a helpful AI content writer specializing in {channel.value}."},
                {"role": "user", "content": f"Create {channel.value} content with a {tone.value} tone for {audience.value} audience. Purpose: '{purpose}'. Topic: '{prompt}'. {channel_instructions}"}
            ]
            
            payload = {
                "model": OPENROUTER_MODEL,
                "messages": messages,
                "max_tokens": 600 if channel == Channel.SCRIPT else 400,
                "temperature": 0.7
            }

            loop = asyncio.get_event_loop()
            response = await loop.run_in_executor(
                self.executor,
                lambda: requests.post(self.api_url, headers=self.headers, json=payload, timeout=60)
            )

            print(f"📡 OpenRouter status: {response.status_code}")

            if response.status_code == 200:
                result = response.json()
                text = result["choices"][0]["message"]["content"]
                print(f"✅ Generated {channel.value}: {text[:80]}...")
                subject, body = self.extract_subject_body(text, channel)
                return subject, body
            else:
                print("❌ OpenRouter Error:", response.text)
                return None, None

        except Exception as e:
            print("💥 AI error:", e)
            return None, None

    def _get_channel_instructions(self, channel: Channel):
        """Get specific instructions for different channels"""
        instructions = {
            Channel.EMAIL: "Create a professional email with clear subject line and body.",
            Channel.LINKEDIN: "Create professional LinkedIn content with relevant industry hashtags.",
            Channel.SCRIPT: "Create a conversational script that can be used for video or audio content."
        }
        return instructions.get(channel, "Create engaging and relevant content.")

    def extract_subject_body(self, text: str, channel: Channel):
        """Extract subject and body from generated text based on channel"""
        if channel == Channel.EMAIL:
            if "Subject:" in text:
                parts = text.split("Subject:", 1)[1]
                lines = parts.strip().split("\n", 1)
                subject = lines[0].strip()
                body = lines[1].strip() if len(lines) > 1 else ""
            else:
                subject = f"Email about topic"
                body = text.strip()
        elif channel == Channel.LINKEDIN:
            # For LinkedIn, use first line as subject or generate one
            lines = text.strip().split('\n')
            subject = lines[0].strip() if lines else f"LinkedIn post about topic"
            body = text.strip()
        elif channel == Channel.SCRIPT:
            # For scripts, generate appropriate subject
            subject = f"Script: {Purpose}"
            body = text.strip()
        else:
            subject = f"{channel.value.title()} content"
            body = text.strip()
        
        return subject, body