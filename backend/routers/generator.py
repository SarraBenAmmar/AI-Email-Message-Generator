"""
API routes for content generation
"""
from fastapi import APIRouter, HTTPException
import time
from models.schemas import (
    GenerationRequest, 
    GenerationResponse, 
    ExportRequest,
    Channel,
    Tone,
    Audience
)
from app.services.ai_service import AIService
from app.services.fallback_generator import FallbackGenerator
from app.services.export_service import ExportService
from config import CHANNELS, TONES, AUDIENCES

# ADD prefix back to router since we removed it from main.py
router = APIRouter(prefix="/api/v1", tags=["content-generation"])

# Initialize services
ai_service = AIService()
fallback_generator = FallbackGenerator()
export_service = ExportService()

@router.post("/generate", response_model=GenerationResponse)
async def generate_sequence(request: GenerationRequest):
    """Generate content sequence for any channel"""
    print(f"🎯 Received generate request: {request}")
    
    start_time = time.time()
    sequence = []
    
    # Define purposes based on sequence length
    purposes = ["Introduction", "Follow-up", "Value Proposition", "Call to Action", "Closing"]
    
    # Use AI service
    use_ai = True

    for i in range(request.sequence_length):
        purpose = purposes[i] if i < len(purposes) else f"Message {i+1}"
        print(f"🧠 Step {i+1}: {purpose} for {request.channel.value}")
        subject, body = None, None

        if use_ai:
            subject, body = await ai_service.generate_with_ai(
                request.prompt, 
                request.channel, 
                request.tone, 
                request.audience, 
                purpose
            )

        if not body:
            # Use fallback generator
            print("🔄 Using fallback generator...")
            fallback_sequence = await fallback_generator.generate_sequence(request)
            if i < len(fallback_sequence):
                subject = fallback_sequence[i].subject
                body = fallback_sequence[i].body

        if not body:
            # Ultimate fallback
            print("⚠️ Using ultimate fallback...")
            subject = f"{purpose}: {request.prompt}"
            body = f"This is the {purpose.lower()} for {request.channel.value} about {request.prompt}."

        sequence.append({
            "subject": subject,
            "body": body,
            "step": i + 1,
            "purpose": purpose
        })

    elapsed = time.time() - start_time
    
    print(f"✅ Generation complete! Created {len(sequence)} items in {elapsed:.2f}s")
    
    return GenerationResponse(
        sequence=sequence,
        metadata={
            "status": "success",
            "generation_time": f"{elapsed:.2f}s",
            "model": "openrouter" if use_ai else "template",
            "channel": request.channel.value,
            "tone": request.tone.value,
            "audience": request.audience.value,
            "items_generated": len(sequence)
        }
    )

@router.get("/channels")
async def get_channels():
    """Get available channels, tones, and audiences"""
    return {
        "channels": CHANNELS,
        "tones": TONES,
        "audiences": AUDIENCES
    }

@router.post("/export")
async def export_sequence(export_req: ExportRequest):
    """Export generated content sequence"""
    try:
        return await export_service.export(export_req.sequence, export_req.format)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Add a test endpoint to verify this router is working
@router.get("/test")
async def test_router():
    return {"message": "Router is working!", "router": "generator"}