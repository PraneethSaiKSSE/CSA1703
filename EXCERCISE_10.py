import heapq
class Node:
    def __init__(self, x, y, cost, parent=None):
        self.x = x
        self.y = y
        self.cost = cost
        self.parent = parent
    def __lt__(self, other):
        return self.cost < other.cost
def astar(grid, start, goal):
    open_set = []
    closed_set = set()
    start_node = Node(start[0], start[1], 0)
    heapq.heappush(open_set, start_node)
    while open_set:
        current_node = heapq.heappop(open_set)
        if (current_node.x, current_node.y) == goal:
            path = []
            while current_node is not None:
                path.append((current_node.x, current_node.y))
                current_node = current_node.parent
            return path[::-1]
        closed_set.add((current_node.x, current_node.y))
        for neighbor in get_neighbors(grid, current_node):
            if neighbor not in closed_set:
                neighbor_node = Node(neighbor[0], neighbor[1], current_node.cost + 1, current_node)
                heapq.heappush(open_set, neighbor_node)
    return None 
def get_neighbors(grid, node):
    neighbors = []
    x, y = node.x, node.y
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] != 1:
            neighbors.append((new_x, new_y))
    return neighbors
if __name__ == '__main__':
    grid = [
        [0, 0, 0, 0, 1],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1],
        [0, 0, 0, 0, 0]
    ]
    start = (0, 0)
    goal = (4, 4)
    path = astar(grid, start, goal)
    if path:
        print("Shortest Path:")
        for point in path:
            print(point)
    else:
        print("No path found")
