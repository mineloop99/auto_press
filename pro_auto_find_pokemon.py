import sys
from threading import Thread
import keyboard
import mouse
import tkinter as tk
import tkinter.messagebox as msgbox
from playsound import playsound

from utils.auto_pattern import seeking
from utils.get_active_window import get_active_window
from utils.detect_image import detect_text
from utils.config import get_list_pokemon, resource


class Auto:
    _is_running = False

    def toggle_running(self):
        self._is_running = not self._is_running

    def set_running(self, value: bool):
        self._is_running = value


POKEMON_WINDOW_NAME = "PROClient"
list_pokemon = get_list_pokemon()

auto = Auto()

time_beetween_press = 0.1  # in second
catch_time_beetween_press = (
    0.3  # in second, at least 0.3 or it will be consume CPU to 100%
)

key_quit_program = "q"
key_start = "`"
key_start_with_run_away = "-"
key_catch_start = "F12"
key_stop = "="  # Must diff key start
key_auto_move = ["a", "d"]  # Just two key only


def show_message_pop_up(message="", timeout=500):
    root = tk.Tk()
    root.withdraw()
    root.after(timeout, root.destroy)
    msgbox.showinfo("Info", message, master=root)


def stop(stop_msg="Stopped!"):
    global auto
    print("Auto " + stop_msg)
    show_message_pop_up(stop_msg)
    auto.set_running(False)


# Target window == "" its mean all window and pass
def before_auto_check(target_window_name: str):
    if target_window_name == "":
        return True
    if target_window_name in get_active_window():
        return True
    return False


def auto_with_run():
    global auto
    if auto._is_running:
        return
    auto.toggle_running()
    print("With Run")
    show_message_pop_up("With Run Started")
    while auto._is_running:
        if keyboard.is_pressed(key_stop):
            stop("Auto With Run")
            return
        if not before_auto_check(POKEMON_WINDOW_NAME):
            continue
        keyboard.press_and_release("4")
        seeking(time_beetween_press, key_auto_move)


def on_auto_press_no_run():
    global auto
    if auto._is_running:
        return
    auto.toggle_running()
    print("With No Run")
    show_message_pop_up("With No Run Started!")
    while auto._is_running:
        if keyboard.is_pressed(key_stop):
            stop("Auto With No Run Stopped!")
            return
        if not before_auto_check(POKEMON_WINDOW_NAME):
            continue
        seeking(time_beetween_press, key_auto_move)


def catch_callback():
    global auto
    auto.set_running(False)
    try:
        playsound(resource("..\\assets\\sound\\catched_sound.mp3"))
    except:
        pass
    finally:
        show_message_pop_up("Catched! ", 10000000)


def auto_catch():
    global auto
    if auto._is_running:
        return
    auto.toggle_running()
    print("Catch Started!")
    show_message_pop_up("Catch Started!")
    while auto._is_running:
        if keyboard.is_pressed(key_stop):
            stop("Auto Catch Stopped!")
            return
        if not before_auto_check(POKEMON_WINDOW_NAME):
            continue
        thread_auto = Thread(
            target=detect_text, args=[list_pokemon, "4", catch_callback]
        )
        thread_auto.daemon = True
        thread_auto.start()
        seeking(catch_time_beetween_press, key_auto_move)


def on_auto_press_with_run():
    auto_with_run()


def on_auto_mouse_press_with_run():
    thread_auto = Thread(target=auto_with_run)
    thread_auto.daemon = True
    thread_auto.start()


def exit_program():
    show_message_pop_up("exit")
    sys.exit(0)


def main():
    keyboard.add_hotkey(key_start, on_auto_press_no_run)
    keyboard.add_hotkey(key_start_with_run_away, on_auto_press_with_run)
    keyboard.add_hotkey(key_catch_start, auto_catch)
    keyboard.add_hotkey(key_quit_program, exit_program)
    mouse.on_button(on_auto_mouse_press_with_run, (), mouse.X2, mouse.UP)

    thread_mouse = Thread(target=mouse.wait)
    print("Mouse listen is starting!")
    thread_mouse.daemon = True
    thread_mouse.start()
    print("Keyboard listen is starting!")
    keyboard.wait()


main()
