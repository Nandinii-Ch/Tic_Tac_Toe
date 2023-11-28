def print_board(x_state, o_state):
    print(f"{mark(0)} | {mark(1)} | {mark(2)} ")
    print(f"--|---|---")
    print(f"{mark(3)} | {mark(4)} | {mark(5)} ")
    print(f"--|---|---")
    print(f"{mark(6)} | {mark(7)} | {mark(8)} ")
    
def mark(n):
    m = 'x' if x_state[n] else ('O' if o_state[n] else n)
    return m

def sum(a, b, c):
    return a+b+c
def check_win(x_state, o_state):
    wins = [[0,1,2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 1, 4], [2, 4, 6]]
    for win in wins:
        if sum(x_state[win[0]] , x_state[win[1]] , x_state[win[2]]) == 3:
            print("X won the game")
            return 1
        if sum(o_state[win[0]] , o_state[win[1]], o_state[win[2]]) == 3:
            print("O win the game")
            return 0
    return -1

def is_right_move(n):
    if x_state[n] == 0 and o_state[n] == 0:
        return 1
    return 0
def update(value, turn):
    if is_right_move(value):
        if turn == 1:
            x_state[value] = 1
        elif turn == 0:
            o_state[value] = 1
    else:
        print("Move not valid")
        value = int(input("Please enter again : "))
        update(value, turn)

if __name__ == "__main__" :
    x_state = [0 for i in range(0,9)]
    o_state = [0 for i in range(0,9)]
    turn = 1 #1 for x and 0 for o
    print("Welcome to Tic_Tac_Toe")
    count = 0
    while(True):
        print_board(x_state, o_state)
        if count == 9:
            print("game over")
            break
        if(turn == 1):
            print("X's chance")
            value = int(input("Please enter a value : "))
            update(value, turn)
            
        else:
            print("O's chance")
            value = int(input("Please enter a value : "))
            update(value, turn)
        check = check_win(x_state, o_state)
        if(check != -1):
            break
        count += 1
        turn = 1 - turn
