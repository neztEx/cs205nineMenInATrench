#game definitions
import array
import random

class Game:
    
    def __init__(self, option):
        self.rows = 2
        self.cols = 10
        self.puzzle = self.puzzle(option)
        self.solution = self.solution()

    def printGame(self):
        for i in self.puzzle:
            for j in i:
                print(j, end = " ")
            print()
        return

    def solution(self):
        solution = [[0 for i in range(self.cols)] for j in range(self.rows)] #inner loop = cols and outter loop = rows
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
        return solution
    
    def puzzle(self, option):
        puzzle = [[0 for i in range(self.cols)] for j in range(self.rows)] #inner loop = cols and outter loop = rows
        if option == 1:
            puzzle[1][0] = 1
            puzzle[1][1] = 2
            puzzle[1][2] = 3
            puzzle[1][3] = 4
            puzzle[1][4] = 5
            puzzle[1][5] = 6
            puzzle[1][6] = 7
            puzzle[1][7] = 8
            puzzle[1][8] = 0
            puzzle[1][9] = 9
        elif option == 2:
            puzzle[1][0] = 1
            puzzle[1][1] = 2
            puzzle[1][2] = 3
            puzzle[1][3] = 4
            puzzle[1][4] = 5
            puzzle[1][5] = 6
            puzzle[1][6] = 7
            puzzle[1][7] = 0
            puzzle[1][8] = 8
            puzzle[1][9] = 9
        elif option == 3:
            puzzle[1][0] = 1
            puzzle[1][1] = 2
            puzzle[1][2] = 3
            puzzle[1][3] = 4
            puzzle[1][4] = 5
            puzzle[1][5] = 6
            puzzle[1][6] = 0
            puzzle[1][7] = 7
            puzzle[1][8] = 8
            puzzle[1][9] = 9
        elif option == 4:
            puzzle[1][0] = 1
            puzzle[1][1] = 2
            puzzle[1][2] = 3
            puzzle[1][3] = 4
            puzzle[1][4] = 5
            puzzle[1][5] = 6
            puzzle[1][6] = 0
            puzzle[1][7] = 0
            puzzle[1][8] = 8
            puzzle[1][9] = 9
            puzzle[0][7] = 7
        elif option == 5:
            puzzle[1][0] = 0
            puzzle[1][1] = 2
            puzzle[1][2] = 3
            puzzle[1][3] = 0
            puzzle[1][4] = 4
            puzzle[1][5] = 5
            puzzle[1][6] = 6
            puzzle[1][7] = 7
            puzzle[1][8] = 8
            puzzle[1][9] = 9
            puzzle[0][3] = 1
        else:   
            print("Default Puzzle")     
            puzzle[1][0] = 0
            puzzle[1][1] = 2
            puzzle[1][2] = 3
            puzzle[1][3] = 4
            puzzle[1][4] = 5
            puzzle[1][5] = 6
            puzzle[1][6] = 7
            puzzle[1][7] = 8
            puzzle[1][8] = 9
            puzzle[1][9] = 1
        return puzzle

    def random(self):
        gameSizeNine = [1,2,3,4,5,6,7,8,9,0]

        values = random.sample(gameSizeNine, len(gameSizeNine))

        self.puzzle = [[0 for i in range(self.cols)] for j in range(self.rows)]
        for i in range(len(gameSizeNine)):
            self.puzzle[1][i] = values.pop()
        return