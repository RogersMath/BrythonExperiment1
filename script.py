from browser import document, html, window
import math

# Initialize the game board
board_size = 10
cell_size = 50
start = (0, 0)
exit = (9, 9)
obstacles = set()

# Generate random obstacles using JavaScript's Math.random()
def random_int(min_val, max_val):
    return math.floor(window.Math.random() * (max_val - min_val + 1)) + min_val

while len(obstacles) < 3:
    obstacle = (random_int(0, board_size - 1), random_int(0, board_size - 1))
    if obstacle != start and obstacle != exit:
        obstacles.add(obstacle)

# Set up the canvas
canvas = document["gameCanvas"]
ctx = canvas.getContext("2d")

# Draw the board
def draw_board():
    ctx.clearRect(0, 0, canvas.width, canvas.height)
    for row in range(board_size):
        for col in range(board_size):
            x, y = col * cell_size, row * cell_size
            ctx.strokeRect(x, y, cell_size, cell_size)
            if (row, col) == start:
                ctx.fillStyle = "green"
                ctx.fillRect(x, y, cell_size, cell_size)
            elif (row, col) == exit:
                ctx.fillStyle = "blue"
                ctx.fillRect(x, y, cell_size, cell_size)
            elif (row, col) in obstacles:
                ctx.fillStyle = "red"
                ctx.fillRect(x, y, cell_size, cell_size)
            else:
                ctx.fillStyle = "white"
                ctx.fillRect(x, y, cell_size, cell_size)

# Player starting position
player_pos = list(start)

# Draw the player
def draw_player():
    x, y = player_pos[1] * cell_size, player_pos[0] * cell_size
    ctx.fillStyle = "yellow"
    ctx.fillRect(x, y, cell_size, cell_size)

# Update the board with player position
def update_board():
    draw_board()
    draw_player()

# Handle key presses to move the player
def move_player(event):
    if event.keyCode == 37:  # Left arrow
        if player_pos[1] > 0 and (player_pos[0], player_pos[1] - 1) not in obstacles:
            player_pos[1] -= 1
    elif event.keyCode == 38:  # Up arrow
        if player_pos[0] > 0 and (player_pos[0] - 1, player_pos[1]) not in obstacles:
            player_pos[0] -= 1
    elif event.keyCode == 39:  # Right arrow
        if player_pos[1] < board_size - 1 and (player_pos[0], player_pos[1] + 1) not in obstacles:
            player_pos[1] += 1
    elif event.keyCode == 40:  # Down arrow
        if player_pos[0] < board_size - 1 and (player_pos[0] + 1, player_pos[1]) not in obstacles:
            player_pos[0] += 1
    update_board()
    check_win()

# Check if the player has reached the exit
def check_win():
    if tuple(player_pos) == exit:
        ctx.fillStyle = "green"
        ctx.fillText("You Win!", canvas.width // 2 - 30, canvas.height // 2)

# Initialize the game
update_board()
document.bind("keydown", move_player)
