from pynput import keyboard
from dotenv import dotenv_values

config = dotenv_values(".env")

WARNING_IMAGE_PATH = "images/Warning.png"
KEY_COMBO = {keyboard.Key.ctrl, keyboard.KeyCode.from_char('k')}  # Example combo: CTRL + K
MESSAGE_BODY = "Someone has been trying to access your computer."
MESSAGE_TITLE = "WARNING!"

PUSHOVER_TOKEN = config["PUSHOVER_TOKEN"]
PUSHOVER_USER = config["PUSHOVER_USER"]
PUSHOVER_DEVICE = config["PUSHOVER_DEVICE"]