% Define rules and facts for animal categories
mammal(X) :- has_fur(X).
bird(X) :- has_feathers(X), lays_eggs(X).
reptile(X) :- has_scales(X), \+ has_gills(X).

has_fur(dog).
has_fur(cat).
has_feathers(eagle).
lays_eggs(crow).
has_scales(fish).
has_scales(snake).
has_gills(fish).


animal_category(X, "Mammal") :- mammal(X).
animal_category(X, "Bird") :- bird(X).
animal_category(X, "Reptile") :- reptile(X).


