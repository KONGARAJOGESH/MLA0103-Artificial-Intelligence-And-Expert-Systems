:- dynamic fact/1.

% Initial Facts
fact(a).
fact(b).

% Rules
rule(c) :-
    fact(a),
    fact(b).

rule(d) :-
    fact(c).

% Forward Chaining
forward :-
    rule(X),
    \+ fact(X),
    assertz(fact(X)),
    write('Derived: '),
    write(X),
    nl,
    fail.

forward.

% Display all facts
show_facts :-
    fact(X),
    write(X),
    nl,
    fail.

show_facts.
