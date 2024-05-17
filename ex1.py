
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def recomendacao_do_imc(imc):
    if imc < 18.5:
        return ("Seu IMC está abaixo do média. Recomenda-se ganhar peso com uma dieta rica em nutrientes,"
                "incluindo proteínas magras, carboidratos saudáveis e gorduras boas.")
    elif 18.5 <= imc < 24.9:
        return ("Seu IMC está dentro da faixa normal. Mantenha uma dieta balanceada e continue com a prática "
                "regular de exercícios.")
    elif 25 <= imc < 29.9:
        return ("Seu IMC indica sobrepeso. Recomenda-se adotar uma dieta equilibrada com controle de calorias "
                "e aumentar a prática de atividades físicas.")
    elif 30 <= imc < 34.9:
        return ("Seu IMC indica obesidade grau I. É importante buscar orientação médica para um plano de perda "
                "de peso, incluindo dieta e exercício.")
    elif 35 <= imc < 39.9:
        return ("Seu IMC indica obesidade grau II. Recomenda-se fortemente buscar acompanhamento médico para "
                "um plano de emagrecimento adequado.")
    else:
        return ("Seu IMC indica obesidade grau III. É crucial procurar ajuda médica imediata para tratar a obesidade "
                "e prevenir complicações graves.")

def main():
    try:

        peso = float(input("Digite seu peso em kg: "))
        altura = float(input("Digite sua altura em metros: "))
        
        imc = calcular_imc(peso, altura)
        print(f"Seu IMC é: {imc:.2f}")
        
        recomendacao = recomendacao_do_imc(imc)
        print(recomendacao)
        
    except ValueError:
        print("Por favor, insira valores válidos para peso e altura.")

if __name__ == "__main__":
    main()