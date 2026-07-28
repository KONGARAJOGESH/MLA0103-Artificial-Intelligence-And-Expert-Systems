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
PSEUDO CODES

------------------------------------------------------------------------------------------------------------
#1 SUM OF INTEGERS FROM 1 TO N

FUNCTION SUM(N)

IF N = 0 THEN
    RETURN 0
ELSE
    RETURN N + SUM(N-1)
END IF

END FUNCTION

------------------------------------------------------------------------------------------------------------
#2 DATABASE WITH NAME AND DOB

START

STORE Name and DOB

READ Name

SEARCH Database

IF Name Found THEN
    DISPLAY DOB
ELSE
    DISPLAY "Record Not Found"
END IF

STOP

------------------------------------------------------------------------------------------------------------
#3 STUDENT–TEACHER–SUBJECT DATABASE

START

STORE Student, Teacher and Subject Details

READ Student ID or Subject Code

SEARCH Database

IF Record Found THEN
    DISPLAY Details
ELSE
    DISPLAY "Record Not Found"
END IF

STOP

------------------------------------------------------------------------------------------------------------
#4 PLANETS DATABASE

START

STORE Planet Names

READ Planet Name

SEARCH Database

IF Planet Found THEN
    DISPLAY "Planet Exists"
ELSE
    DISPLAY "Planet Not Found"
END IF

STOP

------------------------------------------------------------------------------------------------------------
#5 TOWERS OF HANOI

FUNCTION TOH(N, SOURCE, DESTINATION, AUXILIARY)

IF N = 1 THEN
    DISPLAY "Move Disk from SOURCE to DESTINATION"
ELSE
    CALL TOH(N-1, SOURCE, AUXILIARY, DESTINATION)
    DISPLAY "Move Disk from SOURCE to DESTINATION"
    CALL TOH(N-1, AUXILIARY, DESTINATION, SOURCE)
END IF

END FUNCTION

------------------------------------------------------------------------------------------------------------
#6 BIRD CAN FLY OR NOT

START

STORE Bird Names

STORE Flying Birds

READ Bird Name

IF Bird Can Fly THEN
    DISPLAY "Can Fly"
ELSE
    DISPLAY "Cannot Fly"
END IF

STOP

------------------------------------------------------------------------------------------------------------
#7 FAMILY TREE

START

STORE Male, Female and Parent Facts

DEFINE Mother, Father, Grandfather,
Grandmother, Brother and Sister Relations

READ Person Name

DISPLAY Required Relation

STOP

------------------------------------------------------------------------------------------------------------
#8 DIET SUGGESTION SYSTEM

START

STORE Diseases and Diet Suggestions

READ Disease

SEARCH Database

IF Disease Found THEN
    DISPLAY Suggested Diet
ELSE
    DISPLAY "Diet Not Available"
END IF

STOP

------------------------------------------------------------------------------------------------------------
#9 MONKEY BANANA PROBLEM

START

Monkey Walks to Box

Monkey Pushes Box Under Banana

Monkey Climbs onto Box

Monkey Grasps Banana

DISPLAY "Banana Obtained"

STOP

------------------------------------------------------------------------------------------------------------
#10 FRUIT AND ITS COLOUR USING BACKTRACKING

START

STORE Fruit and Colour Facts

READ Fruit Name or Colour

SEARCH Database

DISPLAY Matching Result

IF More Answers Exist THEN
    DISPLAY Next Answer
END IF

STOP

------------------------------------------------------------------------------------------------------------
#11 BEST FIRST SEARCH

FUNCTION BEST_FIRST_SEARCH(Start, Goal)

OPEN ← Start

CLOSED ← Empty

WHILE OPEN is not Empty

    SELECT Best Node

    IF Goal Reached THEN
        DISPLAY Path
        STOP
    END IF

    EXPAND Node

    ADD Successors to OPEN

END WHILE

DISPLAY "Goal Not Found"

END FUNCTION

------------------------------------------------------------------------------------------------------------
#12 MEDICAL DIAGNOSIS

START

STORE Symptoms and Diseases

READ Symptom

