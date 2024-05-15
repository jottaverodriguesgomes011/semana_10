class Lampada:
    def __init__(self):
        self.estado = False

    def set_state(self):
        self.estado = True

led = Lampada ()

while True:
    print('O estado atual da lampada é:', led.estado)