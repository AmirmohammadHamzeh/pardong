from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://admin:password@localhost:27017/")
DB_NAME = os.getenv("DB_NAME", "pardong")


class Database:
    client: AsyncIOMotorClient = None
    db = None

    @staticmethod
    async def connect():
        if Database.client is None:
            Database.client = AsyncIOMotorClient(MONGO_URI)
            Database.db = Database.client[DB_NAME]
            print("✅ MongoDB connected!")

    @staticmethod
    async def close():
        if Database.client:
            Database.client.close()
            print("❌ MongoDB connection closed.")

    @staticmethod
    def get_collection(collection_name: str):
        """دریافت کالکشن بعد از مقداردهی دیتابیس"""
        if Database.db is None:
            raise RuntimeError("Database connection is not initialized. Call `Database.connect()` first.")
        return Database.db[collection_name]
