def contar_vogais(s):
    vogais = "aeiouAEIOU"
    count = 0
    
    for char in s:
        if char in vogais:
            count += 1
            
    return count

def main():
    frase = input("Digite uma string: ")
    num_vogais = contar_vogais(frase)
    
    print(f"O número de vogais na string fornecida é: {num_vogais}")

if __name__ == "__main__":
    main()