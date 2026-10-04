import pyautogui


class KeyboardControl:

    def write(self, text):
        pyautogui.write(text)

    def press(self, key):
        pyautogui.press(key)

    def hotkey(self, *keys):
        pyautogui.hotkey(*keys)