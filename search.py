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
        
        print "Start:", problem.getStartState()
        print "Is the start a goal?", problem.isGoalState(problem.getStartState())
        print "Start's successors:", problem.getSuccessors(problem.getStartState())
        """
    "*** YOUR CODE HERE ***"
    
    
    #
    # print "Start:", problem.getStartState()
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    # print "Start's successors:", problem.getSuccessors(problem.getStartState())
    
    
    import Queue
    current_node = [problem.getStartState(), []]
    frontier = Queue.LifoQueue()
    frontier.put(current_node)
    explored = set()
    successor = None
    if problem.isGoalState(current_node[0]):
        return current_node[1]
    while True:
        if frontier.empty():
            return None
        current_node = frontier.get()
        current_place = current_node[0]
        current_path = current_node[1]
        if problem.isGoalState(current_place):
            return current_path
        explored.add(current_place)
        successor = problem.getSuccessors(current_place)
        # print current_node
        for node in successor:
            node_place = node[0]
            node_action = node[1]
            if node_place not in explored:
                frontier.put( (node_place, current_path + [node_action]))

'''could be finished by recursive way'''


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    import Queue
    #
    # import Queue
    # root_nodes =(problem.getStartState(), [])
    # def BFS(node,problem = problem):
    #     if problem.isGoalState(node[0]):
    #         return node[1]
    #     return BFS(problem.getSuccessors())
    #
    # BFS(root_nodes)
    # BFS(problem.getStartState)
    #
    current_node = [problem.getStartState(), []]
    frontier = Queue.Queue()
    frontier.put(current_node)
    explored = set()
    successor = None
    if problem.isGoalState(current_node[0]):
        return current_node[1]
    while True:
        if frontier.empty():
            return None
        current_node = frontier.get()
        current_place = current_node[0]
        current_path = current_node[1]
        if problem.isGoalState(current_place):
            return current_path
        explored.add(current_place)
        successor = problem.getSuccessors(current_place)
        # print current_node
        for node in successor:
            node_place = node[0]
            node_action = node[1]
            if node_place not in explored:
                frontier.put( (node_place, current_path + [node_action]))

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first
    bug!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!








    ."""

    "*** YOUR CODE HERE ***"
    import util
    print problem

    #
    # import Queue
    # root_nodes =(problem.getStartState(), [])
    # def BFS(node,problem = problem):
    #     if problem.isGoalState(node[0]):
    #         return node[1]
    #     return BFS(problem.getSuccessors())
    #
    # BFS(root_nodes)
    # BFS(problem.getStartState)
    #
    current_node = [problem.getStartState(), []]
    frontier = util.PriorityQueue()
    frontier.push(current_node,0)
    explored = set()
    successor = None
    min_cost_path = []
    if problem.isGoalState(current_node[0]):
        return current_node[1]
    while True:
        
        # print frontier
        if frontier.isEmpty():
            break
        current_node = frontier.pop()
        current_place = current_node[0]
        current_path = current_node[1]
        if problem.isGoalState(current_place):
            min_cost_path = current_path
        explored.add(current_place)
        if min_cost_path == []:
            successor = problem.getSuccessors(current_place)
            # print current_node
            for node in successor:
                node_place = node[0]
                node_action = node[1]
                if node_place not in explored:
                    path = current_path + [node_action]
                    # print path
                    frontier.update((node_place, path), problem.getCostOfActions(path))
                    # print problem.getCostOfActions(path)
    # print min_cost_path
    return min_cost_path
    
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
        A heuristic function estimates the cost from the current state to the nearest
        goal in the provided SearchProblem.  This heuristic is trivial.
        """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    import searchAgents
    import util

    def f(path, place):
        return len(path) + searchAgents.manhattanHeuristic(place, problem)
    current_node = [problem.getStartState(), []]
    frontier = util.PriorityQueue()
    frontier.push(current_node,f([],current_node[0]))
    explored = set()
    successor = None
    min_cost_path = []
    if problem.isGoalState(current_node[0]):
        return current_node[1]
    while True:

        # print frontier
        if frontier.isEmpty():
            break
        current_node = frontier.pop()
        current_place = current_node[0]
        current_path = current_node[1]
        if problem.isGoalState(current_place):
            min_cost_path = current_path
        explored.add(current_place)
        if min_cost_path == []:
            successor = problem.getSuccessors(current_place)
            # print current_node
            for node in successor:
                node_place = node[0]
                node_action = node[1]
                if node_place not in explored:
                    path = current_path + [node_action]
                    # print path
                    frontier.update((node_place, path), f(path, node_place))
                    # print problem.getCostOfActions(path)
    # print min_cost_path
    return min_cost_path





    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

