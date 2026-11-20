# 1. Pedir a velocidade do carro em km/h e converter para inteiro
# lembre-se: guarde o resultado de int(input(...)) em uma variável

velocidade = int(input("Qual a Velocidade do carro em Km/h? "))

# 2. Se a velocidade for maior que 80, mostrar "Acima do limite! Multa."
# lembre-se: use 'if', '>', ':' e 'print(...)' indentado na linha de baixo

if velocidade > 80:
    
    print("Acima do limite! Multa. ")

# 3. Senão, se a velocidade for maior ou igual a 60, mostrar "Velocidade segura na via."
# lembre-se: use 'elif', '>=', ':' e 'print(...)' indentado na linha de baixo

elif velocidade >= 60:

    print("Velocidade segura na via. ")

# 4. Senão (para qualquer velocidade menor que 60), mostrar "Abaixo do limite da via."
# lembre-se: use apenas 'else:' (sem condição!) e o 'print(...)' indentado na linha de baixo

else:
    
    print("Abaixo do limite da via. ")