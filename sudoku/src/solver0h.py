import re, sys

def main():
    with open("problem.txt", "r") as file:
        lines = file.readlines()
    for line in lines:
        allCellList = check(line)
        emptyCellIndexList = empty(allCellList)

        for emptyCell in emptyCellIndexList:
            print(usableNums(emptyCell, allCellList))

def check(line):
    match = re.search(r"^([\.1-9]{9} ){8}[\.1-9]{9}$", line)
    if not match:
        raise ValueError("Invalid input")
    else:
        line = line.replace(" ", "")
        cellList = []
        for cell in list(line):
            if cell == ".":
                cell = None
            elif cell == "\n":
                break
            else:
                cell = int(cell)
            cellList.append(cell)

        return cellList

def empty(cellList):
    indexList = []
    for index, cell in enumerate(cellList):
        if cell == None:
            indexList.append(int(index))

    return indexList

def row(index, allCellList):
    rowNumStart = (index // 9) * 9
    rowNumEnd = rowNumStart + 8
    row = allCellList[rowNumStart : rowNumEnd+1]
    usedNumList = []
    for cell in row:
        if cell != None:
            usedNumList.append(cell)

    return usedNumList

def column(index, allCellList):
    firstColumn = [0, 9 , 18, 27, 36, 45, 54, 63, 72]
    columnNum = (index % 9)
    column = []
    for cell in firstColumn:
        column.append(allCellList[cell+columnNum])
    usedNumList = []
    for cell in column:
        if cell != None:
            usedNumList.append(cell)

    return usedNumList

def block(index, allCellList):
    rowIndex = (index // 9) // 3
    columnIndex = (index % 9) // 3
    firstIndex = (rowIndex * 27) + (columnIndex * 3)
    block = []
    for x in range (9):
        if x < 3:
            cell = firstIndex + (x * 1)
        elif x < 6:
            cell = firstIndex + 9 + (x % 3 * 1)
        else:
            cell = firstIndex + 18 + (x % 3 * 1)
        block.append(allCellList[cell])
    usedNumList = []
    for cell in block:
        if cell != None:
            usedNumList.append(cell)

    return usedNumList

def allUsedNumList(index, allCellList):
    usedNumList = row(index, allCellList) + column(index, allCellList) + block(index, allCellList)
    return set(usedNumList)

def usableNums(index, allCellList):
    return {1,2,3,4,5,6,7,8,9} - allUsedNumList(index, allCellList)



if __name__ == "__main__":
    main()
