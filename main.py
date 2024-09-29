def calc_size(dificuldade):
    if dificuldade == 1:
        size = 5
    elif dificuldade == 2:
        size = 10
    else:
        size = 15
    return size

def dicionarios():
    positions = {
        "X": {
            "1": {
                "coordenadas": {"1x1", "2x2", "3x3", "4x4", "5x5", "1x5", "2x4", "4x2", "5x1"},
                "respostas": 9
            },
            "2": {
                "coordenadas": {
                    "1x1", "2x2", "3x3", "4x4", "5x5", "6x6", "7x7", "8x8", "9x9", "10x10",
                    "1x10", "2x9", "3x8", "4x7", "5x6", "6x5", "7x4", "8x3", "9x2", "10x1"
                },
                "respostas": 20
            },
            "3": {
                "cooredenadas": {
                    "1x1", "2x2", "3x3", "4x4", "5x5", "6x6", "7x7", "8x8", "9x9", "10x10",
                    "11x11", "12x12", "13x13", "14x14", "15x15",
                    "1x15", "2x14", "3x13", "4x12", "5x11", "6x10", "7x9", "8x8", "9x7", "10x6",
                    "11x5", "12x4", "13x3", "14x2", "15x1"
                },
                "respostas": 30
            }
        },
        "O": {
            "1": {
                "coordenadas": {"3x1", "2x1", "1x2", "1x3", "1x4", "2x5", "3x5", "4x5", "5x4", "5x3", "5x2", "4x1"},
                "respostas": 12
            },
            "2": {
                "coordenadas": {
                    "5x1", "4x1", "3x2", "2x3", "1x4", "1x5", "1x6", "1x7", "2x8", "3x9", "4x10",
                    "5x10", "6x10", "7x10", "8x9", "9x8", "10x7", "10x6", "10x5", "10x4", "9x3", "8x2",
                    "7x1", "6x1"
                },
                "respostas": 24
            },
            "3": {
                "coordenadas": {
                    "8x1", "7x2", "6x3", "5x4", "4x5", "3x6", "2x7", "1x8", "1x9", "1x10", "1x11",
                    "1x12", "2x13", "3x14", "4x15", "5x15", "6x15", "7x15", "8x15", "9x15",
                    "10x14", "11x13", "12x12", "13x11", "14x10", "15x9", "15x8", "15x7", "14x6",
                    "13x5", "12x4", "11x3", "10x2", "9x1"},
                "respostas": 34
            }
        }
    }

    def print_dic(dic, size):
        for x in range(1,size+1):
            linha = ""
            for y in range(1,size+1):
                chave = f"{x}x{y}"
                valor = dic[chave] if dic[chave] is not None else " . "
                linha += f"{valor} "
            print(linha)

    def create_board(formato, dificuldade, size):

        suture_board = {}

        for i in range(size):
            for j in range(size):
                coord = f"{i + 1}x{j + 1}"
                suture_board[coord] = "."
                if formato == "X" and coord in positions["X"][f"{dificuldade}"]["coordenadas"]:
                    suture_board[coord] = "X"
                if formato == "O" and coord in positions["O"][f"{dificuldade}"]["coordenadas"]:
                    suture_board[coord] = "O"
        return suture_board

    def game():
        formato = input("Qual formato deseja? (X/O)?\n->").strip().upper()
        dificuldade = int(input("\nQual dificuldade deseja escolher?\n\n1 - Fácil\n2 - Médio\n3 - Difícil\n\n->"))
        size = calc_size(dificuldade)

        print()
        print_dic({f"{i}x{j}": "." for i in range(1, size + 1) for j in range(1, size + 1)},size)

        print("\nVamos iniciar o exercício. Com base no formato apresentado, digite a Coordenada do mapa que você deve colocar os pontos.")
        respostas = {}

        for i in range(positions[formato][f"{dificuldade}"]["respostas"]):

            resp = input("Digite uma coordenada que você deve colocar um ponto:\n(NúmeroDaLinhaxNúmeroDaColuna)\n->")

            if resp in respostas:
                print("\nCORRETO! Porém você já digitou essa resposta anteriormente...\n")
            elif resp in positions[formato][f"{dificuldade}"]["coordenadas"]:
                print("\nCORRETO!\n")
                respostas[resp] = ""
            else:
                print("\nCoordenada errada.\n")

        suture_board = create_board(formato, dificuldade, size)
        print("\nExercício finalizado, o local dos pontos é o seguinte:")
        print_dic(suture_board,size)

    game()

