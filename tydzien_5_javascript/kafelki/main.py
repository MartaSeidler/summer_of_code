import random

COLS = 30
ROWS = 30
COLORS =  ["🟥", "🟧", "🟨", "🟩", "🟦"]

def create_board():
    return [[None for _ in range(COLS)] for _ in range(ROWS)]

def assign_colors(board):
    
    for i in range(ROWS):
        for j in range(COLS):
            available_colors = COLORS.copy()

            if i > 0 and board[i-1][j] in available_colors:
                available_colors.remove(board[i-1][j])
            if j > 0 and board[i][j-1] in available_colors:
                available_colors.remove(board[i][j-1])

            board[i][j] = random.choice(available_colors)
              
    return board

def counting_colors(board):

  red = 0
  orange = 0
  yellow = 0
  green = 0
  blue = 0

  for i in range(ROWS):
        for j in range(COLS):
          if board[i][j] == COLORS[0]:
            red += 1
          elif board[i][j] == COLORS[1]:
            orange += 1
          elif board[i][j] == COLORS[2]:
            yellow += 1
          elif board[i][j] == COLORS[3]:
            green += 1
          elif board[i][j] == COLORS[4]:
            blue += 1

  return print(f"""
{COLORS[0]} - {red}
{COLORS[1]} - {orange} 
{COLORS[2]} - {yellow}
{COLORS[3]} - {green}
{COLORS[4]} - {blue}
""")

def display_board(board):
    for row in board:
        print(''.join(row))

def main():
    board = create_board()
    assign_colors(board)
    display_board(board)
    counting_colors(board)

if __name__ == "__main__":
    main()