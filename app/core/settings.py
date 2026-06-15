from dotenv import load_dotenv 
import os

load_dotenv()

class Settings:
    GEMINI_API_KEY: str = os.getenv('GEMINI_API_KEY')
    GEMINI_MODEL: str = os.getenv('GEMINI_MODEL', 'gemini-2.5-flash')

settings = Settings()