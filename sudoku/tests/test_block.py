from solve import *

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

def test_block():
    assert block(grid,  0) == [None, 8, None, 1, None, None, None, None, 7]
    assert block(grid,  9) == [None, 8, None, 1, None, None, None, None, 7]
    assert block(grid, 18) == [None, 8, None, 1, None, None, None, None, 7]
    assert block(grid,  2) == [None, 8, None, 1, None, None, None, None, 7]
    assert block(grid, 11) == [None, 8, None, 1, None, None, None, None, 7]    
    assert block(grid, 20) == [None, 8, None, 1, None, None, None, None, 7]
    
    assert block(grid, 54) == [9, None, None, None, None, 4, None, 2, None]
    assert block(grid, 64) == [9, None, None, None, None, 4, None, 2, None]
    assert block(grid, 74) == [9, None, None, None, None, 4, None, 2, None]
    
    assert block(grid, 80) == [1, None, None, None, None, 5, None, 8, None]
    assert block(grid, 70) == [1, None, None, None, None, 5, None, 8, None]
    assert block(grid, 60) == [1, None, None, None, None, 5, None, 8, None]
    