# bot/config/config.py
import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).parent / 'tokens.env'
load_dotenv(env_path)

TELEGRAM_TOKEN_BOT = os.getenv('TELEGRAM_TOKEN_BOT')
ACCESS_URL = os.getenv('ACCESS_URL')

SUBGRAM_MAIN_API = os.getenv('SUBGRAM_MAIN_API')
SUBGRAM_SECRET_KEY = os.getenv('SUBGRAM_SECRET_KEY')