# 8-Puzzle
Artificially Intelligent system for solving 8-puzzle board game.


This project was originally provided as a class assignment, then later optimized after better understanding of data structures and algorithms. The assignment required the intelligent system to provide a set of moves to move from an initial state to a goal state, or inform the user that it is not possible.

Four types of algorithms are used to find the proper sequence:
- Greedy-Breadth-First-Search (Misplaced)
- Greedy-Breadth-First-Search (Manhattan)
- A* Misplaced Search
- A* Manhattan Search

Each of the four types of algorithms use a variation of heuristics or combination of heuristics to help determine the next state to analyze for finding the sequence to the goal state.

- Misplaced:  Amount of numbers that are out of place
- Manhattan:  Sum of the total movements to get into goal position place for all numbers.

The AI may confirm if the puzzle is solvable given an initial and final state.
The system also returns a sequence of moves to make to change from the initial state to the goal state.

