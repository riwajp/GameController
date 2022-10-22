from pynput.keyboard import Key, KeyCode, Controller, Listener
import time

keyboard = Controller()
keymap = {"joystick": {"N": Key.up,
                       "E": Key.right, "W": Key.left, "S": Key.down}}


pressed = []


def press(key):
    global pressed
    print(pressed)
    keys = [i for i in key]

    if (len(keys) == 1 and keys[0] == "C"):
        print("CCCCCCCCCCc")
        for i in pressed:
            try:
                keyboard.release(keymap["joystick"][i])
            except:
                pass
        pressed = []
    else:

        for i in pressed:

            keyboard.release(keymap["joystick"][i])

        for i in keys:

            keyboard.press(keymap["joystick"][i])
        pressed = keys
    print(key)

    # keyboard.press(key)


def press1(key):
    keyboard.press(key)


def release1(key):
    keyboard.release(key)
