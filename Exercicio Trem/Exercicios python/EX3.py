"""História de Usuário para Trilho Infinito:

Como usuário, quero dar uma lista de comandos ao trem para movê-lo em um trilho numérico infinito.
O usuário deve informar a posição inicial do trem.
Os comandos disponíveis são "Esquerda" e "Direita".
Quero saber a posição final do trem após executar os comandos.

História de Usuário para Trilho Finito:

Como usuário, quero dar uma lista de comandos ao trem para movê-lo em um trilho numérico finito, com limites definidos pelo usuário.
O usuário deve informar a posição inicial do trem dentro dos limites.
Os comandos disponíveis são "Esquerda" e "Direita".
O trem nunca deve sair dos limites do trilho definido pelo usuário.
A lista de comandos pode ter no máximo 30 comandos.
Quero saber a posição final do trem após executar os comandos, considerando os limites do trilho."""


def calcular_posicao_final(comandos, trilho_infinito=False, limite_inferior=None, limite_superior=None):
    posicao = 0
    
    for comando in comandos:
        if comando == "Direita":
            posicao += 1
        elif comando == "Esquerda":
            posicao -= 1
        
        if not trilho_infinito:
            posicao = max(limite_inferior, min(posicao, limite_superior))
    
    return posicao

def main():
    trilho_infinito = input("O trilho é infinito? (S/N): ").upper() == "S"
    
    if not trilho_infinito:
        limite_inferior = int(input("Informe o limite inferior do trilho: "))
        limite_superior = int(input("Informe o limite superior do trilho: "))
        posicao_inicial = int(input("Informe a posição inicial do trem: "))
    else:
        limite_inferior = None
        limite_superior = None
        posicao_inicial = int(input("Informe a posição inicial do trem: "))
    
    num_comandos = int(input("Quantos comandos deseja inserir (máximo 30)? "))
    comandos = []
    for i in range(num_comandos):
        comando = input(f"Comando {i+1}: ").capitalize()
        comandos.append(comando)
    
    posicao_final = calcular_posicao_final(comandos, trilho_infinito, limite_inferior, limite_superior)
    print("Posição Final:", posicao_final)

if __name__ == "__main__":
    main()