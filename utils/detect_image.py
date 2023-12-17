import cv2
import keyboard
import pyautogui
import numpy as np
import pytesseract
from utils.config import EXECUTABLE_TESSERACT_FILE


from utils.meta import CATURE_REGION

pytesseract.pytesseract.tesseract_cmd = EXECUTABLE_TESSERACT_FILE


def get_frame():
    img = pyautogui.screenshot(region=CATURE_REGION)
    frame = np.array(img)
    return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)


def detect_text(list_target: list[str], key_run: str, callback):
    # Convert to grayscale
    frame = get_frame()
    all_text = pytesseract.image_to_string(frame).lower()
    for target in list_target:
        if target in all_text:
            callback()
            return
    keyboard.press_and_release(key_run)
