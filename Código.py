# Alunos: João Silva RM123456, Maria Souza RM654321

# Função para validar entrada numérica e evitar erros
def ler_numero(mensagem, tipo=float):
    while True:
        try:
            valor = tipo(input(mensagem))
            return valor
        except ValueError:
            print("Valor inválido. Tente novamente.")


# Função para cadastrar novos bairros e seus dados
def cadastrar_bairro(dados):
    print("\nCadastro de Bairro - Informações Obrigatórias")
    nome = input("Nome do bairro: ").strip()
    chuva = ler_numero("Quantidade de chuva nas últimas 24h (mm): ")
    nivel_rio = ler_numero("Nível do rio (m): ")
    ocorrencias = ler_numero("Ocorrências de enchente registradas mês passado: ", int)
    bairro = {
        "nome": nome,
        "chuva": chuva,
        "nivel_rio": nivel_rio,
        "ocorrencias": ocorrencias
    }
    dados.append(bairro)
    print("Cadastro realizado com sucesso!\n")


# Função para analisar risco de enchente em cada bairro
def analisar_risco(dados):
    print("\nAnálise de Risco de Enchente:")
    for bairro in dados:
        risco = "Baixo"
        # Critérios fictícios: chuva > 80mm, nível do rio > 4.5m, ocorrências passadas
        if bairro['chuva'] > 100 or bairro['nivel_rio'] > 5 or bairro['ocorrencias'] > 2:
            risco = "Alto"
        elif bairro['chuva'] > 60 or bairro['nivel_rio'] > 4:
            risco = "Moderado"

        print(f"- Bairro: {bairro['nome']}")
        print(f"  Chuva: {bairro['chuva']} mm | Rio: {bairro['nivel_rio']} m | Ocorrências: {bairro['ocorrencias']}")
        print(f"  >> Risco: {risco}")
        # Sugestão conforme risco
        if risco == 'Alto':
            print("   Alerta: Atenção máxima! Reforçar monitoramento e evacuar áreas de risco.")
        elif risco == 'Moderado':
            print("   Atenção: Monitorar área e informar moradores.")
        else:
            print("   Situação estável. Manter monitoramento de rotina.")
        print()


# Função para consultar bairros
def listar_bairros(dados):
    print("\nLista de bairros cadastrados:")
    for bairro in dados:
        print(f"- {bairro['nome']}")
    print()


# Função principal de menu
def main():
    # Lista que armazena dados dos bairros (estrutura solicitada)
    bairros = []
    while True:
        print("\n========= Sistema de Gestão de Riscos de Enchentes =========")
        print("1. Cadastrar Bairro")
        print("2. Analisar Risco de Enchente")
        print("3. Listar Bairros")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_bairro(bairros)
        elif opcao == "2":
            if bairros:
                analisar_risco(bairros)
            else:
                print("Nenhum bairro cadastrado.")
        elif opcao == "3":
            if bairros:
                listar_bairros(bairros)
            else:
                print("Nenhum bairro cadastrado.")
        elif opcao == "4":
            print("Saindo... Obrigado por utilizar!")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Execução do programa
if __name__ == "__main__":
    main()