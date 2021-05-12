#start of project
import os
import time
from search import *
from ninePuzzle import *

def outputGame(puzzle):
        for i in puzzle:
            for j in i:
                print(j, end = " ")
            print()
        return     

def gameSearch(puzzle):
    while True:
        # try:
            choice = int(input("Enter your choice of algorithm:\n1) Uniform Cost Search\n2) A* with the Misplaced Tile heuristic\n3) A* with the Euclidean distance heuristic\n4) A* with the Manhattan Sergeant distance heuristic\n"))

            if choice == 1:
                print("1 Selected")
                start = time.perf_counter()
                results,level, maxQueue = search(puzzle, False, False, False)
                finish = time.perf_counter()
                outputGame(results)
                print(f"Time of completion: {finish-start:0.4f}s")
                print(f"Number of nodes expanded: {level}")
                print(f"Max number of nodes in queue: {maxQueue}")
                input("Press Enter to continue...")
                break
            elif choice == 2:
                print("2 Selected")
                start = time.perf_counter()
                results, level, maxQueue = search(puzzle, True, False, False)                
                finish = time.perf_counter()
                outputGame(results)
                print(f"Time of completion: {finish-start:0.4f}s")
                print(f"Number of nodes expanded: {level}")
                print(f"Max number of nodes in queue: {maxQueue}")
                input("Press Enter to continue...")
                break
            elif choice == 3:
                print("3 Selected")
                start = time.perf_counter()
                results,level, maxQueue = search(puzzle, False, True, False)                
                finish = time.perf_counter()
                outputGame(results)
                print(f"Time of completion: {finish-start:0.4f}s")
                print(f"Number of nodes expanded: {level}")
                print(f"Max number of nodes in queue: {maxQueue}")
                input("Press Enter to continue...")
                break
            elif choice == 4:
                print("4 Selected")
                start = time.perf_counter()
                results,level, maxQueue = search(puzzle, False, False, True)                
                finish = time.perf_counter()
                outputGame(results)
                print(f"Time of completion: {finish-start:0.4f}s")
                print(f"Number of nodes expanded: {level}")
                print(f"Max number of nodes in queue: {maxQueue}")
                input("Press Enter to continue...")
                break
        # except:
        #     print("Invalid choice!")
    return

if __name__ == '__main__':
    while True:
        # try:2
        
            # os.system('cls' if os.name == 'nt' else 'clear' )
            choice = int(input("Welcome to Samuel Tapia 862097969 8 puzzle solver. \nType “1” to use a random puzzle, or “2” to use a default puzzle.\n"))
            
            if choice == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("-----Random Puzzle Generated-----")
                p = Game(1)
                p.random()
                p.printGame()
                gameSearch(p.puzzle)
            elif choice == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("-----Select Puzzle Generated-----")
                option = int(input("Select difficulty\n1)Very Easy\n2)Easier\n3)Easy\n4)MedEasy\n5)Medium\n6)Hard\n"))
                p = Game(option)
                p.printGame()
                gameSearch(p.puzzle)
            else:  
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Invalid option!")

        # except:
        #     os.system('cls' if os.name == 'nt' else 'clear')
        #     print("Invalid input!\n")