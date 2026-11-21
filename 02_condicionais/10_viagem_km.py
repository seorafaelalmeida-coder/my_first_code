# 1. Pedir a distância da viagem em km e converter para inteiro
# lembre-se: guarde o resultado de int(input(...)) em uma variável

distancia = int(input("Qual a distancia em Km da viagem? "))

# 2. Se a distância for maior ou igual a 500, mostrar "Viagem longa! Prepare o carro."
# lembre-se: use 'if', '>=', ':' e 'print(...)' indentado na linha de baixo

if distancia >= 500:
    print("Viagem longa! Prepare o carro. ")

# 3. Senão, se a distância for maior ou igual a 100, mostrar "Viagem média. Boa estrada!"
# lembre-se: use 'elif', '>=', ':' e 'print(...)' indentado na linha de baixo

elif distancia >=100:
    print("Viagem média. Boa estrada! ")

# 4. Senão (para qualquer distância menor que 100), mostrar "Viagem curta. Vai tranquilo!"
# lembre-se: use apenas 'else:' (sem condição!) e o 'print(...)' indentado na linha de baixo

else:
    print("Viagem curta. Vai tranquilo! ")