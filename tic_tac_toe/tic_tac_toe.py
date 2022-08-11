# Создайте программу для игры в ""Крестики-нолики"".

def main():
# Движок программы
    introduction = intro()
    board = create_grid()
    pretty = printPretty(board)
    symbol_1, symbol_2 = sym()
    full = isFull(board, symbol_1, symbol_2) # Функция запуска игры
    
def intro():
# Правила игры
    print("Привет! Приветствую тебя в игре крестики-нолики")
    print("\n")
    print("Правила: Игрок 1 и игрок 2, обозначенные X и O, ходят по очереди. "
          "Поле размером 3*3 клетки. Игрок, которому удается поставить "
          "три своих отметки в горизонтальном, вертикальном или диагональном ряду выигрывает.")
    print("\n")
    input("Нажмите Enter, чтобы продолжить.")
    print("\n")

def create_grid():
# Создадим пустое поле
    print("Вот игровое поле: ")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]        
    return board

def sym():
# Функция определения игроков
    symbol_1 = input("Игрок 1, ты хочешь играть Х или О? ")
    if symbol_1 == "X" or "x" or "Х" or "х" or "+":
        symbol_2 = "0" or "O" or "o" or "" or "О" or "о"
        print("Игрок 2, тогда вы будете играть О. ")
    else:
        symbol_2 = "X" or "x" or "Х" or "х" or "+"
        print("Игрок 2, тогда вы будете играть X. ")
    input("Нажмите Enter, чтобы продолжить.")
    print("\n")
    return (symbol_1, symbol_2)

def startGamming(board, symbol_1, symbol_2, count):
    # Выбор хода
    if count % 2 == 0:
        player = symbol_1
    elif count % 2 == 1:
        player = symbol_2
    print("Игрок "+ player + ", Ваша очередь. ")
    row = int(input("Выберите строку: "
                    "[верхняя строка: введите 0, средняя строка: введите 1, нижняя строка: введите 2]: "))
    column = int(input("Выберите столбец: "
                       "[левый столбец: введите 0, средний столбец: введите 1, правый столбец введите 2]: "))

    # Проверка, не выходит ли выбор игроков за пределы допустимого диапазона
    while (row > 2 or row < 0) or (column > 2 or column < 0):
        outOfBoard(row, column)
        row = int(input("Выберите строку [верхняя строка: "
                        "[введите 0, средняя строка: введите 1, нижняя строка: введите 2]: "))
        column = int(input("Выберите столбец: "
                           "[левый столбец: введите 0, средний столбец: введите 1, правый столбец введите 2]: "))

        # Проверка, заполнения поля
    while (board[row][column] == symbol_1)or (board[row][column] == symbol_2):
        filled = illegal(board, symbol_1, symbol_2, row, column)
        row = int(input("Выберите строку [верхняя строка: "
                        "[введите 0, средняя строка: введите 1, нижняя строка: введите 2]:"))
        column = int(input("Выберите столбец: "
                            "[левый столбец: введите 0, средний столбец: введите 1, правый столбец введите 2]: "))    
        
    # Нахождение символов игрока на поле
    if player == symbol_1:
        board[row][column] = symbol_1
    else:
        board[row][column] = symbol_2
    return (board)

def isFull(board, symbol_1, symbol_2):
    count = 1
    winner = True
# Проверяем на заполненность поля
    while count < 10 and winner == True:
        gaming = startGamming(board, symbol_1, symbol_2, count)
        pretty = printPretty(board)
        
        if count == 9:
            print("Поле полностью заполнено. Игра закончена.")
            if winner == True:
                print("Это ничья. ")

        # Проверим, есть ли здесь победитель
        winner = isWinner(board, symbol_1, symbol_2, count)
        count += 1
    if winner == False:
        print("Игра закончена.")
        
    # Функция подведения итогов
    report(count, winner, symbol_1, symbol_2)

def outOfBoard(row, column):
# Эта функция сообщает игрокам, 
# что их выбор находится вне допустимого диапазона.
    print("Ваш выбор вне указанных границ. Выберите другой. ")
    
def printPretty(board):
# Функция печати поля
    rows = len(board)
    cols = len(board)
    print("---+---+---")
    for r in range(rows):
        print(board[r][0], " |", board[r][1], "|", board[r][2])
        print("---+---+---")
    return board

def isWinner(board, symbol_1, symbol_2, count):
# Функция проверки победителя
    winner = True
    # Проверка строк
    for row in range (0, 3):
        if (board[row][0] == board[row][1] == board[row][2] == symbol_1):
            winner = False
            print("Игрок " + symbol_1 + ", Ты победил!")
   
        elif (board[row][0] == board[row][1] == board[row][2] == symbol_2):
            winner = False
            print("Игрок " + symbol_2 + ", Ты победил!")
            
    # Проверка столбцов
    for col in range (0, 3):
        if (board[0][col] == board[1][col] == board[2][col] == symbol_1):
            winner = False
            print("Игрок " + symbol_1 + ", Ты победил!")
        elif (board[0][col] == board[1][col] == board[2][col] == symbol_2):
            winner = False
            print("Игрок " + symbol_2 + ", Ты победил!")

    # Проверка диагонали
    if board[0][0] == board[1][1] == board[2][2] == symbol_1:
        winner = False 
        print("Игрок " + symbol_1 + ", Ты победил!")

    elif board[0][0] == board[1][1] == board[2][2] == symbol_2:
        winner = False
        print("Игрок " + symbol_2 + ", Ты победил!")

    elif board[0][2] == board[1][1] == board[2][0] == symbol_1:
        winner = False
        print("Игрок " + symbol_1 + ", Ты победил!")

    elif board[0][2] == board[1][1] == board[2][0] == symbol_2:
        winner = False
        print("Игрок " + symbol_2 + ", Ты победил!")
    return winner
    
def illegal(board, symbol_1, symbol_2, row, column):
    print("Выбранная Вами клетка уже заполнена. Выберите другую.")

def report(count, winner, symbol_1, symbol_2):
    print("\n")
    input("Нажмите Enter, чтобы увидеть сводку игры. ")
    if (winner == False) and (count % 2 == 1 ):
        print("Победитель: Игрок " + symbol_1 + ".")
    elif (winner == False) and (count % 2 == 0 ):
        print("Победитель: Игрок " + symbol_2 + ".")
    else:
        print("Это ничья. ")

# Вызов главной функции
main()