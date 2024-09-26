import random

#-------------------------------------------Jogador X Jogador------------------------------------------------------------

class JogadorXJogador:
    #definindo as variaveis self
    def __init__(self):
        self.nome1 = None
        self.nome2 = None
        self.jogada1 = None
        self.jogada2 = None
        self.placar01 = []
        self.placar02 = []

    #inicio p pegar os nomes
    def inicio(self):
        self.nome1 = input("Digite o nome do primeiro jogador: ")
        self.nome2 = input("Digite o nome do segundo jogador: ")
        jogar = True

        #loopzao
        while jogar:
            self.jogada1 = input(f"{self.nome1} - escolha sua jogada (pedra, papel ou tesoura): ").lower()
            self.jogada2 = input(f"{self.nome2} - escolha sua jogada (pedra, papel ou tesoura): ").lower()

            if self.jogada1 not in ["pedra", "papel", "tesoura"] or self.jogada2 not in ["pedra", "papel", "tesoura"]:
                print("Jogada inválida! Por favor, escolha entre 'pedra', 'papel' ou 'tesoura'.")
                continue

            if (self.jogada1 == "pedra" and self.jogada2 == "tesoura") or \
               (self.jogada1 == "papel" and self.jogada2 == "pedra") or \
               (self.jogada1 == "tesoura" and self.jogada2 == "papel"):
                print(f"\n{self.nome1} escolheu: {self.jogada1} | {self.nome2} escolheu: {self.jogada2}")
                print(f"\n{self.nome1} VENCEU!!")
                self.placar01.append(1)
            elif self.jogada1 == self.jogada2:
                print(f"\n{self.nome1} escolheu: {self.jogada1} | {self.nome2} escolheu: {self.jogada2}")
                print("\nEmpate!!")
            else:
                print(f"\n{self.nome1} escolheu: {self.jogada1} | {self.nome2} escolheu: {self.jogada2}")
                print(f"\n{self.nome2} VENCEU!!")
                self.placar02.append(1)

            jogar = self.novamente()

        self.exibir_placar()

    #se o jogador quiser jogar d novo
    def novamente(self):
        while True:
            escolha = input("\nDeseja jogar novamente? (sim | nao): ").strip().lower()
            if escolha == "sim":
                return True
            elif escolha == "nao":
                return False
            else:
                print("Resposta inválida. Por favor, responda com 'sim' ou 'nao'.")

    #mostrando o placar
    def exibir_placar(self):
        print(f"\n{self.nome1} ficou com {len(self.placar01)} pontos!")
        print(f"\n{self.nome2} ficou com {len(self.placar02)} pontos!")
        print(f"\nObrigado por jogar Jokenpo, voltem sempre {self.nome1} e {self.nome2}!!")

#-------------------------------------------Jogador X PC------------------------------------------------------------

class JogadorXPC:

    #definindo as variaveis self
    def __init__(self):
        self.nome1 = None
        self.nome2 = None
        self.jogada1 = None
        self.jogada2 = None
        self.placar01 = []
        self.placar02 = []

    #inicio p pegar os nomes
    def inicio(self):
        self.nome1 = input("Digite o nome do jogador: ")
        jogar = True

        #loopzao
        while jogar:
            self.jogada1 = input(f"{self.nome1} - escolha sua jogada (pedra, papel ou tesoura): ").lower()
            self.jogada2 = random.choice(["pedra", "papel", "tesoura"])

            if self.jogada1 not in ["pedra", "papel", "tesoura"]:
                print("Jogada inválida! Por favor, escolha entre 'pedra', 'papel' ou 'tesoura'.")
                continue

            if (self.jogada1 == "pedra" and self.jogada2 == "tesoura") or \
               (self.jogada1 == "papel" and self.jogada2 == "pedra") or \
               (self.jogada1 == "tesoura" and self.jogada2 == "papel"):
                print(f"\n{self.nome1} escolheu: {self.jogada1} | PC escolheu: {self.jogada2}")
                print(f"\n{self.nome1} VENCEU!!")
                self.placar01.append(1)
            elif self.jogada1 == self.jogada2:
                print(f"\n{self.nome1} escolheu: {self.jogada1} | PC escolheu: {self.jogada2}")
                print("\nEmpate!!")
            else:
                print(f"\n{self.nome1} escolheu: {self.jogada1} | PC escolheu: {self.jogada2}")
                print("\nPC VENCEU!!")
                self.placar02.append(1)

            jogar = self.novamente()

        self.exibir_placar()

    #se o jogador quiser jogar d novo
    def novamente(self):
        while True:
            escolha = input("\nDeseja jogar novamente? (sim | nao): ").strip().lower()
            if escolha == "sim":
                return True
            elif escolha == "nao":
                return False
            else:
                print("Resposta inválida. Por favor, responda com 'sim' ou 'nao'.")

    #mostrando o placar
    def exibir_placar(self):
        print(f"\n{self.nome1} ficou com {len(self.placar01)} pontos!")
        print(f"\nPC ficou com {len(self.placar02)} pontos!")
        print(f"\nObrigado por jogar Jokenpo, voltem sempre {self.nome1} e PC!!")

