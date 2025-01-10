from solver import *

problemStr = ".8.....1. 1..2..9.. ..7..4..3 3...1..9. ...7.2... .6..8...4 9..4..1.. ..4..3..5 .2.....8."
problemList = [None, 8,    None, None, None, None, None, 1,    None,
               1,    None, None, 2,    None, None, 9,    None, None,
               None, None, 7,    None, None, 4,    None, None, 3,
               3,    None, None, None, 1,    None, None, 9,    None,
               None, None, None, 7,    None, 2,    None, None, None,
               None, 6,    None, None, 8,    None, None, None, 4,
               9,    None, None, 4,    None, None, 1,    None, None,
               None, None, 4,    None, None, 3,    None, None, 5,
               None, 2,    None, None, None, None, None, 8,    None]
grid = makeGrid(problemStr)

def test_usedNumbers():
    assert usedNumbers(grid,  0) == {1, 3, 9, 8, 7}
    assert usedNumbers(grid, 80) == {2, 8, 3, 4, 5, 1}
    assert usedNumbers(grid,  8) == {1, 8, 3, 4, 5, 9}
    assert usedNumbers(grid, 54) == {1, 3, 9, 2, 4}    
    
def test_usableNumbers():
    assert usableNumbers(grid,  0) == {2, 4, 5, 6}
    assert usableNumbers(grid, 80) == {6, 7, 9}
    assert usableNumbers(grid,  8) == {2, 6, 7}
    assert usableNumbers(grid, 54) == {5, 6, 7, 8}
    