

def main():
    count = 1
    values = value_collection()
    player1 = input("please enter the first player's name: ")
    player2 = input("please enter the second player's name: ")
    while True:
        show_table(values)
        find_winner(values, count, player1, player2)
        player = find_player(count, player1, player2)
        square = input(f"it is {player}'s turn. Please choose a square (1-9): ")
        square = input_interger_validation(square)
        square = input_1to10_validation(square)
        square = used_square_check(values, square)
        put_into_square(values, square, count)
        count += 1
        
def find_player(count, player1, player2):
    if count % 2 == 1:
        player = player1
    else:
        player = player2
    return player

def value_collection():
    values = []
    for square in range(1,10):
        values.append(square)
    return values

def show_table(values):
    print(f"{values[0]}|{values[1]}|{values[2]}")
    print("-+-+-")
    print(f"{values[3]}|{values[4]}|{values[5]}")
    print("-+-+-")
    print(f"{values[6]}|{values[7]}|{values[8]}")

def put_into_square(values, square, count):
    if count % 2 == 1:
        values[square - 1] = "x"
    if count % 2 == 0:
        values[square - 1] = "o"
    
def find_winner(values, count, player1, player2):
    player = find_player(count + 1, player1, player2)
    if values[0] == values[1] == values[2] or \
       values[3] == values[4] == values[5] or \
       values[6] == values[7] == values[8] or \
       values[0] == values[3] == values[6] or \
       values[1] == values[4] == values[7] or \
       values[2] == values[5] == values[8] or \
       values[0] == values[4] == values[8] or \
       values[2] == values[4] == values[6]:
        print(f"congrate, {player} win!")
        exit()
    if count == 10:
        print("Draw!")
        exit()
        
def input_interger_validation(number):
     while True:
         try:
             number = int(number)
             return number
         except ValueError:
             print("Sorry, you should enter a interger")
             number = input("Please choose a square (1-9): ")
    
def input_1to10_validation(number):
     while True:
         if 0 < number < 10:
             return number
         else:
             print("Sorry, you should enter a interger between 1 to 9.")
             number = input("Please choose a square (1-9): ")
             number = input_interger_validation(number)

def used_square_check(values, square):
    while True:
        if values[square - 1] == "o" or values[square - 1] == "x":
            print("Sorry, you can not do that.")
            square = input("Please choose a square (1-9): ")
            square = input_interger_validation(square)
            square = input_1to10_validation(square)
        else:
            return square

if __name__ == "__main__":
    main()