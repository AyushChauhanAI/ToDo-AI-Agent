import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

DATABASE_URL=os.getenv("DATABASE_URL")

GROQ_API_KEY=os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

print("GROQ KEY LENGTH:", len(GROQ_API_KEY) if GROQ_API_KEY else None)