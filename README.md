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
