# Puzzle game

# Initialize the puzzle
puzzle = [["*", "*", "*"],
          ["*", "*", "*"],
          ["*", "*", "*"]]

# Function to display the puzzle
def display_puzzle():
  for row in puzzle:
    print(" ".join(row))
  print()

# Initialize the player's position
pos_x = 0
pos_y = 0

# Main game loop
while True:
  # Display the puzzle
  display_puzzle()

  # Get player's move
  move = input("Enter your move (up, down, left, right): ")

  # Update player's position based on move
  if move == "up":
    pos_y -= 1
  elif move == "down":
    pos_y += 1
  elif move == "left":
    pos_x -= 1
  elif move == "right":
    pos_x += 1
  else:
    print("Invalid move")
    continue

  # Make sure the player's move is valid
  if pos_x < 0 or pos_x >= len(puzzle[0]) or pos_y < 0 or pos_y >= len(puzzle):
    print("Invalid move")
    pos_x = 0
    pos_y = 0
    continue

  # Update the puzzle with the player's move
  puzzle[pos_y][pos_x] = "X"