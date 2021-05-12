# cs205nineMenInATrench
The program allows you select from a set of pre-define puzzles of Nine Men In A Trench and allows the user to select to how to solve each puzzle using different search algorithms.

# How to Run
```python3 main.py```


## Demo 

```
Welcome to Samuel Tapia Nine Men In A Trench. 
Type “1” to use a random puzzle, or “2” to use a default puzzle.

-----Select Puzzle Generated-----
Select difficulty
1)Very Easy
2)Easier
3)Easy
4)MedEasy
5)Medium
6)Hard


0 0 0 0 0 0 0 0 0 0 
1 2 3 4 5 6 7 8 0 9

Enter your choice of algorithm:
1) Uniform Cost Search
2) A* with the Misplaced Tile heuristic
3) A* with the Euclidean distance heuristic

Starting search...
The best state to expand with f(n)=0 h(n)=0 + g(n)=0
0 0 0 0 0 0 0 0 0 0 
1 2 3 4 5 6 7 8 0 9 
The best state to expand with f(n)=1 h(n)=0 + g(n)=1
0 0 0 0 0 0 0 0 0 0 
1 2 3 4 5 6 7 0 8 9 
The best state to expand with f(n)=1 h(n)=0 + g(n)=1
0 0 0 0 0 0 0 0 0 0 
1 2 3 4 5 6 7 8 9 0 
solution found!
0 0 0 0 0 0 0 0 0 0 
1 2 3 4 5 6 7 8 9 0 
Time of completion: 0.0008s
Number of nodes expanded: 3
Max number of nodes in queue: 7
```