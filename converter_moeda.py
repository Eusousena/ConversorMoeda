import time

class Moeda:
    def __init__(self, code_coin, taxa):
        self.code_coin = code_coin
        self.taxa = taxa

    TAXAS_CAMBIO = {  # Defined within the class for better encapsulation
        "USD": 5.20,
        "EUR": 5.80,
        "GBP": 6.30,
    }

    @classmethod
    def from_codigo(cls, code_coin):
        if code_coin not in cls.TAXAS_CAMBIO:
            raise ValueError(f"A moeda {code_coin} não é suportada")
        return cls(code_coin, cls.TAXAS_CAMBIO[code_coin])

class ConversorMoeda:
    @staticmethod
    def get_taxa_cambio(code_coin):
        moeda = Moeda.from_codigo(code_coin)  # Use Moeda.from_codigo for consistency
        return moeda.taxa

    @staticmethod
    def converter(valor_a_ser_convertido, moeda_origem, moeda_destino):
        taxa_origem = ConversorMoeda.get_taxa_cambio(moeda_origem)
        taxa_destino = ConversorMoeda.get_taxa_cambio(moeda_destino)

        valor_convertido = valor_a_ser_convertido * (taxa_destino / taxa_origem)
        return valor_convertido

while True:
    print("Bem Vindo ao conversor de moedas Plus.")
    time.sleep(1)

    moeda = input("""
[1]USD
[2]EUR
[3]GBP
Qual moeda deseja converter para real?:         
""")
    time.sleep(0.5)

    try:
        valor = float(input("Qual o valor?: "))
    except ValueError:
        print("Valor inválido. Insira um número decimal.")
        continue  # Skip to the next iteration if input is invalid

    if moeda == "1":
        real = Moeda("BRL", 1.0)  # Create a Real object once (optional)
        dolar = Moeda.from_codigo("USD")
        valor_convertido = ConversorMoeda.converter(valor, dolar, real)
        print(f"US$ {valor:.2f} equivalem a R$ {valor_convertido:.2f}")
    elif moeda == "2":
        real = Moeda("BRL", 1.0)  # Create a Real object once (optional)
        euro = Moeda.from_codigo("EUR")
        valor_convertido = ConversorMoeda.converter(valor, euro, real)
        print(f"€ {valor:.2f} equivalem a R$ {valor_convertido:.2f}")
    elif moeda == "3":
        real = Moeda("BRL", 1.0)  # Create a Real object once (optional)
        libra = Moeda.from_codigo("GBP")
        valor_convertido = ConversorMoeda.converter(valor, libra, real)
        print(f"£ {valor:.2f} equivalem a R$ {valor_convertido:.2f}")
    else:
        print("Opção inválida")
