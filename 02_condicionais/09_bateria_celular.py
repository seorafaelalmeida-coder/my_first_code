# 1. Pedir o nível de bateria do celular (0 a 100) e converter para inteiro
# lembre-se: guarde o resultado de int(input(...)) em uma variável

bateria = int(input("Qual o nível de bateria do celular? "))

# 2. Se a bateria for maior ou igual a 80, mostrar "Bateria carregada! Tudo certo."
# lembre-se: use 'if', '>=', ':' e 'print(...)' indentado na linha de baixo

if bateria >= 80:
    
    print("Bateria carregada! ")

# 3. Senão, se a bateria for maior ou igual a 20, mostrar "Bateria moderada. Dá para usar tranquilo."
# lembre-se: use 'elif', '>=', ':' e 'print(...)' indentado na linha de baixo

elif bateria >= 20:

    print("Bateria moderada. ")

# 4. Senão (para qualquer nível menor que 20), mostrar "Bateria fraca! Conecte o carregador."
# lembre-se: use apenas 'else:' (sem condição!) e o 'print(...)' indentado na linha de baixo

else:

    print("Bateria fraca!")
