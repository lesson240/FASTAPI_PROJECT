from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
from app.config import MONGO_DB_NAME, MONGO_DB_URL


class MongoDB:

    def __init__(self):
        self.client = None
        self.engine = None

    def connect(self):
        self.client = AsyncIOMotorClient(MONGO_DB_URL)
        self.engine = AIOEngine(client=self.client, database=MONGO_DB_NAME)
        print("DB와 성공적으로 연결되었습니다.")

    def close(self):
        self.client.close()
        print("DB와 성공적으로 연결을 끊었습니다")


mongodb = MongoDB()
