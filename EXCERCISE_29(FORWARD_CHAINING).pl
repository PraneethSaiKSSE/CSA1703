
has_fur(dog).
has_fur(cat).
has_feathers(bird).
lays_eggs(bird).
has_scales(fish).
has_scales(snake).
has_gills(fish).


mammal(X) :- has_fur(X).
bird(X) :- has_feathers(X), lays_eggs(X).
reptile(X) :- has_scales(X), \+ has_gills(X).

forward_chaining :-
    findall(X, mammal(X), Mammals),
    findall(X, bird(X), Birds),
    findall(X, reptile(X), Reptiles),
    append(Mammals, Birds, Temp1),
    append(Temp1, Reptiles, Categories),
    list_to_set(Categories, UniqueCategories),
    assert(animal_categories(UniqueCategories)).


