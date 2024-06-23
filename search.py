# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    start = problem.getStartState()#Περνουμε την αρχικη κατασταση του προβλήματος αναζήτησης
    #ελεγχουμε αν αρχική κατασταση = κατάσταση στόχου
    if problem.isGoalState(start):
       # print("Start state is equal to Goal state")
        return []

    #στοιβα για να βαλουμε τους κομβους-καταστάσεις προς επίσκεψη
    myStack = util.Stack()
    
    visiteds =util.Queue()  # Χρησιμοποιούμε σύνολο για να αποθηκευουμε τους κόμβους που εχουν εξερευνηθει
    # (node,actions)
    #βαζουμε την αρχικη κατασταση στην λίστα
    myStack.push((start, []))

    #μεχρι να αδειασει η στοίβα  με κομβους προς εξερευνηση
    while not myStack.isEmpty():
        #κανουμε αποθηση του πρωτου στοιχειου της στοίβας
        current, actions = myStack.pop()
        
        #αν ο κομβος δεν εχει εξερευνηθει
        if current not in visiteds.list:
            #προσθηκη στην λιστα με τους κομβους που εχουν  εξερευνηθει
            visiteds.push(current)
            #print("Visited node:", current)  # Εκτύπωση του τρέχοντος κόμβου
            
            if problem.isGoalState(current):
               # print("Goal reached!")  # Εκτύπωση ότι ο στόχος έχει επιτευχθεί
                l= list(visiteds.list)
               # print("STATES(X,Y):" , l)#
                return actions

           #τοποθετούμε στην στοίβα τους γειτονικούς κομβους ,του κόμβου οπου βρισκόμαστε
            for next_, action,cost in problem.getSuccessors(current):
                newAction = actions + [action]
                myStack.push((next_, newAction))
                #print("Node to expand(pushed to the stack)", next_)  # Εκτύπωση του επόμενου κόμβου που προστίθεται στη στοίβα


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # Λήψη της αρχικής κατάστασης
    start = problem.getStartState()
    #print("Start state:", start)
    
    # Ελέγχουμε αν η αρχική κατάσταση είναι ο στόχος
    if problem.isGoalState(start):
       # print("Start state is equal to Goal state")
        return []
    
    # Ουρά για να βάλουμε τις καταστάσεις που πρέπει να επισκεφτούμε
    q = util.Queue()
    visiteds = []  # Λίστα για τους επισκεπτόμενους κόμβους
    
    # Προσθήκη της αρχικής κατάστασης στην ουρά
    q.push((start, []))
   # print("Pushed start state to the queue")

    # Μέχρι να αδειάσει η ουρά με τους κόμβους προς εξερεύνηση
    while not q.isEmpty():
        current, actions = q.pop()  # Αποθήκευση του επόμενου κόμβου και των ενεργειών που οδηγούν σε αυτόν
        #print("Current state:", current)
        if current not in visiteds:  # Αν ο κόμβος δεν έχει επισκεφθεί ακόμα
            visiteds.append(current)  # Προσθήκη του στη λίστα των επισκεπτόμενων κόμβων
           # print("Visited node:", current)

            if problem.isGoalState(current):  # Έλεγχος αν είναι ο στόχος
               # print("Goal state reached!")  # Εκτύπωση ότι ο στόχος έχει επιτευχθεi
                #print("STATES(X,Y):" , visiteds)
                return actions  # Επιστροφή των ενεργειών που οδηγούν στο στόχο

            # Προσθήκη των γειτονικών καταστάσεων του τρέχοντος κόμβου στην ουρά
            for next_, action, cost in problem.getSuccessors(current):
                newAction = actions + [action]  # Δημιουργία νέας λίστας ενεργειών που περιέχει και την προηγούμενη
                q.push((next_, newAction))  # Προσθήκη της καινούργιας κατάστασης στην ουρά
               # print("Node to expand(pushed to the queque):", current,"->",next_)

    # Αν δεν βρεθεί λύση, εκτός από το print, εγείρεται ένα μη υλοποιημένο σφάλμα
    util.raiseNotDefined()

