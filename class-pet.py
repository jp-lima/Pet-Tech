
class Pet():
    def __init__(self,nome,idade,especie,raca):
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.raca = raca
    def cadastrar(self):
        return {"nome": self.nome, "idade": self.idade, "especie": self.especie, "raca":self.raca}
