class Persona:

    def __init__(self, nome, eta):

        self.nome = nome

        self.eta = eta


    def __getattribute__(self, attributo):

        print(f"Sto accedendo all'attributo: {attributo}")

        return super().__getattribute__(attributo)


p = Persona("Mario", 30)


# accesso agli attributi

print(p.nome)

print(p.eta)