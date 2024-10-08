class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")

class MotoristaCLI(SimpleCLI):
    def __init__(self, motorista_model):
        super().__init__()
        self.motorista_model = motorista_model
        self.add_command("create", self.create_motorista)
        self.add_command("read", self.read_motorista)
        self.add_command("update", self.update_motorista)
        self.add_command("delete", self.delete_motorista)

    def create_motorista(self):
        nota_motorista = int(input("Adicione a nota do motorista(1-10): "))
        
        # Criar objeto motorista
        motorista_id = self.motorista_model.create_motorista(nota_motorista)
        print(f"Motorista criado com o ID {motorista_id}")

        # Adicionar corridas
        while True:
            add_corrida = input("Adicionar uma corrida? (yes/no): ").lower()
            if add_corrida == 'no':
                break
            
            nota_corrida = int(input("Nota da corrida (0-5): "))
            distancia = float(input("Distancia (km): "))
            valor = float(input("Preço (R$): "))

            # Criar passageiro associado
            passageiro_nome = input("nome do passageiro: ")
            passageiro_documento = input("documento do passageiro: ")

            # Montar o objeto corrida
            corrida = {
                "nota": nota_corrida,
                "distancia": distancia,
                "valor": valor,
                "passageiro": {
                    "nome": passageiro_nome,
                    "documento": passageiro_documento
                }
            }

            # Adiciona a corrida ao motorista
            self.motorista_model.add_corrida(motorista_id, corrida)
            print(f"Corrida adicionada para o motorista com ID {motorista_id}.")

    def read_motorista(self):
        motorista_id = input("ID do motorista: ")
        motorista = self.motorista_model.read_motorista_by_id(motorista_id)
        if motorista:
            print(f"Nota do Motorista: {motorista['nota']}")
            print("Corridas:")
            for corrida in motorista['corridas']:
                print(f" - Nota: {corrida['nota']}, Distância: {corrida['distancia']} km, Valor: R$ {corrida['valor']}")
                passageiro = corrida['passageiro']
                print(f"   Passageiro: {passageiro['nome']}, Documento: {passageiro['documento']}")
        else:
            print("Motorista não encontrado.")

    def update_motorista(self):
        motorista_id = input("ID do motorista: ")
        nova_nota = int(input("nova nota do motorista: "))
        self.motorista_model.update_motorista(motorista_id, nova_nota)
        print(f"Motorista com ID {motorista_id} atualizado.")

    def delete_motorista(self):
        motorista_id = input("ID do motorista: ")
        self.motorista_model.delete_motorista(motorista_id)
        print(f"Motorista de ID {motorista_id} deletado.")

    def run(self):
        print("Bem vindo")
        print("Comando disponíveis: create, read, update, delete, quit")
        super().run()