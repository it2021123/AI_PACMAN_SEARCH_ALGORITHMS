Pacman Search Algorithms(run in python  3.6)



This repository contains implementations of various search algorithms applied to the game Pacman. The project is divided into three main files, each responsible for different aspects of the game and search strategies.
Files and Implementations
1. search.py

In this file, we implemented search agents that utilize different search algorithms to navigate Pacman through the maze without considering the presence of ghosts (opponents). The algorithms implemented are:

   Depth-First Search (DFS): A search algorithm that explores as far as possible along each branch before backtracking.

    python pacman.py -l tinyMaze -p SearchAgent -a fn=dfs
    python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs
    python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=dfs

Breadth-First Search (BFS): A search algorithm that explores all of the neighbor nodes at the present depth before moving on to the nodes at the next depth level.

    python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
    python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=bfs

Uniform Cost Search (UCS): A search algorithm that expands the least cost node first.

    python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
     python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
    python pacman.py -l mediumScaryMaze -p StayWestSearchAgent

A Search*: An informed search algorithm that uses both path cost and a heuristic to determine the order of node expansion.


    python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic

2. multiAgents.py

This file contains implementations of multi-agent search algorithms, where Pacman has to navigate the maze while considering the presence of ghosts (opponents). The algorithms implemented are:

    Minimax Algorithm: A decision rule for minimizing the possible loss for a worst-case scenario.


python autograder.py -q q6

Alpha-Beta Pruning: An optimization technique for the minimax algorithm that reduces the number of nodes evaluated by the minimax algorithm in its search tree. 

     python pacman.py -p MinimaxAgent -l trappedClassic -a depth=3
    python autograder.py -q q7

Expectimax Algorithm: A variant of the minimax algorithm which deals with probabilistic events by averaging the expected utility.



    python autograder.py -q q8
    python pacman.py -p ExpectimaxAgent -l minimaxClassic -a depth=3
    python pacman.py -p AlphaBetaAgent -l trappedClassic -a depth=3 -q -n 10
    python pacman.py -p ExpectimaxAgent -l trappedClassic -a depth=3 -q -n 10

In this project, we implemented an enhanced evaluation function named betterEvaluationFunction to evaluate game states. This function aims to improve the performance of the Pacman agent, particularly in the smallClassic maze with one ghost. The goal is for the agent to win more than half of the games in a depth-2 search.
Evaluation Criteria

The performance of the agent is evaluated based on the following criteria:

    Winning Games:
        If the agent wins at least once, you receive 1 point.
        If the agent wins 5 times, you receive an additional 1 point.
        If the agent wins all 10 times, you receive an additional 2 points.

    Average Score:
        If the agent's average score is at least 500, you receive 1 point.
        If the agent's average score is at least 1000, you receive 2 points.

    Execution Time:
        If the games take less than 30 seconds (with the --no-graphics option), you receive 1 point.

Running the Evaluation

To evaluate the performance of your betterEvaluationFunction, you can use the following commands:
With Graphics

     python autograder.py -q q9 
     python pacman.py -p AlphaBetaAgent -a evalFn=better,depth=2 -l smallClassic -k 2


Without Graphics

	python autograder.py -q q9 --no-graphics


Implementation

The betterEvaluationFunction should evaluate game states based on various factors such as:

    Pacman's distance to the nearest food: Encourage Pacman to move towards the nearest food.
    Pacman's distance to ghosts: Encourage Pacman to avoid ghosts, especially when they are in a dangerous state.
    Number of remaining food pellets: Encourage Pacman to eat all the food pellets.
    Number of power pellets: Encourage Pacman to eat power pellets when necessary.

3. searchAgent.py

This file includes the implementation of a utility function used for evaluating game states. This evaluation function helps to guide the search algorithms by scoring the desirability of a game state, influencing the decisions made by the algorithms.
Usage:

  
	 python pacman.py -l trickySearch -p AStarFoodSearchAgent


To run the algorithms, you can execute the respective Python files. The implementations can be tested and executed within the context of the Pacman game environment provided in this repository. Detailed instructions on running the game and algorithms can be found in the project documentation.
Conclusion

This project showcases the application of various search algorithms in a dynamic and interactive environment like the Pacman game. The implemented algorithms demonstrate different strategies for navigating through the game, both in the presence and absence of opponents.

Feel free to explore the code and experiment with different configurations and game scenarios. Contributions and improvements are welcome!

For more detailed instructions and examples, please refer to the in-line comments and documentation within each Python file. Happy coding and have fun with Pacman!