def listas():

    positions = [
        [
            [["1x1", "2x2", "3x3", "4x4", "5x5", "1x5", "2x4", "4x2", "5x1"],9],
            [["1x1", "2x2", "3x3", "4x4", "5x5", "6x6", "7x7", "8x8", "9x9", "10x10", "1x10", "2x9", "3x8", "4x7", "5x6", "6x5", "7x4", "8x3", "9x2", "10x1"],20],
            [["1x1", "2x2", "3x3", "4x4", "5x5", "6x6", "7x7", "8x8", "9x9", "10x10", "11x11", "12x12", "13x13", "14x14", "15x15", "1x15", "2x14", "3x13", "4x12", "5x11", "6x10", "7x9", "8x8", "9x7", "10x6","11x5", "12x4", "13x3", "14x2", "15x1"],30]
        ],
        [
            [["3x1", "2x1", "1x2", "1x3", "1x4", "2x5", "3x5", "4x5", "5x4", "5x3", "5x2", "4x1"], 12],
            [["5x1", "4x1", "3x2", "2x3", "1x4", "1x5", "1x6", "1x7", "2x8", "3x9", "4x10", "5x10", "6x10", "7x10", "8x9", "9x8", "10x7", "10x6", "10x5", "10x4", "9x3", "8x2", "7x1", "6x1"], 24],
            [["8x1", "7x2", "6x3", "5x4", "4x5", "3x6", "2x7", "1x8", "1x9", "1x10", "1x11", "1x12", "2x13", "3x14", "4x15", "5x15", "6x15", "7x15", "8x15", "9x15", "10x14", "11x13", "12x12", "13x11", "14x10", "15x9", "15x8", "15x7", "14x6", "13x5", "12x4", "11x3", "10x2", "9x1"], 34]
        ]
    ]

    def print_list(list):
        for linha in list:
            print(linha)

    def create_board(formato,dificuldade,size, indice):
        suture_board = []

        for i in range(size):
            list = []
            for j in range(size):
                if (f"{i+1}x{j+1}" in positions[indice][dificuldade-1][0]) and formato == "X":
                    list.append("X")
                elif (f"{i+1}x{j+1}" in positions[indice][dificuldade-1][0]) and formato == "O":
                    list.append("O")
                else:
                    list.append(".")
            suture_board.append(list)
        return suture_board

    def game():

        formato = input("Qual formato deseja? (X/O)?\n->").strip().upper()
        if formato == "X":
            indice = 0
        else:
            indice = 1
        dificuldade = int(input("\nQual dificuldade deseja escolher?\n\n1 - Fácil\n2 - Médio\n3 - Difícil\n\n->"))

        size = calc_size(dificuldade)

        print()
        print("\nVamos iniciar o exercício. Com base no formato apresentado, digite a Coordenada do mapa que você deve colocar os pontos.")
        for i in range(size):
            print(["." for _ in range(size)])

        print(positions[indice][dificuldade-1][0])
        respostas = []
        for i in range(positions[indice][dificuldade][1]):
            resp = input("Digite uma coordenada que você deve colocar um ponto:\n(NúmeroDaLinhaxNúmeroDaColuna)\n->")

            if resp in respostas:
                print("\nCORRETO! Porém você já digitou essa resposta anteriormente...\n")
            elif resp in positions[indice][dificuldade-1][0]:
                print("\nCORRETO!\n")
                respostas.append(resp)
            else:
                print("\nCoordenada errada.\n")

        suture_board = create_board(formato,dificuldade,size, indice)
        print("\nExercício finalizado, o local dos pontos é o seguinte:")
        print_list(suture_board)

    game()

def menu():
    opcao = input("Deseja jogar utilizando:\n1 - Dicionarios\n2 - Listas\n\n->")
    if opcao == "1":
        dicionarios()
    elif opcao == "2":
        listas()
    else:
        print("Opção inválida")

menu()