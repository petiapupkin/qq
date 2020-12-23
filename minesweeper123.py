from typing import List, Set, Dict, Tuple, Optional

def greetPlayer():
    print("\nWelcome to Minesweeper.\n")
    input("Press any key to continue...\n")

def createBoard():
    board: List[List[int]] = [[100, 100, 100], [100, 100, 100],[100, 100, 201]]
    return board

def selectGameOption() -> str:
    while True:
        print("\nGame Options:")
        print("----------------------------")
        print("To pick a square, type 'a'.")
        print("To quit the game, type 'b'.")
        currentChoice = input("Please select an option: \n")
        if currentChoice == "a" or currentChoice == "b":
            return currentChoice
        else:
            print("That is an invalid option. Please try again.")

def selectSquare() -> Tuple[str, int]:
    while True:
        print("\n")
        column: str = input("Please select a column (A, B, or C): ")
        row: int = int(input("Please select a row (0, 1, or 2): \n"))
        if (column == "A" or column == "B" or column == "C") and (row >= 0 and row < 3):
            return column, row
        else:
            print("That is an invalid option. Please try again.")

def convertColumn(currColumn: str) -> int:
    if currColumn == "A":
        return 0
    elif currColumn == "B":
        return 1
    elif currColumn == "C":
        return 2
    else:
        return -1

def selectMoveOption() -> bool:
    while True:
        print("\nMove options:")
        print("-----------------------------------------------------------")
        print("Do you want to flag (\"f\") or reveal (\"r\") the selected square?")
        choice: str = input()
        if choice == "f":
            return True
        elif choice == "r":
            return False
        else:
            print("That is an invalid option. Please try again.")

def calculateBombs(board: List[List[int]], column: int, row: int) -> int:
        finalCount: int = 0

        # Top left, mid, and right
        if row - 1 >= 0:
            if column - 1 >= 0 and board[row -1][column - 1] == 201:
                finalCount += 1
            if board[row -1][column] == 201:
                finalCount += 1 
            if column + 1 <= 2 and board[row -1][column + 1] == 201:
                finalCount += 1
        
        # Left and right
        if column - 1 >= 0 and board[row][column - 1] == 201:
            finalCount += 1
        if column + 1 <= 2 and board[row][column + 1] == 201:
            finalCount += 1  

        # Bottom left, mid, and right
        if row + 1 <= 2:
            if column - 1 >= 0 and board[row + 1][column - 1] == 201:
                finalCount += 1
            if board[row + 1][column] == 201:
                finalCount += 1 
            if column + 1 <= 2 and board[row + 1][column + 1] == 201:
                finalCount += 1  
        
        return finalCount

def updateBoard(board: List[List[int]], column: int, row: int, flag: bool) -> List[List[int]]:
        if flag:
            board[row][column] = 202
        elif board[row][column] == 201:
            return [[301]]
        else:
            numberOfBombs: int = calculateBombs(board, column, row)
            if numberOfBombs == 0:
                board[row][column] = 101
            else:
                board[row][column] = numberOfBombs
        return board

def printBoard(board: List[List[int]]) -> None:
    print("   A  B  C ")
    for index, row in enumerate(board):
        nextRow: List[str] = []
        for square in row:
                if square == 100 or square == 201:
                    nextRow.append(" _ ")     
                elif square == 101:
                    nextRow.append(" C ")
                else:
                    nextRow.append(" {} ".format(str(square)))
        print("{} {} \n".format(index, "".join(nextRow)))

def validateBoard(board: List[List[int]]) -> bool:
    for row in board:
        for square in row:
            if square == 100 or square == 201:
                return False
    return True

def startGame() -> None:
    greetPlayer()

def runGame() -> bool:
    # Initialization variables
    board: List[List[int]] = createBoard()
    bombs: int = 0
    strColumn: str = ""
    column: int = -1
    row: int = -1

    while True:
        # Player selects a game option
        printBoard(board)
        currentChoice: str = selectGameOption()
        
        # Player quits game
        if currentChoice == 'b':
            return False
        
        # Player selects a square
        strColumn, row = selectSquare()
        column = convertColumn(strColumn)

        flag: bool = selectMoveOption() 
        
        # Board updated
        board = updateBoard(board, column, row, flag)

        # Bomb hit
        if board[0][0] == 301:
           return False
        
        # Check if board completed
        roundResult: bool = validateBoard(board)
        if roundResult:
           return True

def endGame(gameResult: bool) -> None:
    if gameResult:
        print("Congratulations! You won!")
    else:
        print("You lose...")

# Entry point
def main() -> None:
    startGame()
    gameResult: bool = runGame()
    endGame(gameResult)

if __name__ == "__main__":
    main()