from queue import PriorityQueue
# from gameSetup import * 
import numpy as np
import copy
import heapq
import math

#solution
rows = 2
cols = 10

solution = [[0 for i in range(cols)] for j in range(rows)] #inner loop = cols and outter loop = rows
solution[1][0] = 1
solution[1][1] = 2
solution[1][2] = 3
solution[1][3] = 4
solution[1][4] = 5
solution[1][5] = 6
solution[1][6] = 7
solution[1][7] = 8
solution[1][8] = 9
solution[1][9] = 0

#GLOBAL VARIABLES
#level is g(n) the cost to reach the node from the start
LEVEL = 0

class Node:

    def __init__(self, cost1, gameState1, level):
        self.cost = cost1
        self.state = gameState1
        self.euclidean = 0 #distance h(n)
        self.level = level #distance g(n)
        self.hash = self.getKey()
    
    def getKey(self):
        # temp = [[str(self.state[i][j]) for j in range(cols)] for i in range(rows)]
        result = "".join(["".join(str(self.state[0])),"".join(str(self.state[1]))])
        return result
    

def childNodes(gameState, misplaced, euclidean, currLevel, manhattan):
    #creating child nodes from parent to add the search graph
    
    #find current position of blank space
    # x,y = findBlank(gameState)
    
    #gamestate
    #0000000000
    #0234567891
    #blanks = (1,0), (0,3), (0,5), (0,7)
    blanks = findBlank(gameState)

    #actions are for current x,y position ["UP","DOWN","LEFT","RIGHT"]
    #example if x,y = [1,1] then th UP = 1,0...etc 
    childNodes = []
    
    for j in blanks:
        actions = [[j[0],j[1]-1],[j[0],j[1]+1],[j[0]-1,j[1]],[j[0]+1,j[1]]]
        for i in actions:
            child = move(gameState, j[0], j[1], i[0], i[1]) #return changed gameState
            if child is not None:
                if misplaced:
                    eDistance = misplacedTile(gameState)
                    child_node = Node(0, child, currLevel)
                    child_node.euclidean = eDistance
                    child_node.level = currLevel + 1
                    child_node.cost = child_node.level + eDistance
                elif euclidean:
                    eDistance = euclideanDistance(gameState)
                    child_node = Node(0, child, currLevel)
                    child_node.euclidean = eDistance
                    child_node.level = currLevel + 1
                    child_node.cost = child_node.level + eDistance
                elif manhattan:
                    eDistance = manhattanDistanceSergeant(gameState)
                    child_node = Node(0, child, currLevel)
                    child_node.euclidean = eDistance
                    child_node.level = currLevel + 1
                    child_node.cost = child_node.level + eDistance
                else:
                    child_node = Node(0, child, currLevel)
                    child_node.level += 1
                    child_node.cost = child_node.level
                childNodes.append(child_node)

    return childNodes

def move(gameState, xCur, yCur, xMove, yMove):
    #checks to see if the actions to move blank space are possible range is 0 to len(gameState)
    state = copy.deepcopy(gameState)
    
    notPossible = [0,1,2,4,6,8,9]

    if yMove >= 0 and yMove < len(state[0]) and xMove >= 0 and xMove < len(state):
        if xMove == 0 and yMove in notPossible:
            return None
        tempState = state #copies current state of game
        tempVal = tempState[xMove][yMove] #assigns value of the move position to temp
        tempState[xMove][yMove] = state[xCur][yCur] #move blank space to move state
        tempState[xCur][yCur] = tempVal
        return tempState
    else:
        return None

def findBlank(gameState):
    #returns a list current position(s) of blank tiles
    blankTiles = []
    for i in range(cols):
        if gameState[1][i] == 0:
            blankTiles.append([1,i])
    if gameState[0][3] == 0:
        blankTiles.append([0,3])
    if gameState[0][5] == 0:
        blankTiles.append([0,5])
    if gameState[0][7] == 0:
        blankTiles.append([0,7])
    
    return blankTiles

def goalTest(gameState):
    #returns true or false if currentState is the goalState
    # for i in range(rows):
    #     for j in range(cols):
    #         if gameState[i][j] != gameState.solution[i][j]:
    #             return False

    for i in range(len(gameState[0])-1):
        if gameState[0][i] != 0:
            return False
        if gameState[1][i] != i+1:
            return False
    return True

def takeFirst(elem):
    return elem[0]

