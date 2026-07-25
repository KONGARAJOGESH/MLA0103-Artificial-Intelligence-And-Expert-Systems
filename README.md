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
