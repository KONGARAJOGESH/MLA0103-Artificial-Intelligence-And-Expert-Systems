# PSEUDO CODES
----------------------------------------------------------- #1 BFS PROGRAM -----------------------------------------------------------

FUNCTION BFS(start):

visited ← empty list
queue ← empty queue

INSERT start INTO queue

WHILE queue is not empty:

    current ← REMOVE first element FROM queue

    IF current is not in visited:

        ADD current TO visited

        FOR each adjacent_node OF current:

            INSERT adjacent_node INTO queue

DISPLAY "BFS Traversal :", visited
----------------------------------------------------------- #2 DFS PROGRAM -----------------------------------------------------------

FUNCTION DFS(vertex, visited):

IF vertex is not in visited:

    ADD vertex TO visited

    DISPLAY vertex

    FOR each adjacent_node OF vertex:

        CALL DFS(adjacent_node, visited)

END FUNCTION
# PSEUDO CODE
----------------------------------------------------------- #3 UNIFORM COST SEARCH (UCS) PROGRAM -----------------------------------------------------------

FUNCTION UCS(start, goal)

frontier ← empty priority queue
visited ← empty set

INSERT (0, start, [start]) INTO frontier

WHILE frontier is not empty

    (cost, node, path) ← REMOVE node with minimum cost

    IF node = goal THEN

        DISPLAY path
        DISPLAY cost
        STOP

    END IF

    IF node is not in visited THEN

        ADD node TO visited

        FOR each (neighbor, edge_cost) OF node

            new_cost ← cost + edge_cost

            INSERT (new_cost, neighbor, path + neighbor) INTO frontier

        END FOR

    END IF

END WHILE

DISPLAY "Goal Not Found"

END FUNCTION
