class Lampada:
    def __init__(self):
        self.estado = False

        def set_state(self):
            self.estado = True

led = Lampada ()
print(led.estado) # Ligado ou Desligado
led.set_state()
print(led.estado) # Ligado ou Desligado
led.set_state()
print(led.estado) # Ligado ou Desligado