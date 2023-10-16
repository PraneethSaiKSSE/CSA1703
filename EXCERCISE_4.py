from itertools import permutations

def solve_cryptarithmetic(puzzle):
    # Split the puzzle into words and extract unique letters
    words = puzzle.split()
    letters = set("".join(words))

    # Check if the number of unique letters is greater than 10 (0-9 digits)
    if len(letters) > 10:
        return "Too many unique letters"

    # Generate all possible permutations of digits (0-9) for the unique letters
    digit_permutations = permutations("0123456789", len(letters))

    # Iterate through the permutations and try to solve the puzzle
    for perm in digit_permutations:
        digit_map = dict(zip(letters, perm))
        if all(int("".join([digit_map[c] for c in word])) for word in words):
            # If the puzzle is solved, return the solution
            solution = " ".join([word.translate(str.maketrans(digit_map)) for word in words])
            return solution

    return "No solution found"

# Example usage
puzzle = "SEND + MORE = MONEY"
print("SEND + MORE = MONEY")
solution = solve_cryptarithmetic(puzzle)
print(solution)
