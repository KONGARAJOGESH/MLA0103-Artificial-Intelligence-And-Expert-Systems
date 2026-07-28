male(john).
male(peter).
female(mary).
female(linda).

parent(john,peter).
parent(mary,peter).
parent(john,linda).
parent(mary,linda).

human(X) :-
    male(X).

human(X) :-
    female(X).

father(X,Y) :-
    parent(X,Y),
    male(X).

mother(X,Y) :-
    parent(X,Y),
    female(X).

child(X,Y) :-
    parent(Y,X).

grandparent(X,Y) :-
    parent(X,Z),
    parent(Z,Y).

ancestor(X,Y) :-
    parent(X,Y).

ancestor(X,Y) :-
    parent(X,Z),
    ancestor(Z,Y).
