class Game:
    totalGames = 0

    def __init__(self, name="", yearLaunch=0, multiplayer=0, note=0):
        self.name = name
        self.yearLaunch = yearLaunch
        self.multiplayer = multiplayer
        self.note = note
        self.totalEvaluation = 0
        Game.totalGames += 1

    def __str__(self):
        return f"Game: {self.name}"
    
    def technical_sheet(self):
        print("-=(Dados do jogo)=-")
        print(f"Nome do jogo: {self.name}")
        print(f"Ano de lançamento: {self.yearLaunch}")
        print(f"Modo multiplayer: {self.multiplayer}")
        print(f"Nota do jogo: {self.note}\n")

    def evaluate(self, note):
        self.totalEvaluation += note
        self.evaluators += 1

    def average(self):
        print(f"Média do jogo {self.name}: {self.totalEvaluation / self.evaluators}")

game1 = Game("The Legend of Zelda", 2017, False, 9.5)
game2 = Game("Fortnite", 2017, True, 8.0)
game3 = Game("Red Dead Redemption", 2018, False, 10.0)

game1.technical_sheet()
game2.technical_sheet()
game1.evaluate(10)
game1.evaluate(2)
game1.evaluate(5)
game1.average()

print(f"Total de jogos criados: {Game.totalGames}")