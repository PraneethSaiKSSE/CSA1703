can_fly(pigeon).
can_fly(sparrow).
can_fly(eagle).
cannot_fly(penguin).
cannot_fly(ostrich).


bird_can_fly(Bird) :- can_fly(Bird).
bird_can_fly(Bird) :- \+ cannot_fly(Bird).
