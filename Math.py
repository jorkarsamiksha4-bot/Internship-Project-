# Step 1: Movie dataset
movies = {
    "Avengers": "Action",
    "Titanic": "Romance",
    "Inception": "Sci-Fi",
    "Gladiator": "Action",
    "Notebook": "Romance"
}

# Step 2: User preference
user_preference = "Action"

# Step 3: Recommendation
print("Recommended Movies:")
for movie, genre in movies.items():
    if genre == user_preference:
        print(movie)
import math

# Initialize board
board = [' ' for _ in range(9)]

# Display board
def print_board():
    print()
    for i in range(3):
        print(board[i*3], '|', board[i*3+1], '|', board[i*3+2])
        if i < 2:
            print('--+---+--')
    print()

# Check winner
def is_winner(player):
    win_positions = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for a, b, c in win_positions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

# Check draw
def is_draw():
    return ' ' not in board

# Minimax algorithm
def minimax(is_ai):
    if is_winner('O'):
        return 1
    if is_winner('X'):
        return -1
    if is_draw():
        return 0

    if is_ai:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best_score = min(best_score, score)
        return best_score

# AI move
def ai_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'O'

# Human move
def human_move():
    move = int(input("Enter position (1-9): ")) - 1
    if move < 0 or move > 8 or board[move] != ' ':
        print("Invalid move! Try again.")
        human_move()
    else:
        board[move] = 'X'

# Game start
print("TIC-TAC-TOE AI")
print("Position Guide:")
print("1 | 2 | 3")
print("--+---+--")
print("4 | 5 | 6")
print("--+---+--")
print("7 | 8 | 9")

print_board()

# Game loop
while True:
    human_move()
    print_board()
    if is_winner('X'):
        print("🎉 You win!")
        break
    if is_draw():
        print("😐 Draw!")
        break

    ai_move()
    print("AI Move:")
    print_board()
    if is_winner('O'):
        print("🤖 AI wins!")
        break
    if is_draw():
        print("😐 Draw!")
        break