import keyboard
import time
import random

on_running = False

key_start = "-"
key_stop = "="  # Must diff key start

time_beetween_press = 0.1  # in second

key_auto_move = ["a", "d"]  # Just two key only
key_to_run = "]"  # Just one


def on_auto_press():
    global on_running
    if on_running:
        return
    else:
        on_running = True
    print("Auto started!")
    while on_running:
        if keyboard.is_pressed(key_stop):
            print("Auto stopped!")
            on_running = False
            return
        random_number = random.randint(0, 1)
        if random_number == 0:
            keyboard.press(key_auto_move[0])
        elif random_number == 1:
            keyboard.press(key_auto_move[1])
        time.sleep(time_beetween_press)
        keyboard.release(key_auto_move[0])
        keyboard.release(key_auto_move[1])


def on_auto_run_press():
    keyboard.press(key_to_run)
    keyboard.release(key_to_run)


keyboard.add_hotkey(key_start, on_auto_press)

keyboard.add_hotkey(key_to_run, on_auto_run_press)
keyboard.wait()
