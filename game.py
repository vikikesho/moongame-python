import random as rd

from board import findPhaseNeighbor
from card import Card

class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.score = 0
        self.hand = []
        self.nextPlayer = None
        pass

    def __str__(self) -> str:
        return self.name

class Game:
    def __init__(self, board) -> None:
        self.deck = []
        self.currentPlayer = None
        self.board = board
        pass

    def drawCard(self, player, n):
        for i in range(n):
            player.hand.append(self.deck.pop())

    def renewDeck(self, seed=None):
        rd.seed(seed)

        self.deck.clear()
        for i in range(8):
            self.deck.extend([Card(i), Card(i)])

        rd.shuffle(self.deck)

    def checkScoring(self, node):
        for i in node.neighbors:
            if i.card != None:
                if abs(i.card.value - node.card.value) == 4:
                    self.currentPlayer.score += 2
                    print("{player} gains 2 points for a full moon.".format(player=self.currentPlayer))

                    node.changeOwner(self.currentPlayer)
                    i.changeOwner(self.currentPlayer)

                if i.card.value == node.card.value:
                    self.currentPlayer.score += 1
                    print("{player} gains 1 points for matching phase.".format(player=self.currentPlayer))

                    node.changeOwner(self.currentPlayer)
                    i.changeOwner(self.currentPlayer)

        dList = findPhaseNeighbor(node, descending=True)
        aList = findPhaseNeighbor(node, descending=False)

        for dCycle in dList:
            for aCycle in aList:
                cycle = dCycle[:]
                cycle.extend(aCycle[1:])
                if len(cycle) >= 3:
                    self.currentPlayer.score += len(cycle)
                    print("{player} gains {score} points for a {score}-cycle.".format(player=self.currentPlayer, score=len(cycle)))

                    for i in cycle:
                        i.changeOwner(self.currentPlayer)

    def runGame(self):
        self.renewDeck()

        player1 = Player("Player 1")
        player2 = Player("Player 2")

        player1.nextPlayer = player2
        player2.nextPlayer = player1
        
        self.currentPlayer = player1

        self.drawCard(player1, 3)
        self.drawCard(player2, 3)

        while not self.board.isFull():
            if len(self.currentPlayer.hand) < 3:
                self.drawCard(self.currentPlayer, 1)

            print("{player}'s turn. {score} points.".format(player=self.currentPlayer, score=self.currentPlayer.score))
            for i in self.currentPlayer.hand:
                print(i)

            cardChoice = None

            while cardChoice == None:
                card = int(input("Enter a card:"))

                for i in self.currentPlayer.hand:
                    if i.value == card:
                        cardChoice = i
                        self.currentPlayer.hand.remove(i)
                        break

                if cardChoice != None:
                    break
                else:
                    print("You don't have this card.")

            while True:
                pos = int(input("Enter a position:"))

                if self.board.nodeList[pos].addCard(cardChoice):
                    self.checkScoring(self.board.nodeList[pos])
                    break
                else:
                    print("The cell is occupied.")

            for i in self.board.nodeList:
                print(i)

            self.currentPlayer = self.currentPlayer.nextPlayer

        for i in self.board.nodeList:
            if i.owner != None:
                i.owner.score += 1

        print(player1.score)
        print(player2.score)
