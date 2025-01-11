def makeGrid(line):
    line = line.replace(" ", "")
    try:
        if len(line) == 81:
            return [int(cell) if cell != "." else None for cell in line]
        else:
            raise RuntimeError("Incorrect problem input")
    except RuntimeError:
        raise

def emptyCellIndices(grid):
    return [i for i, cell in enumerate(grid) if cell == None]
    
def row(grid, cellIndex):
    rowIndex = cellIndex // 9
    return grid[9*rowIndex : (9*rowIndex)+9]

def column(grid, cellIndex):
    columnIndex = cellIndex % 9
    return [ grid[(9*i)+columnIndex] for i in range(0,9)]

def block(grid, cellIndex):
    cellRowIndex       = cellIndex // 9
    cellColumnIndex    = cellIndex % 9
    blockRowIndex      = cellRowIndex // 3 
    blockColumnIndex   = cellColumnIndex // 3
    topLeftCellInBlock = blockRowIndex * 27 + blockColumnIndex * 3
    
    return grid[topLeftCellInBlock      : topLeftCellInBlock + 3] + \
           grid[topLeftCellInBlock + 9  : topLeftCellInBlock + 9 + 3] + \
           grid[topLeftCellInBlock + 18 : topLeftCellInBlock + 18 + 3]

def usedNumbers(grid, cellIndex):
    usedNumbersInRow    = [n for n in row(grid, cellIndex)    if n is not None]
    usedNumbersInColumn = [n for n in column(grid, cellIndex) if n is not None]
    usedNumbersInBlock  = [n for n in block(grid, cellIndex)  if n is not None]
    return set(usedNumbersInRow + usedNumbersInColumn + usedNumbersInBlock)

def usableNumbers(grid, cellIndex):
    return {1, 2, 3, 4, 5, 6, 7, 8, 9} - usedNumbers(grid, cellIndex)


def solve(grid):
    emptyCells = emptyCellIndices(grid)
    if len(emptyCells) == 0:
        return grid
    else:
        emptyCellIndex = emptyCells[0]
        usableNums = usableNumbers(grid, emptyCellIndex)
        for n in usableNums:
            grid[emptyCellIndex] = n
            if solve(grid):
                return grid
        grid[emptyCellIndex] = None
        return False


def verifySolution(grid):
    for i, n in enumerate(grid):
        rowNumbers    = row(grid, i)
        columnNumbers = column(grid, i)
        blockNumbers  = block(grid, i)
        if unique(rowNumbers) and unique(columnNumbers) and unique(blockNumbers):
            continue
        else:
            return False
    return True

def unique(numbersList):
    return set(numbersList) == {1, 2, 3, 4, 5, 6, 7, 8, 9}

def printSolution(grid):
    solutionStr = ""
    for rowIndex in range(0, 9):
        for i in range(rowIndex * 9, rowIndex * 9 + 9):
            solutionStr += str(grid[i])
        solutionStr += "\n"
    print(solutionStr)


if __name__ == "__main__":
    with open("problem.txt", "r") as f:
        for line in f:
            grid = makeGrid(line.rstrip("\n"))
            solution = solve(grid)
            if verifySolution(solution):
                printSolution(solution)

