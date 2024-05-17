def calcular_media(notas):
    return sum(notas) / len(notas)

def verificar_aprovacao(media_provas, media_trabalhos, nota_minima_prova=None, nota_minima_trabalho=None):
    if nota_minima_prova is not None and media_provas < nota_minima_prova:
        return "Reprovado: Nota mínima em uma das provas não alcançada."
    elif nota_minima_trabalho is not None and media_trabalhos < nota_minima_trabalho:
        return "Reprovado: Nota mínima nos trabalhos não alcançada."
    else:
        media_final = (media_provas + media_trabalhos) / 2
        return f"Aprovado! Média final: {media_final:.2f}"

def main():
    notas_p = [float(input(f"Nota da prova {i+1}: ")) for i in range(3)]
    notas_t = [float(input(f"Nota do trabalho {i+1}: ")) for i in range(2)]

    media_p = calcular_media(notas_p)
    media_t = calcular_media(notas_t)

    mensagem_aprovacao = verificar_aprovacao(media_p, media_t, 7.0, 6.0)
    print(mensagem_aprovacao)

if __name__ == "__main__":
    main()