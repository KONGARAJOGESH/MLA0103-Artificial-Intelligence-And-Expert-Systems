bird(parrot).
bird(pigeon).
bird(peacock).

has_feathers(parrot).
has_feathers(pigeon).
has_feathers(peacock).

lays_eggs(parrot).
lays_eggs(pigeon).
lays_eggs(peacock).

can_fly(parrot).
can_fly(pigeon).

bird_type(X) :-
    has_feathers(X),
    lays_eggs(X).

can_move(X) :-
    bird(X).

living(X) :-
    bird(X).

flying_bird(X) :-
    bird(X),
    can_fly(X).
