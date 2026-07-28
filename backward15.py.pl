% Facts
parent(john, mary).
parent(mary, alice).
parent(alice, bob).

% Rule
grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).
