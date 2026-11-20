# 1. Pedir a quantidade de vida (HP) do personagem e converter para inteiro
# lembre-se: guarde o resultado de int(input(...)) em uma variável

hp = int(input("Qual a quantidade de HP do personagem? "))

# 2. Se o HP for maior ou igual a 70, mostrar "Vida cheia! Pronto para o combate."
# lembre-se: use 'if', '>=', ':' e 'print(...)' indentado na linha de baixo

if hp >= 70:
    
    print("Vida cheia! pronto para combate.")

# 3. Senão, se o HP for maior ou igual a 30, mostrar "Atenção! Use uma poção em breve."
# lembre-se: use 'elif', '>=', ':' e 'print(...)' indentado na linha de baixo
elif hp >= 30:

    print("Atenção! use uma poção em breve. ")

# 4. Senão (para qualquer HP menor que 30), mostrar "Perigo! Vida crítica!"
# lembre-se: no final, use apenas 'else:' (sem condição!) e o 'print(...)' indentado

else:
    
    print("Perigo! Vida crítica!")