from pynput import keyboard
from dotenv import load_dotenv
from pathlib import Path
import os

ROOT_DIR = Path(__file__).resolve(strict=True).parent

load_dotenv(ROOT_DIR / ".env")

WARNING_IMAGE_PATH = ROOT_DIR / "images/Warning.png"
KEY_COMBO = {keyboard.Key.ctrl, keyboard.KeyCode.from_char('k')}  # Example combo: CTRL + K
MESSAGE_BODY = "Someone has been trying to access your computer."
MESSAGE_TITLE = "WARNING!"
WARNING_COUNT = 5

PUSHOVER_TOKEN = os.getenv("PUSHOVER_TOKEN", None)
PUSHOVER_USER = os.getenv("PUSHOVER_USER", None)
PUSHOVER_DEVICE = os.getenv("PUSHOVER_DEVICE", None)