def uniformCostSearch(problem):
    "Search the node of least total cost first. "

    # Αρχική κατάσταση
    start = problem.getStartState()
   # print("Start state:", start)  # Εκτύπωση της αρχικής κατάστασης

    # Έλεγχος αν η αρχική κατάσταση είναι ήδη η κατάσταση στόχος
    if problem.isGoalState(start):
       # print("Start state is already a goal state.")
        return []

    # Λίστα για την αποθήκευση των επισκεφθέντων κόμβων
    visited = []
    # Λίστα για την αποθήκευση των κόμβων που επιλέγονται
    selected_nodes = []

    # Προτεραιότητα ουρά για την επεξεργασία των κόμβων με βάση το κόστος
    pr_queue = util.PriorityQueue()
    # Προσθήκη της αρχικής κατάστασης με προτεραιότητα 0
    pr_queue.push((start, [], 0), 0)

    while not pr_queue.isEmpty():
        # Αποσπούμε τον επόμενο κόμβο από την ουρά με τη μικρότερη προτεραιότητα
        current, actions, prev_cost = pr_queue.pop()
      #  print("Current node:", current)  # Εκτύπωση του τρέχοντος κόμβου

        # Αν ο κόμβος δεν έχει επισκεφθεί
        if current not in visited:
            visited.append(current)
            # Προσθήκη του τρέχοντος κόμβου στη λίστα με τους επιλεγμένους κόμβους
            selected_nodes.append(current)

            # Έλεγχος αν ο κόμβος είναι κατάσταση στόχος
            if problem.isGoalState(current):
              #  print("Goal reached!")  # Εκτύπωση ότι ο στόχος έχει επιτευχθεί
                # Εκτύπωση της λίστας των επισκεφθέντων κόμβων
               # print("Visited nodes:", visited)
                return actions

            # Επεξεργασία των γειτονικών κόμβων
            for nextNode, action, cost in problem.getSuccessors(current):
                new_act = actions + [action]
                # Υπολογισμός του συνολικού κόστους μέχρι τον τρέχοντα κόμβο
                new_cost = prev_cost + cost
                # Προσθήκη του επόμενου κόμβου με το σχετικό κόστος στην ουρά με τη σωστή προτεραιότητα
                pr_queue.push((nextNode, new_act, new_cost), new_cost)
               # print("Node to expand(pushed to the priority queque):", nextNode)  # Εκτύπωση του επόμενου κόμβου που προστίθεται στην ουρά

    # Αν δεν υπάρχει λύση, επιστρέφουμε "Not Defined"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
   A heuristic function estimates the cost from the current state to the nearest
   goal in the provided SearchProblem.  This heuristic is trivial.
   """
    return 0
 
def aStarSearch(problem, heuristic=nullHeuristic):
    """
    A* search algorithm.

    Args:
    - problem: The search problem to be solved.
    - heuristic: The heuristic function to estimate the cost to reach the goal from a given state.

    Returns:
    - A list of actions to reach the goal state.
    """
    # Αρχική κατάσταση
    st = problem.getStartState()
    #print("Starting A* search from state:", st)

    # Έλεγχος αν η αρχική κατάσταση είναι ήδη η κατάσταση στόχος
    if problem.isGoalState(st):
       # print("Start state is already a goal state.")
        return []

    # Λίστα για την αποθήκευση των επισκεφθέντων κόμβων
    visited = []
   # print("Visited nodes:", visited)

    # Προτεραιότητα ουρά για την επεξεργασία των κόμβων
    pr_queue = util.PriorityQueue()

    # Προσθήκη της αρχικής κατάστασης με προτεραιότητα 0
    pr_queue.push((st, [], 0), 0)

    while not pr_queue.isEmpty():
        # Αποσπούμε τον επόμενο κόμβο από την ουρά με τη μικρότερη προτεραιότητα
        cur, actions, prev_cost = pr_queue.pop()
       # print("Expanding node:", cur)

        # Αν ο κόμβος δεν έχει επισκεφθεί
        if cur not in visited:
            # Προσθήκη του τρέχοντος κόμβου στη λίστα με τους επισκεφθέντων κόμβους
            visited.append(cur)

            # Έλεγχος αν ο κόμβος είναι κατάσταση στόχος
            if problem.isGoalState(cur):
               # print("Goal reached!")
               # print("Visited nodes:", visited)
                return actions

            # Επεξεργασία των γειτονικών κόμβων
            for nextNode, action, cost in problem.getSuccessors(cur):
                new_act = actions + [action]
                new_cost = prev_cost + cost
                heuristic_cost = new_cost+ heuristic(nextNode, problem)
                pr_queue.push((nextNode, new_act, new_cost), heuristic_cost)
               # print("Added next node to the priority queue:", nextNode)

    # Αν δεν υπάρχει λύση, επιστρέφουμε "Not Defined"
    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
