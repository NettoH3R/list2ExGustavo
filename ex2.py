def verificar_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def primos_inferiores(n):
    primos = []
    for i in range(2, n + 1):
        if verificar_primo(i):
            primos.append(i)
    return primos

def main():
    try:
        numero = int(input("Digite um número inteiro: "))
        
        if numero < 1:
            print("Por favor, insira um número maior que 0.")
            return
        
        if verificar_primo(numero):
            print(f"{numero} é um número primo.")
        else:
            print(f"{numero} não é um número primo.")
        
        # Imprime todos os números primos até o número fornecido
        primos = primos_inferiores(numero)
        print(f"Números primos de 1 até {numero}: {primos}")
        
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

if __name__ == "__main__":
    main()