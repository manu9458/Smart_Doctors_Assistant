import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings:
    GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY", "")
    EMBED_MODEL: str = "models/text-embedding-004"
    LLM_MODEL: str = "models/gemini-2.5-flash"
    DB_DIR: str = "chroma_db"
    CHUNK_SIZE: int = 1000
    CHUNK_OVERLAP: int = 100

    DEFAULT_TEMP: float = 0.2
    DEFAULT_TOP_K: int = 8

    def validate(self):
        if not self.GOOGLE_API_KEY:
            raise ValueError("GOOGLE_API_KEY missing in environment.")