SEARCH Knowledge Base

IF Match Found THEN
    DISPLAY Disease
ELSE
    DISPLAY "Diagnosis Not Available"
END IF

STOP

------------------------------------------------------------------------------------------------------------
#13 FORWARD CHAINING

START

STORE Facts

STORE Rules

APPLY Rules to Existing Facts

GENERATE New Facts

REPEAT Until No New Facts are Generated

DISPLAY Final Conclusion

STOP

------------------------------------------------------------------------------------------------------------
#14 BACKWARD CHAINING

START

READ Goal

CHECK Whether Goal is a Known Fact

IF Goal is Not Known THEN

    FIND Rule for Goal

    PROVE Each Condition

END IF

IF Goal is Proven THEN
    DISPLAY "Goal Proven"
ELSE
    DISPLAY "Goal Cannot Be Proven"
END IF

STOP
============================================================
1. EXPERIMENT NAME:
A* Search Algorithm Implementation

PSEUDOCODE:
============================================================

START

Input graph, heuristic values, start node and goal node

Create priority queue

Insert start node into priority queue

Set cost of start node as 0

Set parent of start node as NULL

WHILE priority queue is not empty:

    Remove node with lowest f value

    IF current node is goal node:

        Trace path using parent nodes

        Display shortest path and cost

        STOP

    FOR each neighbour of current node:

        Calculate new path cost

        IF new cost is smaller than previous cost:

            Update cost

            Calculate f value = cost + heuristic

            Add neighbour to priority queue

            Store parent node

END


============================================================
2. EXPERIMENT NAME:
Water Jug Problem Using Breadth First Search (BFS)

PSEUDOCODE:
============================================================

START

Initialize jug capacities

Set initial state and goal state

Create an empty queue

Insert initial state into queue

Create visited list

WHILE queue is not empty:

    Remove first state from queue

    IF current state matches goal state:

        Display solution path

        STOP

    Mark state as visited

    Generate possible water transfer states

    FOR each new state:

        IF state is not visited:

            Add state into queue

IF goal state is not found:

    Display "No Solution"

END


============================================================
3. EXPERIMENT NAME:
Water Jug Problem Using State Space Search

PSEUDOCODE:
============================================================

START

Initialize jug quantities

Display initial state

Perform valid pouring operations

Generate new states

Display each generated state

Repeat operations until goal state is reached

Display goal achieved message

END


============================================================
4. EXPERIMENT NAME:
Depth First Search (DFS) Algorithm Implementation

PSEUDOCODE:
============================================================

START

Input graph and starting node

Create an empty visited list

Call DFS function

DFS(node):

    IF node is not visited:

        Mark node as visited

        Display node

        FOR each adjacent node:

            Call DFS for adjacent node

Display DFS traversal order

END


============================================================
5. EXPERIMENT NAME:
Greedy Best First Search (GBFS) Algorithm Implementation

PSEUDOCODE:
============================================================

START

Input graph, heuristic values, start node and goal node

Create priority queue

Insert start node with heuristic value

Create visited list

WHILE queue is not empty:

    Remove node with lowest heuristic value

    IF node is goal node:

        Display path

        STOP

    Mark node as visited

    FOR each neighbour node:

        Calculate heuristic value

        Add neighbour into priority queue

IF goal is not reached:

    Display "Path Not Found"

END


============================================================
6. EXPERIMENT NAME:
Backward Chaining Using Prolog

PSEUDOCODE:
============================================================

START

Define facts and rules

Enter query (goal)

Check whether goal matches any fact

IF goal is a fact:

    Return TRUE

ELSE:

    Find rule that can prove the goal

    Check conditions of the rule

    Recursively prove sub goals

IF all conditions are true:

    Return TRUE

ELSE:

    Return FALSE

END


============================================================
7. EXPERIMENT NAME:
Forward Chaining Using Prolog

PSEUDOCODE:
============================================================

START

Define initial facts and rules

Store known facts

Repeat until no new facts are generated:

    Select a rule

    Check rule conditions

    Generate new conclusion

    Add conclusion to known facts

Check required query

Display result

END
