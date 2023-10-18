sum_numbers(1,1).
sum_numbers(N, Sum) :-
    N > 1,
    Prev is N - 1,
    sum_numbers(Prev, PrevSum),
    Sum is N + PrevSum.
