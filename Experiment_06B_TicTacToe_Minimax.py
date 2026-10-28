# Experiment 6B: Tic-Tac-Toe using Minimax with Alpha-Beta Pruning
def winner(b):
    lines = [b[0:3], b[3:6], b[6:9],
             b[0::3], b[1::3], b[2::3],
             b[0::4], b[2:7:2]]
    for line in lines:
        if line == ["X"] * 3: return 1
        if line == ["O"] * 3: return -1
    return 0 if " " not in b else None

def minimax(b, player, alpha=-2, beta=2):
    result = winner(b)
    if result is not None:
        return result
    scores = []
    for i in range(9):
        if b[i] == " ":
            b[i] = "X" if player == 1 else "O"
            scores.append(minimax(b, -player, alpha, beta))
            b[i] = " "
            if player == 1:
                alpha = max(alpha, max(scores))
            else:
                beta = min(beta, min(scores))
            if beta <= alpha:
                break
    return max(scores) if player == 1 else min(scores)

board = [" "] * 9
moves = []
for i in range(9):
    board[i] = "X"
    moves.append((minimax(board, -1), i))
    board[i] = " "
print("Best move for X (index 0-8):", max(moves)[1])
