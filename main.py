import random
#######################
#Declaring constants
HEIGHT = 8
WIDTH = 8
########################
# 0 = Blank spot
# 1 = Red spot
# 2 = Black spot
########################
board = []
current_turn = 0
def setup_pretend_board():
  global board
  board = [
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0], 
  [0, 0, 0, 0, 2, 0, 0, 0], 
  [0, 0, 0, 0, 0, 0, 0, 0], 
  [0, 0, 0, 0, 0, 0, 0, 0], 
  [0, 0, 0, 0, 0, 0, 0, 0]]
  
def create_initial_board(height, width):
  global board
  for a in range(HEIGHT):
    board.append(list([0]*WIDTH))
  return board

def print_board(current_board): #Call this to print out the baord, pass in board variable
  listForPrint = "\n \n"
  i = 0
  listForPrint += "   0 1 2 3 4 5 6 7" + "\n"
  for a in current_board:
    listForPrint += str(i) + " |"
    for b in a:
      listForPrint +=  str(b) + " " 
    i = i + 1
    listForPrint += "\n" 
  print(listForPrint)


def setup_board(board):
  for a in range(len(board)):
    for b in range(len(board[a])):
      if a == 0 and (b % 2) == 1:
        board[a][b] = 1
      if a == 1 and (b % 2) == 0: # creates first two lines
        board[a][b] = 1
      if len(board) - 1 == a and (b % 2) == 0: #sets last lines
        board[a][b] = 2
      if len(board) - 2 == a and (b % 2) == 1:
        board[a][b] = 2
        
def get_legal_attacks(turn):
    global board
    attack = []
    for a in range(len(board)):
      for b in range(len(board[a])):
        if turn == 1 and board[a][b] == 1:
          if b == 0:
            if board[a + 1][b + 1] == 2 and board[a+2][b+2] == 0:
              attack.append([a,b,a+2,b+2])
          elif b == len(board[a])-1:
            if board[a+1][b-1] == 2 and board[a+1][b-1] == 0:
              attack.append([a,b,a+2,b+2])
          elif board[a+1][b+1] == 2 and board[a+1][b-1]==2 and  board[a+2][b+2] == 0 and board[a+2][b-2]==0:
            attack.append([a,b,a+2,b+2])
            attack.append([a,b,a+2,b-2])
          elif board[a+1][b-1] == 2 and board[a+2][b-2] == 0:
            attack.append([a,b,a+2,b-2])
          elif board[a+1][b+1] == 2 and board[a+2][b+2] == 0:
            attack.append([a,b,a+2,b+2])
        elif turn == 2 and board[a][b] == 2:
          if b == 0:
            if board[a-1][b+1] == 1 and board[a-2][b+2] == 0:
              attack.append([a,b,a-2,b+2])
          elif b == len(board[a]) - 1:
            if board[a-1][b-1] == 1 and board[a-2][b-2] == 0:
              attack.append([a,b,a-2,b-2])
          elif board[a-1][b+1] == 1 and board[a-1][b-1] == 1 and board[a-2][b+2] == 0 and board[a-2][b-2] == 0:
            attack.append([a,b,a-2,b+2])
            attack.append([a,b,a-2,b-2])
          elif board[a-1][b-1] == 1 and board[a-2][b-2] == 0:
            attack.append([a,b,a-2,b-2])
          elif board[a-1][b+1] == 1 and board[a-2][b+2] == 0:
            attack.append([a,b,a-2,b+2]) 
    return attack


def get_legal_moves(turn):
    global board
    possible_move=[]
    
    for a in range(len(board)):
      for b in range(len(board[a])):
        if turn == 1 and board[a][b] == 1:
          if b == 0:
            if board[a + 1][b + 1] == 0:
              possible_move.append([a,b,a+1,b+1])
          elif b == len(board[a])-1:
            if board[a+1][b-1] == 0:
              possible_move.append([a,b,a+1,b+1])
          elif board[a+1][b+1] == 0 and board[a+1][b-1]==0:
            possible_move.append([a,b,a+1,b+1])
            possible_move.append([a,b,a+1,b-1])
          elif board[a+1][b-1] == 0:
            possible_move.append([a,b,a+1,b-1])
          elif board[a+1][b+1] == 0:
            possible_move.append([a,b,a+1,b-1])
        elif turn == 2 and board[a][b] == 2:
          if b == 0:
            if board[a-1][b+1] == 0:
              possible_move.append([a,b,a-1,b+1])
          elif b == len(board[a]) - 1:
            if board[a-1][b-1] == 0:
              possible_move.append([a,b,a-1,b-1])
          elif board[a-1][b+1] == 0 and board[a-1][b-1] == 0:
            possible_move.append([a,b,a-1,b+1])
            possible_move.append([a,b,a-1,b-1])
          elif board[a-1][b-1] == 0:
            possible_move.append([a,b,a-1,b-1])
          elif board[a-1][b+1] == 0:
            possible_move.append([a,b,a-1,b+11])            
    return possible_move

def game():
  global board
  desired_list = []
  if get_legal_attacks(current_turn):
    moves= get_legal_attacks(current_turn)
    attack = True
    #print("attacks exist")
  else:
    moves = get_legal_moves(current_turn)
    attack = False
  print(moves)
  print_board(board)
  #print("temporary input should look like this: (x,y,x,y)")
  desired = input("piece X, Piece Y, Desired X, Desired Y")
  for i in range(len(desired)):
    if desired[i] != ',':
      desired_list.append(int(desired[i]))
  if len(desired_list) != 4:
    print("ERROR IN DESIRED_LIST")
  if desired_list in moves:
    move_piece(desired_list, attack)
  else:
    print("Try again, invalid response")
    game()

def remove_attacked_piece(move):
  global board
  global current_turn

  board[int(abs(move[0] + move[2]) / 2)][int(abs(move[1] + move[3]) / 2)] = 0
  print("I attacked")
  

def move_piece(move, attack):
  global board
  global current_turn
  print()
  board[move[0]][move[1]] = 0
  board[move[2]][move[3]] = current_turn
  if attack:
    remove_attacked_piece(move)
  if current_turn == 1:
    current_turn = 2
    print("It's Black's turn")
  elif current_turn == 2:
    current_turn = 1
    print("It's Red's turn")
  check_for_winner()
  game()
  
def check_for_winner():
  global current_turn
  global board
  red_safe = False
  black_safe = False
  for a in board:
    for b in a:
      if b == 1:
        red_safe = True
      if b == 2:
        black_safe = True
  if not black_safe:
    red_win()
  elif not red_safe:
    black_win()
        
      
def red_win():
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  print("RED WINS!!!!")
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  quit()
def black_win():
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  print("BLACK WINS!!!")
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  quit()

##############################
if __name__ == "__main__":
   board = create_initial_board(HEIGHT, WIDTH)
   setup_board(board)
   #setup_pretend_board()
   print(print_board(board))
   print("Welcome to checkers!")
   current_turn = random.randint(1,2)
   if current_turn == 1:
     print("Red starts!")
   else:
     print("Black starts!")
   game()
