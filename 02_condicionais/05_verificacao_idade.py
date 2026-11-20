# 1. Pedir a idade do usuário e converter para inteiro
# lembre-se: guarde o resultado de int(input(...)) em uma variável

idade = int(input("Digite sua idade: "))

# 2. Se a idade for maior que 18, mostrar "Acesso Autorizado Maior de Idade"
# lembre-se: use 'if', '>', ':' e 'print(...)' indentado na linha de baixo

if idade > 18:
    print("Acesso Autorizado Maior de Idade")

# 3. Senão, se a idade for exatamente igual a 18, mostrar "Acesso Autorizado 18 Anos"
# lembre-se: use 'elif', '==', ':' e 'print(...)' indentado na linha de baixo

elif idade == 18:
    print("Acesso Autorizado 18 Anos")

# 4. Senão (para qualquer idade menor que 18), mostrar "Acesso Negado"
# lembre-se: 'else:' não leva condição e o 'print(...)' precisa ficar indentado na linha de baixo

else:
    print("Acesso Negado")