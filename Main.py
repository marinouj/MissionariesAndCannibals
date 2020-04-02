from Graph import Graph
from State import State

boat_cap = 2
max_m = 3
max_c = 3

def findPaths():
    move = []
    for c in range(boat_cap + 1):
        for m in range(boat_cap + 1):
            if (m >= c or m == 0) and 1 <= m+c <= boat_cap:
                move.append((m, c))
    return move




def main():
    moveList = findPaths()
    start_state = State(max_m, max_c, True, max_m, max_c, boat_cap, moveList)
    INITIAL_STATE = State(max_m, max_c, True, max_m, max_c, boat_cap, moveList)
    # TERMINAL_STATE = State(-1, -1, Direction.NEW_TO_OLD, -1, -1, 0)

    g = Graph()
    p = g.BFS(INITIAL_STATE)
    p = g.DFS(INITIAL_STATE)

if __name__ == '__main__':
	main()