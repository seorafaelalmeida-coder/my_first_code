# 1. Pedir a temperatura em graus Celsius e converter para inteiro
# lembre-se: guarde o resultado de int(input(...)) em uma variável

temperatura = int(input("Digite a temperatura em C°: "))

# 2. Se a temperatura for maior ou igual a 30, mostrar "Está calor!"
# lembre-se: use 'if', '>=', ':' e 'print(...)' indentado na linha de baixo

if temperatura >= 30:

    print("Hoje está Calor!")

# 3. Senão, se a temperatura for maior ou igual a 15, mostrar "Clima agradável."
# lembre-se: use 'elif', '>=', ':' e 'print(...)' indentado na linha de baixo

elif temperatura >= 15:
    
    print("Hoje está um clima agradável!")

# 4. Senão (para temperaturas menores que 15), mostrar "Está frio!"
# lembre-se: 'else:' não leva condição e o 'print(...)' precisa ficar indentado na linha de baixo

else:
    
    print("Hoje está frio!")