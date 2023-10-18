hanoi(N) :- move(N, left, middle, right).

move(0, _, _, _) :- !.
move(N, A, B, C) :-
    M is N-1,
    move(M, A, C, B),
    write('Move disk from '), write(A), write(' to '), write(C), nl,
    move(M, B, A, C).

