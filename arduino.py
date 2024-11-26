import time

class RoomLightController:
    def __init__(self):
        
        self.lights = [False] * 4 

    def turn_on(self, room):
        if 1 <= room <= 4:
            self.lights[room - 1] = True
            print(f"Luz do cômodo {room} acesa.")
        else:
            print("Cômodo inválido. Escolha entre 1 e 4.")

    def turn_off(self, room):
        if 1 <= room <= 4:
            self.lights[room - 1] = False
            print(f"Luz do cômodo {room} apagada.")
        else:
            print("Cômodo inválido. Escolha entre 1 e 4.")

    def status(self):
        for i in range(4):
            state = "acesa" if self.lights[i] else "apagada"
            print(f"Luz do cômodo {i + 1} está {state}.")

def main():
    controller = RoomLightController()
    
    while True:
        command = input("Digite o comando (ON:<cômodo>, OFF:<cômodo>, STATUS ou 'exit' para sair): ")
        
        if command.lower() == 'exit':
            break
        
        if command.startswith("ON:"):
            try:
                room = int(command.split(":")[1])
                controller.turn_on(room)
            except ValueError:
                print("Comando inválido. Use o formato ON:<cômodo>.")
        
        elif command.startswith("OFF:"):
            try:
                room = int(command.split(":")[1])
                controller.turn_off(room)
            except ValueError:
                print("Comando inválido. Use o formato OFF:<cômodo>.")
        
        elif command.lower() == "status":
            controller.status()
        
        else:
            print("Comando inválido. Use ON:<cômodo>, OFF:<cômodo>, STATUS ou 'exit'.")

if __name__ == "__main__":
    main()