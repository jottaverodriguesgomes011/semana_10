class Lampada:
    def __init__(self):
        self.estado = False

    def set_state(self):
        self.estado = True

led = Lampada ()

while True:
    print('O estado atual da lampada é:', led.estado)
    
    print('Digite [!] para alterar o estado da lampada')
    print('Digite [0] para sair do programa')

    option = input('Digite sua escolha: ')

    if option == '!':
        led.set_state()
    elif option == 0:
        break;
