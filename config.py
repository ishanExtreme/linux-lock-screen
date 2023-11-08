from pynput import keyboard
from dotenv import load_dotenv
from pathlib import Path
import os

ROOT_DIR = Path(__file__).resolve(strict=True).parent

load_dotenv(ROOT_DIR / ".env")

WARNING_IMAGE_PATH = ROOT_DIR / "images/Warning.png" # Image to display when , change to your liking
KEY_COMBO = {keyboard.Key.ctrl, keyboard.KeyCode.from_char('k')}  # Example combo: CTRL + K, change to your liking
MESSAGE_BODY = "Someone has been trying to access your computer." # Pushnotification message, change to your liking
MESSAGE_TITLE = "WARNING!" # Pushnotification title, change to your liking
WARNING_COUNT = 5 # How many times the warning image should be displayed before sending a push notification, change to your liking

PUSHOVER_TOKEN = os.getenv("PUSHOVER_TOKEN", None)
PUSHOVER_USER = os.getenv("PUSHOVER_USER", None)
PUSHOVER_DEVICE = os.getenv("PUSHOVER_DEVICE", None)