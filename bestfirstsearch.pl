edge(a,b).
edge(a,c).
edge(b,d).
edge(c,e).
edge(d,f).

bestfirst(X,Y):-edge(X,Y).
