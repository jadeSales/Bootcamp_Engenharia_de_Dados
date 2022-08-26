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

class Curriculo:
    def __init__(self, pessoa: Pessoa, experiencias: list[str]):
        self.pessoa = pessoa
        self.experiencias = experiencias

    @property
    def quantidade_de_experiencias(self) -> int:
        return len(self.experiencias)

    @property
    def empresa_atual(self) -> str:
        return self.experiencias[-1]

    def adiciona_experiencia(self, experiencia: str) -> None:
        self.experiencias.append(experiencia)

    def __str__(self):
        return f"{self.pessoa.nome} {self.pessoa.sobrenome} tem {self.pessoa.data_de_nascimento} anos e já " \
            f"trabalhou em {self.quantidade_de_experiencias} empresas e atualmente trabalha na empresa {self.empresa_atual}" 


#inicializando o objeto
#instanciando o objeto pessoa
andre = Pessoa(nome='Andre', sobrenome='Sionek', data_de_nascimento=datetime.date(1991, 1, 9))

curriculo_andre = Curriculo(
    pessoa=andre, 
    experiencias=['HSBC', 'Polyteck', 'Boticario', 'Olist', 'EmCasa', 'Gousto']
)

print(curriculo_andre.pessoa)
curriculo_andre.adiciona_experiencia("How Education")
print(curriculo_andre)


class Vivente:
    def __init__(self, nome: str, data_de_nascimento: datetime.date) -> None:
        self.nome = nome
        self.data_de_nascimento = data_de_nascimento

    @property
    def idade(self) -> int:
        #math.floor arredonda o número decimal
        return math.floor((datetime.date.today() - self.data_de_nascimento).days / 365.2425)

    def emite_ruido(self, ruido: str):
        print(f"{self.nome} fez ruido: {ruido}")


class PessoaHeranca(Vivente):
    def __str__(self) -> str:
        return f"{self.nome} tem {self.idade} anos"

    def fala(self, frase):
        return self.emite_ruido(frase)


class Cachorro(Vivente):
    def __init__(self, nome: str,  data_de_nascimento: datetime.date, raca: str):
        super().__init__(nome, data_de_nascimento)
        self.raca = raca


    def __str__(self) -> str:
        return f"{self.nome} é da raca {self.raca} e tem {self.idade} anos"
    
    def late(self):
        return self.emite_ruido("au au")


andre2 = PessoaHeranca(nome='Andre', data_de_nascimento=datetime.date(1991, 1, 9))

print(andre2)

belisco = Cachorro(nome='Belisco', data_de_nascimento=datetime.date(2019, 4, 15), raca='Lhasa Apso')


print(belisco)

belisco.late()
andre2.fala("Cala a boca belisco")
belisco.late()

