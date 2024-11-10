from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import HTTPException
import os

# Replace with your actual MongoDB connection string
MONGODB_URL = "mongodb://localhost:27017"  # Update this to your MongoDB URL
DATABASE_NAME = "mydatabase"

client = AsyncIOMotorClient(MONGODB_URL)
db = client[DATABASE_NAME]

# Example: Accessing a collection
admin_collection = db["admin"]
client_collection = db["client"]

async def get_db_status():
    try:
        # Test if the database is connected
        await client.server_info()
        return "MongoDB connected successfully"
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection error: {str(e)}")
