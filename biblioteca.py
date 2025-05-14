class Animal():
    def __init__(self,nome,cor):
        self.nome=nome
        self.cor=cor

    def comer(self):
        print(f"o{self.nome}foi comer...")

class Gato(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def miar(self):
        print(f"o{self.nome} foi miar...")

class Cachorro(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def latir(self):
        print(f"o {self.nome} foi latir...")


class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def guincha(self):
        print(f"o {self.nome} ta guinchando...")


class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def mugir(self):
        print(f"a {self.nome} foi mugir...")

# ------------------------------------------------------------------------------------------

class Ingresso():
    def __init__(self,valor):
        self.valor=valor

    def imprimirvalor(self):
        print(self.valor)

class IngressoVip(Ingresso):
    def __init__(self,valor):
        super().__init__(valor)
    def imprimirvip(self):
        self.valor= self.valor + self.valor*0.5
        print(self.valor)

#-------------------------------------------------------------------------------------------

class Forma():
    def __init__(self):
        self.perimetro=0
        self.area=0



class Retangulo(Forma):
    def __init__(self,base,altura):
        super().__init__()
        self.base=base
        self.altura=altura


    def calculoarea(self):
        self.area= self.base * self.altura
        print(f"A area do retangulo é:{self.area}")

    def calculoperi(self):
        self.perimetro=self.base*2 + self.altura*2
        print(f"o perimetro do retangulo{self.perimetro}")

class Triangulo(Forma):
    def __init__(self,base,altura):
        super().__init__()
        self.base=base
        self.altura=altura

    def calculoarea(self):
        self.area= (self.base*self.altura)/2
        print(f"A area do trianguloé:{self.area}")

    def calculoperi(self):
        self.perimetro= self.base*3
        print(f"o perimetro do triangulo é:{self.perimetro}")

#-------------------------------------------------------------------------------------------

