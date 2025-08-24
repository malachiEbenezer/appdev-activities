import random


def create_grid(size):
    return [['-' for _ in range(size)] for _ in range(size)]


def place_treasures(grid, num_treasures):
    size = len(grid)
    treasures = 0
    while treasures < num_treasures:
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        if grid[x][y] != 'T':  # Ensure no duplicate treasures
            grid[x][y] = 'T'
            treasures += 1


def display_grid(grid):
    for row in grid:
        print(' '.join(row))
    print()


def get_move():
    move = input("Enter your move (up, down, left, right): ").strip().lower()
    return move


def update_position(position, move, size):
    x, y = position
    if move == 'up' and x > 0:
        x -= 1
    elif move == 'down' and x < size - 1:
        x += 1
    elif move == 'left' and y > 0:
        y -= 1
    elif move == 'right' and y < size - 1:
        y += 1
    return (x, y)


def treasure_hunt_game(size=5, num_treasures=3, max_moves=20):
    grid = create_grid(size)
    place_treasures(grid, num_treasures)
    position = (0, 0)  # Starting position
    found_treasures = 0

    print("Welcome to Treasure Hunt!")
    print(f"Grid size: {size}x{size}, Treasures to find: {num_treasures}, Max moves: {max_moves}")

    for move_count in range(max_moves):
        display_grid(grid)
        print(f"Move {move_count + 1}/{max_moves}. Current position: {position}")

        move = get_move()
        position = update_position(position, move, size)

        x, y = position
        if grid[x][y] == 'T':
            found_treasures += 1
            grid[x][y] = 'F'  # Mark treasure as found
            print("YOU FOUND A TREASURE!")
        else:
            print("No treasure here.")

        if found_treasures == num_treasures:
            print("CONGRATULATIONS! You've found all the treasures!")
            break
    else:
        print("Game over! You've used all your moves.")

    display_grid(grid)


# Run the game
treasure_hunt_game()
