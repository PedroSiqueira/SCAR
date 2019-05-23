from pynput import keyboard

class Keys:
    def __init__(self):
        self.keys = []

    def on_release(self, key):
        if(key == keyboard.KeyCode):
            print('{0} released'.format(key))
            if(key >= 'a' and key <= 'z' or key >= 'A' and key <= 'Z' or key >= '0' and key <= '9'):
                self.keys.append(key)
        elif key == keyboard.Key.esc:
            return False # Stop listener
        elif key == keyboard.Key.enter:
            print(self.keys)
        else:
            keys = []
