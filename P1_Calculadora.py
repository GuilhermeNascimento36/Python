# Calculadora em Python

loopControl = 0
v1 = 0
v2 = 0

import math

def calc(opcao):
    v1 = float(input("\nValor 1: "))
    v2 = float(input("Valor 2: "))
    
    if (opcao == 1):
        return print("\nResultado: ", v1 + v2)
    
    elif (opcao == 2):
        return print("\nResultado: ", v1 - v2)
    
    elif (opcao == 3):
        return print("\nResultado: ", v1 * v2)
    
    elif (opcao == 4):
        if(v1 == 0 or v2 == 0):
            return print("Não é possível dividir por zero.")
        return print("\nResultado: ", v1 / v2)
    
    elif (opcao == 5):
        print("\nRaíz quadrada do valor 1: ", math.sqrt(v1))
        print("Raíz quadrada do valor 2: ", math.sqrt(v2))
    
    elif (opcao == 6):
        if(v1 == 0 or v2 == 0):
            return print("Não é possível elevar na potência zero.")
        print("O valor 1 será elevado pelo valor 2")
        return print("\nResultado: ", math.pow(v1, v2))
    
    else:
        return print("Operação não encontrada.")
    
    
print("CALCULADORA PYTHON")
while loopControl == 0:
  
    print("\nEscolha a operação desejada")
    print("1.Soma\n2.Subtração\n3.Multiplicação\n4.Divisão\n5.Raíz Quadrada\n6.Exponenciação\n7.Sair")
    opcao = int(input("\nOpção: "))
    
    if (opcao > 7 or opcao < 1):
        print("\nopção incorreta!\n")
        
    elif opcao == 7:
        print("\nObrigado por testar o programa!")
        break
        
    else:
        calc(opcao)