from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://admin:password@mongodb:27017/?authSource=admin"
DB_NAME = "pardong"

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
        if Database.db is None:
            raise RuntimeError("Database connection is not initialized. Call `Database.connect()` first.")
        return Database.db[collection_name]
