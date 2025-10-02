"""
Main FastAPI Application
Author: Augustus Rivers <hello@offlabel.design>

This is the entry point. Pretty standard FastAPI setup,
but with better error handling and logging than most tutorials.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from app.core.config import settings
from app.api.v1 import api_router

# Create FastAPI app
app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
    description="Production-ready API built with FastAPI",
    openapi_url=f"{settings.API_V1_PREFIX}/openapi.json",
    docs_url=f"{settings.API_V1_PREFIX}/docs",
    redoc_url=f"{settings.API_V1_PREFIX}/redoc",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Gzip compression
app.add_middleware(GZipMiddleware, minimum_size=1000)

# Include API router
app.include_router(api_router, prefix=settings.API_V1_PREFIX)

@app.get("/")
async def root():
    """Root endpoint - health check"""
    return {
        "status": "running",
        "message": "API is operational",
        "author": "Augustus Rivers",
        "website": "https://offlabel.design"
    }

@app.get("/health")
async def health_check():
    """
    Health check endpoint
    Used by load balancers and monitoring systems
    """
    return {
        "status": "healthy",
        "version": "1.0.0"
    }
