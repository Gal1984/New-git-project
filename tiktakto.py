def print_board(board):
    print("---------")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("---------")

def check_winner(board):
    # בדיקת שורות
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    # בדיקת עמודות
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    # בדיקת אלכסונים
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None

def is_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"תור השחקן: {current_player}")

        try:
            move = input("הכנס מספר שורה ומספר עמודה (לדוג' 1 2): ")
            row, col = map(int, move.strip().split())
            row -= 1
            col -= 1
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("מיקום לא חוקי, נסה שוב.")
                continue
            if board[row][col] != " ":
                print("המקום כבר תפוס, נסה שוב.")
                continue
            board[row][col] = current_player
        except Exception:
            print("נא להזין שני מספרים מופרדים ברווח, לדוג' '2 3'")
            continue

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"השחקן {winner} ניצח!")
            break
        elif is_draw(board):
            print_board(board)
            print("תיקו!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()