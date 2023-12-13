import sys
import keyboard
import time
import random
import tkinter as tk
import tkinter.messagebox as msgbox


def show_message_pop_up(message, timeout=500):
    root = tk.Tk()
    root.withdraw()
    root.after(timeout, root.destroy)
    msgbox.showinfo("Info", message, master=root)


key_quit_program = "q"
key_start = "-"
key_start_with_run_away = "`"
key_stop = "="  # Must diff key start

time_beetween_press = 0.1  # in second

key_auto_move = ["a", "d"]  # Just two key only


on_running = False


def on_auto_press_no_run():
    global on_running
    if on_running:
        return
    else:
        on_running = True
    print("Auto started!")
    show_message_pop_up("Started!")
    while on_running:
        if keyboard.is_pressed(key_stop):
            print("Auto stopped!")
            show_message_pop_up("stopped!")
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


def on_auto_press_with_run():
    global on_running
    if on_running:
        return
    else:
        on_running = True
    print("Auto started!")
    show_message_pop_up("Started!")
    while on_running:
        if keyboard.is_pressed(key_stop):
            print("Auto stopped!")
            show_message_pop_up("stopped!")
            on_running = False
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


def exit_program():
    sys.exit()


keyboard.add_hotkey(key_start, on_auto_press_no_run)
keyboard.add_hotkey(key_start_with_run_away, on_auto_press_with_run)
keyboard.add_hotkey(key_quit_program, exit_program)
keyboard.wait()