#-------------------------------------------PC X PC------------------------------------------------------------

class PCxPC:
    #definindo as variaveis self
    def __init__(self):
        self.nome1 = None
        self.nome2 = None
        self.jogada1 = None
        self.jogada2 = None
        self.placar01 = []
        self.placar02 = []

    #inicio p pegar os nomes
    def inicio(self):
        self.nome1 = input("Digite o nome do primeiro PC: ")
        self.nome2 = input("Digite o nome do segundo PC: ")
        jogar = True

        #loopzao
        while jogar:
            self.jogada1 = random.choice(["pedra", "papel", "tesoura"])
            self.jogada2 = random.choice(["pedra", "papel", "tesoura"])

            if (self.jogada1 == "pedra" and self.jogada2 == "tesoura") or \
               (self.jogada1 == "papel" and self.jogada2 == "pedra") or \
               (self.jogada1 == "tesoura" and self.jogada2 == "papel"):
                print(f"\n{self.nome1} escolheu: {self.jogada1} | {self.nome2} escolheu: {self.jogada2}")
                print(f"\n{self.nome1} VENCEU!!")
                self.placar01.append(1)
            elif self.jogada1 == self.jogada2:
                print(f"\n{self.nome1} escolheu: {self.jogada1} | {self.nome2} escolheu: {self.jogada2}")
                print("\nEmpate!!")
            else:
                print(f"\n{self.nome1} escolheu: {self.jogada1} | {self.nome2} escolheu: {self.jogada2}")
                print(f"\n{self.nome2} VENCEU!!")
                self.placar02.append(1)

            jogar = self.novamente()

        self.exibir_placar()

    #se o jogador quiser jogar d novo
    def novamente(self):
        while True:
            escolha = input("\nDeseja jogar novamente? (sim | nao): ").strip().lower()
            if escolha == "sim":
                return True
            elif escolha == "nao":
                return False
            else:
                print("Resposta inválida. Por favor, responda com 'sim' ou 'nao'.")

    #mostrando o placar
    def exibir_placar(self):
        print(f"\n{self.nome1} ficou com {len(self.placar01)} pontos!")
        print(f"\n{self.nome2} ficou com {len(self.placar02)} pontos!")
        print(f"\nObrigado por jogar Jokenpo, voltem sempre {self.nome1} e {self.nome2}!!")

def main():
    
    #escolher modo jogo
    try:
        escolha = int(input("Escolha o modo de jogo (1 - Jogador vs Jogador | 2 - Jogador vs PC | 3 - PC vs PC): "))
    except ValueError:
        print("Entrada inválida! Por favor, insira um número entre 1 e 3.")
        return

    #tipos de modo de jogo (alternativas)
    if escolha == 1:
        jogo = JogadorXJogador()
        jogo.inicio()
    elif escolha == 2:
        jogo = JogadorXPC()
        jogo.inicio()
    elif escolha == 3:
        jogo = PCxPC()
        jogo.inicio()
    else:
        print("Número inválido!")

#chamando a funcao main
if __name__ == "__main__":
    main()