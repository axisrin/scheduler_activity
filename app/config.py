import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
TZ = os.getenv("TZ")
DB_PATH = os.getenv("DB_PATH")
REDIS_URL = os.getenv("REDIS_URL")