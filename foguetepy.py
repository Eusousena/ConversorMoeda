class Foguete:
    def __init__(self, nome_foguete, planeta, tempo):
        self.nome_foguete = nome_foguete
        self.planeta = planeta
        self.tempo = tempo

    @classmethod
    def ida(cls, nome_foguete, planeta, tempo):
        print(f"{nome_foguete} indo para o planeta {planeta}. tempo de duração {tempo}")

    @classmethod
    def volta(cls):
        return f"voltando para a terra" 


Foguete.ida(nome_foguete="apoloh", planeta="marte", tempo=10)
print(Foguete.volta())
