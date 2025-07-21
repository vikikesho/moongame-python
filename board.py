from card import Card
import numpy as np

class Node:
    def __init__(self, name) -> None:
        self.name = name
        self.card = None
        self.owner = None
        self.neighbors = []
        pass

    def __str__(self) -> str:
        return "Node({name}, {card}, {player})".format(name = self.name, card = self.card, player = self.owner)

    def addNeighbors(self, n):
        self.neighbors.append(n)

    def addCard(self, card):
        if not isinstance(card, Card):
            return False

        if self.card == None:
            self.card = card
            return True
        else:
            return False

    def changeOwner(self, owner):
        self.owner = owner

def connectNode(a, b):
    if b in a.neighbors:
        a.neighbors.append(b)
    if a in b.neighbors:
        b.neighbors.append(a)

def connectNodes(a, nList):
    for i in nList:
        a.connectNode(i)

def findPhaseNeighbor(startNode: Node, descending):
    foundPhaseNeighbor = False
    cycle = [startNode]
    cycleList = []

    for adjNode in startNode.neighbors:
        if adjNode.card != None:
            if descending == True:
                if adjNode.card.value == (startNode.card.value - 1) % 8:
                    foundPhaseNeighbor = True
                    neighborsOfAdjNode = findPhaseNeighbor(adjNode, descending)
                    for s in neighborsOfAdjNode:
                        s.extend(cycle)
                        cycleList.append(s)
            else:
                if adjNode.card.value == (startNode.card.value + 1) % 8:
                    foundPhaseNeighbor = True
                    neighborsOfAdjNode = findPhaseNeighbor(adjNode, descending)
                    for s in neighborsOfAdjNode:
                        a = cycle[:]
                        a.extend(s)
                        cycleList.append(a)
                    
    if not foundPhaseNeighbor:
        cycleList.append(cycle)
    
    return cycleList

class Board:
    def __init__(self, adjMat) -> None:
        self.nodeList = []
        for i in range(9):
            self.nodeList.append(Node(i))

        size = np.shape(adjMat)[0]

        for col in range(size):
            for i in range(size):
                if adjMat[col][i] == 1:
                    self.nodeList[col].addNeighbors(self.nodeList[i])
        pass

    def isFull(self):
        for i in self.nodeList:
            if i.card == None:
                return False

        return True