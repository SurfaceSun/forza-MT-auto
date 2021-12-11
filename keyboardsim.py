import time
import ctypes
import win32api
import win32con
from argsolver import args
keycooldown = 0.001+args.keydelay
LEFT = 37
UP = 38
RIGHT = 39
DOWN = 40
ENTER = 13

LEFT = 65
DOWN = 83
UP = 87
RIGHT = 68
keybind = {
    "up": UP,
    "left": LEFT,
    "down": DOWN,
    "right": RIGHT,
    'enter': ENTER,
    "esc": 27,
    'tab':9,
    'q':81,
    'e':69,
    'i':73
}


def press(key, cooldown=keycooldown):
    MapKey = ctypes.windll.user32.MapVirtualKeyA
    win32api.keybd_event(key, MapKey(key, 0), 0, 0)
    time.sleep(cooldown)
    win32api.keybd_event(key, MapKey(key, 0), win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(cooldown)

def pressdown_str(keystr,cooldown=keycooldown):
    key=keybind[keystr]
    MapKey = ctypes.windll.user32.MapVirtualKeyA
    win32api.keybd_event(key, MapKey(key, 0), 0, 0)
    time.sleep(cooldown)
def pressup_str(keystr,cooldown=keycooldown):
    key=keybind[keystr]
    MapKey = ctypes.windll.user32.MapVirtualKeyA
    win32api.keybd_event(key, MapKey(key, 0), win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(cooldown)


def press_str(keystr,**kwargs):
    press(keybind[keystr],**kwargs)


if __name__ == "__main__":
    pass
    # time.sleep(1)
    # press(72)
    # import pyautogui
    #
    # pyautogui.moveTo(x=100, y=100, duration=2, tween=pyautogui.linear)
    # pyautogui.press('esc')
