# config/settings.py

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ==========================
# Application Settings
# ==========================

APP_NAME = os.getenv("APP_NAME", "Personal Finance Coach")
DEBUG = os.getenv("DEBUG", "True").lower() == "true"

# ==========================
# Groq Configuration
# ==========================

# Groq Configuration

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

MODEL_NAME = "meta-llama/llama-4-scout-17b-16e-instruct"

# ==========================
# Database
# ==========================

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///finance.db"
)

# ==========================
# Redis
# ==========================

REDIS_HOST = os.getenv(
    "REDIS_HOST",
    "localhost"
)

REDIS_PORT = int(
    os.getenv("REDIS_PORT", 6379)
)

# ==========================
# Validation
# ==========================

if not GROQ_API_KEY:
    raise ValueError(
        "❌ GROQ_API_KEY is missing. Please add it to your .env file."
    )

print(f"✅ {APP_NAME} Configuration Loaded")
print(f"🤖 Model : {MODEL_NAME}")
print(f"🗄 Database : {DATABASE_URL}")