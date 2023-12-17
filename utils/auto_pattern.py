import random
import time

import keyboard


def seeking(time_beetween_press: float, key_auto_move: list[str]):
    random_number = random.randint(0, 1)
    if random_number == 0:
        keyboard.press(key_auto_move[0])
    elif random_number == 1:
        keyboard.press(key_auto_move[1])
    time.sleep(time_beetween_press)
    keyboard.release(key_auto_move[0])
    keyboard.release(key_auto_move[1])
