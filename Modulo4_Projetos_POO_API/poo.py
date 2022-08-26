from mailbox import NotEmptyError
import datetime
import math


class Pessoa:
    #armazenando dados
    def __init__(self, nome: str, sobrenome: str, data_de_nascimento: datetime.date):
        self.nome = nome 
        self.sobrenome = sobrenome
        self.data_de_nascimento = data_de_nascimento

    #metodo/atributo derivado da data de nascimento deve ser uma propriedade 
    @property 
    #armazenando métodos
    def idade(self) -> int:
        #math.floor arredonda o número decimal
        return math.floor((datetime.date.today() - self.data_de_nascimento).days / 365.2425)

    def __str__(self) -> str:
        return f"{self.nome} {self.sobrenome} tem {self.data_de_nascimento} anos" 

#inicializando o objeto
#instanciando o objeto pessoa
andre = Pessoa(nome='Andre', sobrenome='Sionek', data_de_nascimento=datetime.date(1991, 1, 9))

print(andre)
print(andre.nome)
print(andre.sobrenome)
print(andre.data_de_nascimento)
print(andre.idade)