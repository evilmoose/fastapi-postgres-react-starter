"""
FastAPI application entry point.
""" 

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.db import test_db_connection

# Create FastAPI app
app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

# Configure CORS
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Root endpoint
@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Welcome to FastAPI PostgreSQL React Template"}

# Database connection test endpoint
@app.get("/api/v1/test-db")
async def test_db():
    """Test database connection endpoint."""
    return await test_db_connection() 
