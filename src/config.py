import os
from dotenv.main import load_dotenv

load_dotenv()


TOKEN = os.getenv("TOKEN")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
