class Passageiro:
    def __init__(self, nome: str, documento: str):
        self.nome = nome
        self.documento = documento

    def __repr__(self):
        return f"Passageiro(nome={self.nome}, documento={self.documento})"

# Classe Corrida
class Corrida:
    def __init__(self, nota: int, distancia: float, valor: float, passageiro: Passageiro):
        self.nota = nota
        self.distancia = distancia
        self.valor = valor
        self.passageiro = passageiro

    def __repr__(self):
        return (f"Corrida(nota={self.nota}, distancia={self.distancia}, valor={self.valor}, "
                f"passageiro={self.passageiro})")

# Classe Motorista
class Motorista:
    def __init__(self, nota: int):
        self.nota = nota
        self.corridas = []

    def adicionar_corrida(self, corrida: Corrida):
        self.corridas.append(corrida)

    def __repr__(self):
        return f"Motorista(nota={self.nota}, corridas={self.corridas})"