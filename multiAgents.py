# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent 
    
    """
    def mini_max(self, state, agentIndex, depth ):
       #print(f"Agent Index: {agentIndex}, Depth: {depth}")
       # depth =self.depth * state.getNumAgents ο έλεγχος αυτος εξασφαλίζει ότι ο αλγόριθμος θα εξερευνήσει όλους
       #τους πιθανούς συνδυασμούς κινήσεων για κάθε παίκτη στον ίδιο αριθμό βημάτων αναζήτησης.
       #στην αρχη ειχα βαλει depth==self.depth και σταματαγε η αναζητηση στο depth-1 βαθος
       if depth == self.depth * state.getNumAgents() or state.isLose() or state.isWin():
           #print("search terminate ",agentIndex)
           return self.evaluationFunction(state)
       
       # αν παίζει ο πακμαν
       if agentIndex == 0:
           #print("Pacman search")
           return self.maxvalue_pac(state, agentIndex, depth)[1]
       
       # αν παίζουν τα φαντασματά
       else:
           #print("ghost ",agentIndex," search)
           return self.minvalue_ghost(state, agentIndex, depth)[1]

    def maxvalue_pac(self, state, agentIndex, depth):
       """
       Η συνάρτηση max-value για την ευρεση βελτιστης καταστασης
       """
       #print("maxval on d: ",depth)
       topAct = ("max", -float("inf"))  # Αρχικοποίηση βέλτιστης ενέργειας και τιμής
       for action in state.getLegalActions(agentIndex):
           nextState=state.generateSuccessor(agentIndex, action)
           newDepth=depth + 1
           nextAgentIndex=(depth + 1) % state.getNumAgents()#δείκτη του επόμενου παίκτη μετά τον τρέχοντα παίκτη στον κύκλο των παικτών
           # Υπολογισμός της τιμής της κίνησης
           sucAction = (action, self.mini_max(nextState,nextAgentIndex,newDepth))
           # Επιλογή βέλτιστης ενέργειας για να πάρει ο πράκτορας μας
           topAct = max(topAct, sucAction, key=lambda x: x[1])
           #print("for loop best-action ",topAct)
       #print("Max best-action ",topAct)
       return topAct

    def minvalue_ghost(self, state, agentIndex, depth):
       """
       Η συνάρτηση min-value για την ευρεση του καλυτερου παχνιδιου απο τους αντιπαλους
       """
       #print("minval on d: ",depth,"-ghost:",agentIndex)
       bestAct = ("min", float("inf"))  # Αρχικοποίηση βέλτιστης ενέργειας και τιμής
       for action in state.getLegalActions(agentIndex):
           nextState=state.generateSuccessor(agentIndex, action)
           newDepth=depth + 1
           nextAgentIndex=(depth + 1) % state.getNumAgents()#δείκτη του επόμενου παίκτη μετά τον τρέχοντα παίκτη στον κύκλο των παικτών
           # Υπολογισμός της τιμής της κίνησης
           sucAction = (action, self.mini_max(nextState,nextAgentIndex,newDepth))
           # Επιλογή βέλτιστης ενέργειας-τα φαντάσματα επιλεγουν ενέργειες που μειώνουν την κερδοφορία του πρακτορα
           #Παίζουν Βέλτιστα οι αντίπαλοι
           bestAct = min(bestAct, sucAction, key=lambda x: x[1])
           #print("for loop best-action  ghost",agentIndex,"---",topAct)
       #print("Action that minimazes pacman best action ",agentIndex,"->>",topAct)
       return bestAct

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        #Eκτέλεση πρωτης κινησης του πράκτορα
        #print("begin minimax")
        return self.maxvalue_pac(gameState, 0, 0)[0]

    

class AlphaBetaAgent(MultiAgentSearchAgent):
   """
   Your minimax agent with alpha-beta pruning 
    """
   

   def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "ο αλγορίθμος ειναι ιδιος με το mini-max  απλως στο τελος εχω βαλει την συνθηκη κλαδέματος"
        "*** YOUR CODE HERE ***"
        #print("aplha-beta algorithm begins")
        # Καλούμε τη συνάρτηση maxval για τον αλγόριθμο αποκοπής alpha-beta
        return self.maxvalue(gameState, 0, 0, -float("inf"), float("inf"))[0]

   def alpha_beta(self, state, agentIndex, depth, alpha, beta):
       """
       Ο αλγόριθμος αποκοπής alpha-beta για την αναζήτηση Minimax.
       """
       if depth == self.depth * state.getNumAgents() or state.isLose() or state.isWin():
           #print("search terminate ",agentIndex)
           return self.evaluationFunction(state)
   
       # αν παίζει ο πακμαν
       if agentIndex == 0:
            #print("Pacman search")
          return self.maxvalue(state, agentIndex, depth, alpha, beta)[1]
       
       # Ελάχιστος # αν παίζουν τα φαντασματά
       else:
           #print("ghost ",agentIndex," search)
           return self.minvalue(state, agentIndex, depth, alpha, beta)[1]

   def maxvalue(self, state, agentIndex, depth, alpha, beta):
       """
       Η συνάρτηση max-value για την αποκοπή alpha-beta.
       
       """
       #print("maxval on d: ",depth)
       topAct = ("max", -float("inf"))  # Αρχικοποίηση βέλτιστης ενέργειας και τιμής
       for action in state.getLegalActions(agentIndex):
          nextState=state.generateSuccessor(agentIndex, action)
          newDepth=depth + 1
          nextAgentIndex=(depth + 1) % state.getNumAgents()#δείκτη του επόμενου παίκτη μετά τον τρέχοντα παίκτη στον κύκλο των παικτών
          # Υπολογισμός της τιμής της κίνησης
          sucAction = (action,self.alpha_beta(nextState,nextAgentIndex,newDepth,alpha, beta))
          # Επιλογή βέλτιστης ενέργειας για να πάρει ο πράκτορας μας
          topAct = max(topAct, sucAction, key=lambda x: x[1])
          #print("for loop best-action ",topAct)
           

          # Αποκοπή-κλαδεμα πακ μαν
          if topAct[1] > beta:
               #print("max:best-Action: v",topAct[1],">beta ",beta)
               #print("punned"))                                                                                                                   )
               return topAct
          else:
               alpha = max(alpha, topAct[1])
               #print("Max best-action ",topAct)
       return topAct

   def minvalue(self, state, agentIndex, depth, alpha, beta):
       """
       Η συνάρτηση min-value για την αποκοπή alpha-beta.
       """
       #print("minval on d: ",depth,"ghost",agentIndex)
       bestAct = ("min", float("inf"))  # Αρχικοποίηση βέλτιστης ενέργειας και τιμής
       for action in state.getLegalActions(agentIndex):
           nextState=state.generateSuccessor(agentIndex, action)
           newDepth=depth + 1
           #δείκτη του επόμενου παίκτη μετά τον τρέχοντα παίκτη στον κύκλο των παικτών
           nextAgentIndex=(depth + 1) % state.getNumAgents()
           # Υπολογισμός της τιμής της κίνησης
           sucAction = (action, self.alpha_beta(nextState,nextAgentIndex,newDepth,alpha, beta))
           # Επιλογή βέλτιστης ενέργειας-τα φαντάσματα επιλεγουν ενέργειες που μειώνουν την κερδοφορία του πρακτορα
           #Παίζουν Βέλτιστα οι αντίπαλοι
           bestAct = min(bestAct, sucAction, key=lambda x: x[1])
           #print("for loop best-action  ghost",agentIndex," ",topAct)
      

           # Αποκοπή-κλαδεμα αντιπαλων
           if bestAct[1] < alpha:
               #print("min:best-Action: v",topAct[1],">beta ",beta)
               #print("punned"))  
               return bestAct
           else:
               beta = min(beta, bestAct[1]) 
               #print("Action that minimazes pacman best action ",agentIndex," ",topAct)

       return bestAct


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
    Your expectimax agent (question 4)
    """

    def expecti_max(self, d, agentIndex, state):
        # Εκτύπωση τρέχουσας κατάστασης
        #print(f"Agent: {agentIndex}, Depth: {d}, State: {state}")

        if state.isWin() or state.isLose() or d > self.depth:
            score = self.evaluationFunction(state)
            #print(f"Terminal State Reached: Score = {score}")
            return score

        ret = []  # Αποθηκεύει την τιμή που επιστρέφεται για τις ενέργειες αυτού του κόμβου
        next = state.getLegalActions(agentIndex)  # Αποθηκεύει τις νόμιμες ενέργειες του agent
       
        if Directions.STOP in next:
            next.remove(Directions.STOP)  # Αφαιρούμε την ενέργεια STOP αν υπάρχει

        #print(f"Agent: {agentIndex}, Legal Actions: {next}")
        action_index = 0  # Δείκτης για την τρέχουσα ενέργεια
        #χρησιμοποιείται για να παρακολουθεί ποια ενέργεια επεξεργάζεται αυτή τη στιγμή ο βρόχος while.
       
       # θα εκτελείται όσο η τιμή του action_index είναι μικρότερη από  τον αριθμό των στοιχείων στη λίστα next).
        while action_index < len(next):
            action = next[action_index]
            # Δημιουργούμε την επόμενη κατάσταση
            new_state = state.generateSuccessor(agentIndex, action) 
           
            if (agentIndex + 1) >= state.getNumAgents():
                #print(f"Next Agent is Pacman, Action: {action}")
             # καλούμε αναδρομικά τη self.expecti_max αυξάνοντας το βάθος (d + 1) και ορίζοντας τον agentIndex σε 0 (Pacman). Προσθέτουμε το αποτέλεσμα αυτής της αναδρομικής κλήσης στη λίστα ret
                ret.append(self.expecti_max(d + 1, 0, new_state))
            else:
                #print(f"Next Agent: {agentIndex + 1}, Action: {action}")
                # καλούμε αναδρομικά τη self.expecti_max με το ίδιο βάθος (d) αλλά αυξάνοντας το agentIndex κατά 1 για να περάσουμε στον επόμενο agent (φάντασμα)
                ret.append(self.expecti_max(d, agentIndex + 1, new_state))
            action_index += 1


        if agentIndex == 0:  # Αν είναι ο pacman
        
        
            if d == 1:  # Αν είμαστε πίσω στη ρίζα, επιστρέφουμε την ενέργεια, αλλιώς την τιμή
                max_score = max(ret)
                length = len(ret)
                
                for i in range(length):
                    if ret[i] == max_score:
                       # print(f"Pacman chooses action: {next[i]} with score {max_score}")
                       # Επιστρέφουμε την ενέργεια με τη μέγιστη τιμή
                        return next[i]  
            else:
                # Αν δεν είμαστε στη ρίζα, επιστρέφουμε τη μέγιστη τιμή
                returnVal = max(ret)  
              #  print(f"Max value for Pacman: {returnVal}")
              
            # Αν είναι φάντασμα   
        elif agentIndex > 0: 
            sm = sum(ret)
            leng = len(ret)
            # Υπολογίζουμε την αναμενόμενη τιμή (μέσος όρος)
            returnVal = float(sm / leng)  
            #print(f"Expected value for Ghosts: {returnVal}")

        return returnVal  # Επιστρέφουμε την υπολογισμένη τιμή


    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        Συνάρτηση getAction: Καλεί τη συνάρτηση expectimax με αρχικό βάθος 1 και agentIndex 0 (Pacman) και επιστρέφει την ενέργεια που πρέπει να εκτελεστεί.
        """
        # Ξεκινάμε την αναζήτηση expectimax από το βάθος 1 με τον pacman
        action = self.expecti_max(1, 0, gameState)
       # print(f"Chosen action: {action}")
        return action

             

def betterEvaluationFunction(currentGameState):
    """
    Αυτή η συνάρτηση αξιολογεί το τρέχον state του παιχνιδιού Pacman και επιστρέφει μια τιμή που δείχνει πόσο καλή είναι η κατάσταση αυτή.
    Η αξιολόγηση λαμβάνει υπόψη διάφορους παράγοντες όπως η απόσταση από το πλησιέστερο φαγητό, η απόσταση από τα φαντάσματα,
    ο αριθμός των κάψουλων και των φαγητών που απομένουν, καθώς και την απόσταση από τα φρούτα.
    """
    pacmanPos = currentGameState.getPacmanPosition()
    ghostList = currentGameState.getGhostStates()
    foods = currentGameState.getFood()
    capsules = currentGameState.getCapsules()

    # Επιστρέφουμε ανάλογα με την κατάσταση του παιχνιδιού.
    if currentGameState.isWin():
        return float("inf")
    if currentGameState.isLose():
        return float("-inf")

    # Δημιουργούμε μια λίστα με τις αποστάσεις από τα φαγητά και βρίσκουμε τη μικρότερη απόσταση.
    foodDistList = []
    for each in foods.asList():
        foodDistList.append(util.manhattanDistance(each, pacmanPos))
    minFoodDist = min(foodDistList) if foodDistList else 0

    # Δημιουργούμε λίστες με τις αποστάσεις από τα φαντάσματα και τα φαντάσματα που είναι scared,
    # και βρίσκουμε τις ελάχιστες αποστάσεις.
    ghostDistList = []
    scaredGhostDistList = []
    
    for each in ghostList:
        if each.scaredTimer == 0:
            # Αποστάσεις μεταξύ του Pacman και κάθε φαντάσματος που δεν είναι φοβισμένο.
            ghostDistList.append(util.manhattanDistance(pacmanPos, each.getPosition()))
        elif each.scaredTimer > 0:
            # Αποστάσεις μεταξύ του Pacman και κάθε φαντάσματος που είναι φοβισμένο.
            scaredGhostDistList.append(util.manhattanDistance(pacmanPos, each.getPosition()))

    minGhostDist = min(ghostDistList) if ghostDistList else float("inf")
    minScaredGhostDist = min(scaredGhostDistList) if scaredGhostDistList else 0

    # Αξιολογούμε το σκορ του παιχνιδιού με βάση τη συνάρτηση αξιολόγησης.
    score = scoreEvaluationFunction(currentGameState)
    
    # Μεταβλητές που αλλάζουν ανάλογα με το πλήθος των φαγητών.
    remainingFoods = len(foods.asList())
    #η συναρτηση ειναι αποδοτικη 1<α<2
    a = 1.2 # Βασική σταθερά
  
    #οι συντελεστές δεν μπορούν να πάρουν τιμές   κοντα  ή πανω απο 10
    if remainingFoods > 10:
        b = 1.5 * a   # Απόσταση από το πλησιέστερο φάντασμα
        c = 3 * a     # Απόσταση από το πλησιέστερο φάντασμα που είναι φοβισμένο
    else:
        b = 3 * a     # Αυξάνουμε την βαρύτητα της απόστασης από τα φαντάσματα όταν τα φαγητά είναι λίγα
        c = 6 * a     # Αυξάνουμε την βαρύτητα της απόστασης από τα φοβισμένα φαντάσματα όταν τα φαγητά είναι λίγα

    e = 3 * a  # Αριθμός των φαγητών
    d = 10* a  # Αριθμός των καψουλών

    
    # Προσθέτουμε την αρνητική επίδραση της απόστασης από το πλησιέστερο φαγητό.
    score += -a * minFoodDist

    # Προσθέτουμε την αρνητική επίδραση της απόστασης από το πλησιέστερο φάντασμα.
    if minGhostDist != float("inf"):
        score += -b * (1.0 / minGhostDist)

    # Προσθέτουμε την αρνητική επίδραση της απόστασης από το πλησιέστερο φάντασμα που είναι scared.
    score += -c * minScaredGhostDist

    # Προσθέτουμε την αρνητική επίδραση του αριθμού των κάψουλων.
    score += -d * len(capsules)

    # Προσθέτουμε την αρνητική επίδραση του αριθμού των τροφίμων.
    score += -e * remainingFoods

    return score






# Abbreviation
better = betterEvaluationFunction
