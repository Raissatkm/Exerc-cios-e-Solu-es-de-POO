class Pessoa():
    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.estado = "parado"

    def parar(self):
        if self.estado == "parado":
            print(self.nome, "está parado")
        else:
            self.estado = "parado"
            print("Mudando de estado para parado!")

    def comer(self):
        if self.estado == "comendo":
            print(self.nome, "já está comendo")
        elif self.estado == "parado":
            print(self.nome, "mudando de estado para comendo.")
            self.estado = "comendo"
        else:
            print(self.nome, "não pode  comer")

    def andar(self):
        if self.estado == "andando":
            print(self.nome, "já está andando")
        elif self.estado == "parado":
            print(self.nome, 'mudando de estado para andando')
            self.estado = "andando"
        else:
            print(self.nome, "não pode andar")

    def falar(self):
        if self.estado == "falando":
            print(self.nome, "está falando")
        elif self.estado == "parado":
            print(self.nome, "mudando de estado para falando.")
            self.estado = "falando"
        else:
            print(self.nome, "não pode falar")

