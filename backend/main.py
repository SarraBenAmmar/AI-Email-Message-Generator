"""
AI Content Generator - Main FastAPI Application
"""
import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import the router
try:
    from routers.generator import router
    print("✅ Router imported successfully")
except ImportError as e:
    print(f"❌ Router import failed: {e}")
    # Create a dummy router for testing
    from fastapi import APIRouter
    router = APIRouter()

app = FastAPI(
    title="AI Content Generator",
    description="Generate various types of content using AI (emails, LinkedIn posts, scripts, etc.)",
    version="4.0"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers - FIXED: Remove prefix from here since it's in the router
app.include_router(router)

@app.get("/")
async def root():
    return {
        "service": "AI Content Generator",
        "status": "running", 
        "version": "4.0",
        "description": "Generate emails, LinkedIn posts, and scripts with AI",
        "endpoints": {
            "generate": "POST /api/v1/generate",
            "channels": "GET /api/v1/channels",
            "export": "POST /api/v1/export",
            "health": "GET /health",
            "docs": "GET /docs"
        }
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "API is running"}

if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting AI Content Generator API...")
    print("📝 API Documentation: http://localhost:8000/docs")
    print("🔗 Available endpoints:")
    print("   - POST /api/v1/generate")
    print("   - GET  /api/v1/channels") 
    print("   - POST /api/v1/export")
    print("   - GET  /health")
    uvicorn.run(app, host="0.0.0.0", port=8000)