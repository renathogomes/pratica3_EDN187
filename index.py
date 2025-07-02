# 1- Classificador de Idade
def classificar_idade():
    try:
        idade = int(input("Digite sua idade: "))
        if 0 <= idade <= 12:
            print("Criança")
        elif 13 <= idade <= 17:
            print("Adolescente")
        elif 18 <= idade <= 59:
            print("Adulto")
        elif idade >= 60:
            print("Idoso")
        else:
            print("Idade inválida")
    except ValueError:
        print("Por favor, digite um número inteiro válido")

# 2- Calculadora de IMC
def calcular_imc():
    try:
        peso = float(input("Digite seu peso em kg: "))
        altura = float(input("Digite sua altura em metros: "))
        if peso <= 0 or altura <= 0:
            print("Peso e altura devem ser valores positivos")
            return
        imc = peso / (altura ** 2)
        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 25:
            classificacao = "Peso normal"
        elif imc < 30:
            classificacao = "Sobrepeso"
        else:
            classificacao = "Obeso"
        print(f"Seu IMC é {imc:.2f} - Classificação: {classificacao}")
    except ValueError:
        print("Por favor, digite valores numéricos válidos")

# 3- Conversor de Temperatura
def converter_temperatura():
    try:
        temp = float(input("Digite a temperatura: "))
        origem = input("Digite a unidade de origem (C/F/K): ").upper()
        destino = input("Digite a unidade de destino (C/F/K): ").upper()
        
        if origem not in ['C', 'F', 'K'] or destino not in ['C', 'F', 'K']:
            print("Unidades inválidas! Use C para Celsius, F para Fahrenheit ou K para Kelvin")
            return
            
        # Converter tudo para Celsius primeiro
        if origem == 'F':
            temp_c = (temp - 32) * 5/9
        elif origem == 'K':
            temp_c = temp - 273.15
        else:
            temp_c = temp
            
        # Converter de Celsius para a unidade de destino
        if destino == 'F':
            result = (temp_c * 9/5) + 32
            unidade = '°F'
        elif destino == 'K':
            result = temp_c + 273.15
            unidade = 'K'
        else:
            result = temp_c
            unidade = '°C'
            
        print(f"Temperatura convertida: {result:.2f}{unidade}")
    except ValueError:
        print("Por favor, digite um valor numérico válido")

# 4- Verificador de Ano Bissexto
def verificar_ano_bissexto():
    try:
        ano = int(input("Digite o ano: "))
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            print(f"{ano} é um ano bissexto")
        else:
            print(f"{ano} não é um ano bissexto")
    except ValueError:
        print("Por favor, digite um ano válido")

# Menu principal
def main():
    while True:
        print("\n=== Menu ===")
        print("1. Classificador de Idade")
        print("2. Calculadora de IMC")
        print("3. Conversor de Temperatura")
        print("4. Verificador de Ano Bissexto")
        print("5. Sair")
        
        opcao = input("Escolha uma opção (1-5): ")
        
        if opcao == '1':
            classificar_idade()
        elif opcao == '2':
            calcular_imc()
        elif opcao == '3':
            converter_temperatura()
        elif opcao == '4':
            verificar_ano_bissexto()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Escolha entre 1 e 5")

if __name__ == "__main__":
    main()