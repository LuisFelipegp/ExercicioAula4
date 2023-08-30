"""Trilho finito:
O usuário deseja simular o movimento de um trem em um trilho numérico infinito. 
Ele deve ser capaz de fornecer uma lista de comandos de movimento (DIREITA ou ESQUERDA)
e o sistema deve calcular a posição final do trem após seguir esses comandos.[

Trilho Finito:
O usuário deseja uma simulação de movimento de trem em um trilho numérico finito, que varia de -2 a +10. 
Ele deve inserir uma lista de comandos de movimento, e o sistema deve garantir que a posição final do trem permaneça dentro dos limites do trilho, 
ou seja, entre -2 e +10.
"""

def final_position(commands, rail_type="infinito"):
    position = 0
    
    if rail_type == "finito":
        min_position = -2
        max_position = 10
    else:
        min_position = float("-inf")
        max_position = float("inf")
    
    for command in commands:
        if command == 'DIREITA':
            position = min(position + 1, max_position)
        elif command == 'ESQUERDA':
            position = max(position - 1, min_position)
    
    return position

# Obtendo os comandos do usuário
num_commands = int(input("Quantos comandos deseja inserir? "))
user_commands = []
for _ in range(num_commands):
    command = input("Informe o comando (DIREITA ou ESQUERDA): ")
    user_commands.append(command)

# Escolhendo o tipo de trilho
rail_type = input("Deseja usar trilho infinito ou finito? (infinito/finito): ")

# Calculando e exibindo a posição inicial e final
initial_pos = 0
print("Posição Inicial:", initial_pos)

final_pos = final_position(user_commands, rail_type)
print("Posição Final:", final_pos)