def search(game, misplaced, euclidean, manhattan):
    print("Starting search...")
    global LEVEL
    maxQueue = 0
    LEVEL = 0
    node = Node(0, game, 0)
    
    frontier = dict()
    frontier[node.hash] = node

    explored = set()
    while True:
        if len(frontier) == 0:
            print("FAILED")
            return game, LEVEL, maxQueue
        if len(frontier) > maxQueue:
            maxQueue = len(frontier)

        # currNode = list(sortDict.values())[0] #gives first value of dict
        # currNode = sortDict[0][1] #gives first value of dict

        ### -------dict Queue----------
        currNode = list(frontier.values())[0]
        for key in frontier.items():
             if key[1].cost < currNode.cost:
                 currNode = key[1]
        frontier.pop(currNode.hash, None)

        LEVEL += 1
        printExpand(currNode.cost, currNode.state, currNode.euclidean, currNode.level)
        results = goalTest(currNode.state)
        if results:
            print("solution found!")
            return currNode.state, LEVEL, maxQueue
        explored.add(currNode.hash)
        state = copy.deepcopy(currNode.state)
        currLevel = copy.deepcopy(currNode.level)
        listChilds = childNodes(state, misplaced, euclidean, currLevel, manhattan)
        for i in listChilds:
            if i.hash in explored:
                continue
            if i.hash not in explored and i.hash not in frontier:
                frontier[i.hash] = i
            elif i.hash in frontier and i.cost < frontier[i.hash].cost:
                # frontier.pop(frontier.index((i.cost,i.state)))
                frontier.pop(i.hash,None)
                frontier[i.hash] = i
            # frontier.sort(key=takeFirst)
            # dict(sorted(frontier.items(), key=lambda item: item[cost]))

def manhattanDistance(game):
    #calculates h(n) value for currentState
    nodeCost = 0
    for i in range(rows):
        for j in range(cols):
            tempi = i
            tempj = j
            correctValue = game[i][j]-1
            correctRow = solution[correctValue][0]
            correctCol = solution[correctValue][1]
            # print(f"Current: [{tempi},{tempj}] -> [{correctRow},{correctCol}]")
            while(tempi != correctRow):
                if(tempi < correctRow):
                    tempi += 1
                    nodeCost += 1
                    # print(tempi)
                else:
                    tempi -= 1
                    nodeCost += 1
                    # print(tempi)
            while(tempj != correctCol):
                if(tempj < correctCol):
                    tempj += 1
                    nodeCost += 1
                    # print(tempj)
                else:
                    tempj -= 1
                    nodeCost += 1
                    # print(tempj)
            # print(nodeCost)
                    
    return nodeCost

def misplacedTile(gameState):
    #returns h(n) counts number of misplaced tiles
    count = 0
    for i in range(len(gameState[0])-1):
        if gameState[1][i] != i+1:
            count += 1
    # if gameState[1][9] != 0:
    #     count += 1
    # if gameState[0][3] != 0:
    #     count += 1
    # if gameState[0][5] != 0:
    #     count += 1
    # if gameState[0][7] != 0:
    #     count += 1
    return count

def euclideanDistance(gameState):
    #returns h(n) counts number of euclidean distance
    x1np = np.array(gameState)
    # print(x1np)
    x2np = np.array(solution)
    # print(x2np)
    sumDistance = 0
    for i in range(rows):
        for j in range(cols):
            if(x1np[i][j] == 0):
                continue
            # print(x1np[i][j])
            goalPosition = np.where(x2np == x1np[i][j])
            # print(goalPosition[0][0],goalPosition[1][0])
            x2 = goalPosition[0][0]
            y2 = goalPosition[1][0]
            xVal = (i - x2)**2 #x1 - x2
            yVal = (j - y2)**2 #y1 - y2
            sumDistance += math.sqrt(xVal + yVal)
    # eDistance = math.sqrt(sumDistance)
    return sumDistance

def euclideanDistanceSergeant(gameState):
    #returns h(n) counts number of euclidean distance
    x1np = np.array(gameState)
    sumDistance = 0
    currentPosition = np.where(x1np == 1) #returns tuple location
    x2 = currentPosition[0][0]
    y2 = currentPosition[1][0]
    xVal = (1 - x2)**2 #x1 - x2
    yVal = (0 - y2)**2 #y1 - y2
    sumDistance += math.sqrt(xVal + yVal)
    # eDistance = math.sqrt(sumDistance)
    return sumDistance

def manhattanDistanceSergeant(gameState):
    #calculates h(n) value for currentState
    # x1np = np.array(gameState)
    # x2np = np.array(solution)
    sumDistance = 0
    # curPosition = np.where(x1np == 1)
    for i in range(rows):
        for j in range(cols):
            if gameState[i][j] == 1:
                x = i
                y = j
                break
    # print(goalPosition[0][0],goalPosition[1][0])
    # x2 = curPosition[0][0]
    # y2 = curPosition[1][0]
    if(x == 0):
        sumDistance += 1
    # yVal = abs(0 - y2)
    sumDistance += abs(0-y)
# eDistance = math.sqrt(sumDistance)
    return sumDistance

def manhattanDistance(gameState):
    #calculates h(n) value for currentState
    x1np = np.array(gameState)
    sumDistance = 0
    for i in range(1,cols):
        currentPosition = np.where(x1np == i) #returns tuple location
        x2 = currentPosition[0][0]
        y2 = currentPosition[1][0]
        if (x2 == 0):
            sumDistance += 1
        sumDistance = sumDistance + y2 - i  
    # sumDistance += math.sqrt(xVal + yVal)

def printExpand(gameCost, gameState, hn, level):
    if hn > 0:
        print(f"The best state to expand with f(n)={gameCost} h(n)={hn} + g(n)={level}")
        for i in gameState:
            for j in i:
                print(j, end = " ")
            print()
    else:
        print(f"The best state to expand with f(n)={gameCost} h(n)=0 + g(n)={level}")
        for i in gameState:
            for j in i:
                print(j, end = " ")
            print()