import subprocess
from pynput import mouse, keyboard
from PIL import Image, ImageTk
import tkinter as tk
import threading

from notif import send_notification
from config import WARNING_IMAGE_PATH, KEY_COMBO, MESSAGE_BODY, MESSAGE_TITLE

xtrlock_process = None
lock_active = False
message_displaying = False
warning_count = 0


current_keys = set()

def on_press(key):
    global xtrlock_process, lock_active

    if key in KEY_COMBO:
        current_keys.add(key)

        if current_keys == KEY_COMBO:
            if lock_active:
                print("unlocking")
                # Kill xtrlock
                subprocess.Popen(["killall", "xtrlock"])
                lock_active = False
            else:
                print("locking")
                # Run xtrlock
                xtrlock_process = subprocess.Popen(["xtrlock", "-f"])
                lock_active = True
    

def on_release(key):
    if key in KEY_COMBO:
        current_keys.remove(key)
    on_keypress(key)

def display_message():
    global message_displaying, warning_count
    message_displaying = True

    display_image_with_tkinter()
        
    message_displaying = False
    if warning_count >= 5:
        send_notification(
            MESSAGE_TITLE,
            MESSAGE_BODY
        )
        warning_count = 0
    else:
        warning_count += 1


def display_image_with_tkinter():
    """Display an image using tkinter."""

    img = Image.open(WARNING_IMAGE_PATH)
    root = tk.Tk()
    root.title("WARNING!")
    
    # Get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Convert PIL image to a format tkinter can use
    tk_image = ImageTk.PhotoImage(img)

    # Get image width and height
    img_width = tk_image.width()
    img_height = tk_image.height()

    # Calculate the position coordinates to center align the image
    x = (screen_width // 2) - (img_width // 2)
    y = (screen_height // 2) - (img_height // 2)
    root.geometry('+%d+%d' % (x, y))
    
    label = tk.Label(root, image=tk_image)
    label.pack()

    # Set a timer to close the window after 1 second
    root.after(3000, root.destroy)
    
    root.mainloop()

def handle_event():
    """Handles a mouse move or keypress event."""
    global message_displaying
    if lock_active and not message_displaying:
        threading.Thread(target=display_message).start()

def on_mouse_move(x, y):
    handle_event()

def on_keypress(key):
    handle_event()

# Start listening to mouse and keyboard
with mouse.Listener(on_move=on_mouse_move) as mouse_listener, keyboard.Listener(on_press=on_press, on_release=on_release) as key_listener:
    mouse_listener.join()
    key_listener.join()
