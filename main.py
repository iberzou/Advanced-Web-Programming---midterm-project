"""
FastAPI Backend for SpeechPro Equipment Store
This REST API provides a welcome endpoint that can be called from the frontend
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
from typing import Dict

# Create FastAPI instance
app = FastAPI(
    title="SpeechPro API",
    description="REST API for Speech Pathology Equipment Store",
    version="1.0.0"
)

# Configure CORS to allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Response model
class WelcomeResponse(BaseModel):
    message: str
    timestamp: str
    status: str

class ProductResponse(BaseModel):
    products: list
    total: int

# Root endpoint
@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to SpeechPro API",
        "version": "1.0.0",
        "endpoints": [
            "/api/welcome",
            "/api/products",
            "/docs"
        ]
    }

# Welcome endpoint - called from the frontend
@app.get("/api/welcome", response_model=WelcomeResponse)
async def get_welcome() -> Dict:
    """
    Welcome endpoint that returns a greeting message
    This endpoint is called from the AngularJS frontend
    """
    return {
        "message": "🎉 Welcome to SpeechPro! Your trusted source for professional speech pathology equipment. We're delighted to serve you!",
        "timestamp": datetime.now().isoformat(),
        "status": "success"
    }

# Additional endpoint - Get products
@app.get("/api/products", response_model=ProductResponse)
async def get_products() -> Dict:
    """
    Get list of available products
    """
    products = [
        {
            "id": 1,
            "name": "Professional Laryngoscope Kit",
            "price": 549.99,
            "category": "Diagnostic Tools",
            "in_stock": True
        },
        {
            "id": 2,
            "name": "Articulation Cards Set",
            "price": 89.99,
            "category": "Therapy Materials",
            "in_stock": True
        },
        {
            "id": 3,
            "name": "Voice Amplifier System",
            "price": 299.99,
            "category": "Audio Equipment",
            "in_stock": True
        },
        {
            "id": 4,
            "name": "Oral Motor Therapy Kit",
            "price": 129.99,
            "category": "Therapy Tools",
            "in_stock": True
        },
        {
            "id": 5,
            "name": "Fluency Master Device",
            "price": 799.99,
            "category": "Advanced Equipment",
            "in_stock": True
        },
        {
            "id": 6,
            "name": "Therapy Mirror Stand",
            "price": 149.99,
            "category": "Clinical Furniture",
            "in_stock": True
        }
    ]
    
    return {
        "products": products,
        "total": len(products)
    }

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }

# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)