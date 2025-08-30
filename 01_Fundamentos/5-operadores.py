num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

soma = num1 + num2
subtracao = num1 - num2
divisao = num1 / num2
multiplicacao = num1 * num2
mod = num1 % num2
exp = num1 ** num2

print("A multiplicação é:", multiplicacao)
print("O módulo é:", mod)
print("A exponenciação é:", exp)

#Comparação

bigger = num1 > num2
print("O primeiro número é maior que o segundo?", bigger)

smaller = num1 < num2   
print("O primeiro número é menor que o segundo?", smaller)

equal = num1 == num2    
print("Os números são iguais?", equal)

different = num1 != num2    
print("Os números são diferentes?", different)

bigger_equal = num1 >= num2
print("O primeiro número é maior ou igual ao segundo?", bigger_equal)

smaller_equal = num1 <= num2
print("O primeiro número é menor ou igual ao segundo?", smaller_equal) 