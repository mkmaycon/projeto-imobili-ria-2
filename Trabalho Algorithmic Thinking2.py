import csv
class Imovel:
    def __init__(self, tipo, quartos=1, vagas=0, possui_criancas=True):
        self.tipo = tipo.lower()
        self.quartos = quartos
        self.vagas = vagas
        self.possui_criancas = possui_criancas

    def calcular_aluguel(self):
        valor = 0

        if self.tipo == "apartamento":
            valor = 700
            if self.quartos == 2:
                valor += 200

            if not self.possui_criancas:
                valor *= 0.95  # desconto de 5%

            valor += self.vagas * 300

        elif self.tipo == "casa":
            valor = 900
            if self.quartos == 2:
                valor += 250

            valor += self.vagas * 300

        elif self.tipo == "estudio":
            valor = 1200

            if self.vagas >= 2:
                valor += 250  # duas vagas
                if self.vagas > 2:
                    valor += (self.vagas - 2) * 60

        return valor
    import csv

class Orcamento:
    VALOR_CONTRATO = 2000

    def __init__(self, imovel, parcelas_contrato):
        self.imovel = imovel
        self.parcelas_contrato = min(parcelas_contrato, 5)

    def calcular_valor_mensal(self):
        return self.imovel.calcular_aluguel()

    def calcular_parcela_contrato(self):
        return self.VALOR_CONTRATO / self.parcelas_contrato

    def gerar_csv(self, nome_arquivo="orcamento.csv"):
        aluguel = self.calcular_valor_mensal()
        parcela_contrato = self.calcular_parcela_contrato()

        with open(nome_arquivo, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Mês", "Aluguel", "Parcela Contrato", "Total Mensal"])

            for mes in range(1, 13):
                total = aluguel
                if mes <= self.parcelas_contrato:
                    total += parcela_contrato

                writer.writerow([mes, aluguel, 
                                 parcela_contrato if mes <= self.parcelas_contrato else 0,
                                 total])
            

def main():
    print("===== GERADOR DE ORÇAMENTO R.M =====")

    tipo = input("Tipo (apartamento, casa, estudio): ")
    quartos = int(input("Quantidade de quartos: "))
    vagas = int(input("Quantidade de vagas: "))
    parcelas = int(input("Parcelas do contrato (até 5): "))

    possui_criancas = True
    if tipo.lower() == "apartamento":
        resp = input("Possui crianças? (s/n): ")
        possui_criancas = resp.lower() == "s"

    imovel = Imovel(tipo, quartos, vagas, possui_criancas)
    orcamento = Orcamento(imovel, parcelas)

    aluguel = orcamento.calcular_valor_mensal()
    parcela_contrato = orcamento.calcular_parcela_contrato()

    print("\n===== RESULTADO =====")
    print(f"Aluguel mensal: R$ {aluguel:.2f}")
    print(f"Parcela do contrato: R$ {parcela_contrato:.2f}")
    print("Contrato total: R$ 2000.00")

    orcamento.gerar_csv()
    print("Arquivo CSV gerado com sucesso!")

if __name__ == "__main__":
    main()