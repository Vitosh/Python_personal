import sys

def check_winner(board, player):
    win_lines = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a, b, c in win_lines:
        if board[a] == player and board[b] == player and board[c] == player:
            return True
    return False

def is_full(board):
    return " " not in board

def print_board(board):
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def minimax(board, is_maximizing):
    # Base Case
    if check_winner(board, "O"): return 1
    if check_winner(board, "X"): return -1
    if is_full(board): return 0

    # Maximizing Step (AI)
    if is_maximizing:
        best_score = -1000
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    
    # Minimizing Step (Human)
    else:
        best_score = 1000
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

def get_best_move(board):
    best_score = -1000
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

def play_game():
    board = [" " for _ in range(9)]
    print_board(board)

    while True:
        user_input = input("Enter move 0-8 (or 'e' to exit): ")
        if user_input.lower() == 'e': sys.exit()

        try:
            choice = int(user_input)
            if board[choice] != " ": continue
            board[choice] = "X"
        except ValueError: continue

        print_board(board)
        if check_winner(board, "X"): print("You Win!"); break
        if is_full(board): print("Draw!"); break

        print("AI is calculating futures...")
        ai_move = get_best_move(board)
        board[ai_move] = "O"
        
        print_board(board)
        if check_winner(board, "O"): print("AI Wins!"); break
        if is_full(board): print("Draw!"); break

if __name__ == "__main__":
    play_game()