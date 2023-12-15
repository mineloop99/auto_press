import sys
from threading import Thread
import keyboard
import mouse
import time
import random
import tkinter as tk
import tkinter.messagebox as msgbox

from const import AUTO_STARTED_LOG, AUTO_STOPPED_LOG, STARTED_LOG, STOPPED_LOG


class Auto:
    _is_running = False

    def toggle_running(self):
        self._is_running = not self._is_running


auto = Auto()
key_quit_program = "q"
key_start = "`"
key_start_with_run_away = "-"
key_stop = "="  # Must diff key start
time_beetween_press = 0.1  # in second
key_auto_move = ["a", "d"]  # Just two key only


def show_message_pop_up(message, timeout=500):
    root = tk.Tk()
    root.withdraw()
    root.after(timeout, root.destroy)
    msgbox.showinfo("Info", message, master=root)


def stop():
    global auto
    print(AUTO_STOPPED_LOG)
    show_message_pop_up(STOPPED_LOG)
    auto.toggle_running()


def auto_with_run():
    global auto
    if auto._is_running:
        return
    auto.toggle_running()
    print(AUTO_STARTED_LOG)
    show_message_pop_up(STARTED_LOG)
    while auto._is_running:
        if keyboard.is_pressed(key_stop):
            stop()
            return
        random_number = random.randint(0, 1)
        keyboard.press("4")
        keyboard.release("4")
        if random_number == 0:
            keyboard.press(key_auto_move[0])
        elif random_number == 1:
            keyboard.press(key_auto_move[1])
        time.sleep(time_beetween_press)
        keyboard.release(key_auto_move[0])
        keyboard.release(key_auto_move[1])


def on_auto_press_no_run():
    global auto
    if auto._is_running:
        return
    auto.toggle_running()
    print(AUTO_STARTED_LOG)
    show_message_pop_up(STARTED_LOG)
    while auto._is_running:
        if keyboard.is_pressed(key_stop):
            stop()
            return
        random_number = random.randint(0, 1)
        if random_number == 0:
            keyboard.press(key_auto_move[0])
        elif random_number == 1:
            keyboard.press(key_auto_move[1])
        time.sleep(time_beetween_press)
        keyboard.release(key_auto_move[0])
        keyboard.release(key_auto_move[1])


def on_auto_press_with_run():
    auto_with_run()


def on_auto_mouse_press_with_run():
    thread_auto = Thread(target=auto_with_run)
    thread_auto.daemon = True
    thread_auto.start()


def exit_program():
    show_message_pop_up("exit")
    sys.exit(0)


keyboard.add_hotkey(key_start, on_auto_press_no_run)
keyboard.add_hotkey(key_start_with_run_away, on_auto_press_with_run)
keyboard.add_hotkey(key_quit_program, exit_program)
mouse.on_button(on_auto_mouse_press_with_run, (), mouse.X2, mouse.UP)

thread_mouse = Thread(target=mouse.wait)
print("Mouse listen is starting!")
thread_mouse.daemon = True
thread_mouse.start()
print("Keyboard listen is starting!")
keyboard.wait()
