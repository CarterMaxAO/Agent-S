import pyautogui
from pynput import mouse
import datetime
import os

def on_click(x, y, button, pressed):
    if pressed:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot = pyautogui.screenshot()
        os.makedirs("screenshots", exist_ok=True)
        filename = f"screenshots/click_{timestamp}_{x}_{y}.png"
        screenshot.save(filename)
        print(f"Screenshot saved: {filename}")

if __name__ == "__main__":
    print("Listening for mouse clicks. Press Ctrl+C to exit.")
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()
