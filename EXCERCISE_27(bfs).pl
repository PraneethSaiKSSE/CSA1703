
edge(a, b, 2).
edge(a, c, 1).
edge(b, d, 3).
edge(c, e, 4).
edge(e, f, 1).
edge(d, f, 5).

heuristic(Node, HeuristicValue) :-
    
    goal(f, GoalNode),
    edge(Node, GoalNode, HeuristicValue).


best_first_search(Start, Goal, Path) :-
    best_first_search_helper([[Start]], Goal, Path).

best_first_search_helper([[Node | Path] | _], Goal, [Node | Path]) :-
    goal(Node, Goal).

best_first_search_helper([Path | Paths], Goal, FinalPath) :-
    extend(Path, NewPaths),
    append(Paths, NewPaths, UpdatedPaths),
    best_first_search_helper(UpdatedPaths, Goal, FinalPath).

extend([Node | Path], NewPaths) :-
    findall([NewNode, Node | Path], 
            (edge(Node, NewNode, _), \+ member(NewNode, Path)),
            NewPaths).


goal(Node, Goal) :- Node = Goal.


