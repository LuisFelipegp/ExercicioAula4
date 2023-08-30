def final_position(commands):
    position = 0
    
    for command in commands:
        if command == 'direita':
            position += 1
        elif command == 'ESQUERDA':
            position -= 1
            
    return position

# Obtendo os comandos do usuário
num_commands = int(input("Quantos comandos deseja inserir? "))
user_commands = []
for _ in range(num_commands):
    command = input("Informe o comando (DIREITA ou ESQUERDA): ")
    user_commands.append(command)

# Calculando e exibindo a posição inicial e final
initial_pos = 0
print("Posição Inicial:", initial_pos)

final_pos = final_position(user_commands)
print("Posição Final:", final_pos)
