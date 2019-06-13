from pynput import keyboard

class Keys:
    def __init__(self, dao, interface):
        self.keys = ""
        self.dao = dao
        self.interface = interface
        self.quit = False
        print("Keyboard listener initialized, press 'ESC' to quit program")

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
            self.quit = True
            print("quitting program...")
            return False # Stop listener
        # gambiarra: tecla numerica 5 nao reconhece se nao colocar o codigo dela
        elif(isinstance(key, keyboard.KeyCode) and key.vk == 65437):
            self.keys += "5"
        # se nao for nenhuma das anteriores, limpa o buffer
        else:
            # se for ENTER, faça uma ação
            if key == keyboard.Key.enter:
                if self.dao.allowAccessByPassword(self.keys):
                    print("Authorized access")
                    self.interface.acessoAutorizado(1)
                else:
                    print("Unauthorized access")
                    self.interface.acessoDesautorizado(1)
            self.keys = ""
