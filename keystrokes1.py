import pydirectinput
import time
from pynput.keyboard import Key, KeyCode, Controller, Listener


keyboard = pydirectinput
keyboard.PAUSE = 0

keymap = {"joystick": {"N": "up",
                       "E": "right", "W": "left", "S": "down"}}

keyboard1 = Controller()
pressed = []


def press(key):
    global pressed
    print(pressed)
    keys = [i for i in key]

    if (len(keys) == 1 and keys[0] == "C"):
        print("CCCCCCCCCCc")
        for i in pressed:
            try:
                keyboard.keyUp(keymap["joystick"][i])
            except:
                pass
        pressed = []
    else:

        for i in pressed:

            keyboard.keyUp(keymap["joystick"][i])

        for i in keys:

            keyboard.keyDown(keymap["joystick"][i])
        pressed = keys
    print(key)

    # keyboard.press(key)


pressed = []


def pressKey(key):
    keyboard.keyDown(key.lower())
    if not (key.lower() in pressed):
        pressed.append(key.lower())

    print(key)


def releaseKey(key):
    if key.lower() in pressed:
        pressed.remove(key.lower())
        keyboard.keyUp(key.lower())
    else:
        pressKey(key)

        releaseKey(key)
