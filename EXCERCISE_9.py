import itertools
def calculate_total_distance(tour, cities):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += cities[tour[i]][tour[i+1]]
    total_distance += cities[tour[-1]][tour[0]] 
    return total_distance
def brute_force_tsp(cities):
    num_cities = len(cities)
    if num_cities <= 2:
        return list(range(num_cities)), calculate_total_distance(list(range(num_cities)), cities)
    min_tour = None
    min_distance = float('inf')
    city_indices = list(range(num_cities))

    for tour in itertools.permutations(city_indices):
        distance = calculate_total_distance(tour, cities)
        if distance < min_distance:
            min_distance = distance
            min_tour = tour

    return min_tour, min_distance
cities=[[0, 11, 9, 21],
        [11, 0, 15, 12],
        [9, 15, 0, 27],
        [21, 12, 27, 0]]
                   
best_tour, min_distance = brute_force_tsp(cities)
print("Best tour:", best_tour)
print("Minimum distance:", min_distance)
