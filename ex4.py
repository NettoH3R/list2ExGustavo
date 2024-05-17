def celsius_para_fahrenheit(temp_celsius):
    # C° => F°
    return (temp_celsius * 9/5) + 32

def fahrenheit_para_celsius(temp_fahrenheit):
    # F° => C°
    return (temp_fahrenheit - 32) * 5/9

def main():
    c_ou_f = input("Escolha a conversão desejada:\n1. Celsius para Fahrenheit\n2. Fahrenheit para Celsius\n")
    
    if c_ou_f == '1':
        temp_C = float(input("Digite a temperatura em Celsius: "))
        temp_F = celsius_para_fahrenheit(temp_C)
        print(f"A temperatura em Fahrenheit é: {temp_F:.2f} °F")
    elif c_ou_f == '2':
        temp_F = float(input("Digite a temperatura em Fahrenheit: "))
        temp_C = fahrenheit_para_celsius(temp_F)
        print(f"A temperatura em Celsius é: {temp_C:.2f} °C")
    else:
        print("Escolha inválida. Por favor, escolha 1 ou 2.")

if __name__ == "__main__":
    main()