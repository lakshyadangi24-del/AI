"""
LAXIS AI Configuration
"""

from dataclasses import dataclass


@dataclass
class Config:
    APP_NAME = "LAXIS AI"
    VERSION = "7.0"

    # Ollama
    MODEL = "llama3.1:8b"

    # Database
    DATABASE = "memory.db"

    # Whisper
    WHISPER_MODEL = "base"

    # Camera
    CAMERA_INDEX = 0

    # GUI
    THEME = "dark"

    # Voice
    SPEECH_RATE = 170
    SPEECH_VOLUME = 1.0


config = Config()