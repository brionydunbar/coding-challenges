"""
Have the function CharlietheDog(strArr) read the array of strings stored in strArr which will be a 4x4 matrix of the characters 'C', 'H', 'F', 'O', where C represents Charlie the dog, H represents its home, F represents dog food, and O represents and empty space in the grid.
Your goal is to figure out the least amount of moves required to get Charlie to grab each piece of food in the grid by moving up, down, left, or right, and then make it home right after.
Charlie cannot move onto the home before all pieces of food have been collected.
For example: if strArr is ["FOOF", "OCOO", "OOOH", "FOOO"], then this looks like the following grid:

For the input above, the least amount of steps where the dog can reach each piece of food, and then return home is 11 steps, so your program should return the number 11.
The grid will always contain between 1 and 8 pieces of food.

Examples:
Input: ["OOOO", "OOFF", "OCHO", "OFOO"]
Output: 7

Input: ["FOOO", "OCOH", "OFOF", "OFOO"]
Output: 10
"""

from collections import deque


def CharlietheDog(strArr):
    rows, cols = 4, 4
    grid = [list(row) for row in strArr]

    # Directions: Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Find Charlie, Home, Food positions
    foods = {}
    food_count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'C':
                start = (r, c)
            elif grid[r][c] == 'H':
                home = (r, c)
            elif grid[r][c] == 'F':
                foods[(r, c)] = food_count
                food_count += 1

    all_food_mask = (1 << food_count) - 1

    # BFS queue: (row, col, food_mask, steps)
    queue = deque([(start[0], start[1], 0, 0)])
    visited = set([(start[0], start[1], 0)])

    while queue:
        r, c, mask, steps = queue.popleft()

        # Check if reached home with all food
        if (r, c) == home and mask == all_food_mask:
            return steps

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                new_mask = mask
                if (nr, nc) in foods:
                    new_mask |= (1 << foods[(nr, nc)])

                # Cannot go home before collecting all food
                if grid[nr][nc] == 'H' and new_mask != all_food_mask:
                    continue

                if (nr, nc, new_mask) not in visited:
                    visited.add((nr, nc, new_mask))
                    queue.append((nr, nc, new_mask, steps + 1))

    return -1  # should never reach here if input guarantees a solution


# keep this function call here
# print(CharlietheDog(input()))

# Testing:
arr1 = ["OOOO", "OOFF", "OCHO", "OFOO"]  # 7
arr2 = ["FOOO", "OCOH", "OFOF", "OFOO"]  # 10
arr3 = ["FOOF", "OCOO", "OOOH", "FOOO"]  # 11

print(CharlietheDog(arr1))
print(CharlietheDog(arr2))
print(CharlietheDog(arr3))