move(grasp,
[state(middle,onbox,middle,hasnot)],
[state(middle,onbox,middle,has)]).

move(climb,
[state(P,onfloor,P,H)],
[state(P,onbox,P,H)]).

move(push(P1,P2),
[state(P1,onfloor,P1,H)],
[state(P2,onfloor,P2,H)]).

move(walk(P1,P2),
[state(P1,onfloor,B,H)],
[state(P2,onfloor,B,H)]).
