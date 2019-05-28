from pynput import keyboard

class Keys:
    def __init__(self, manager):
        self.keys = ""
        self.manager = manager

    def on_release(self, key):
        # se for uma tecla alfanumerica
        if(isinstance(key, keyboard.KeyCode) and key.char is not None and
          (key.char >= 'a' and key.char <= 'z' or
           key.char >= 'A' and key.char <= 'Z' or
           key.char >= '0' and key.char <= '9')
        ):
            self.keys += key.char
        # se for a tecla ESC
        elif key == keyboard.Key.esc:
            print("encerrando listener")
            return False # Stop listener
        # gambiarra: tecla numerica 5 nao reconhece se nao colocar o codigo dela
        elif(isinstance(key, keyboard.KeyCode) and key.vk == 65437):
            self.keys += "5"
        # se nao for nenhuma das anteriores, limpa o buffer
        else:
            # se for ENTER, faça uma ação
            if key == keyboard.Key.enter:
                self.manager.allowAccessByPassword(self.keys)
            else: print("temp")
            self.keys = ""
