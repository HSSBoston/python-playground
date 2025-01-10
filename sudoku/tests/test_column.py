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

def test_column():
    assert column(grid, 0) == [None, 1, None, 3, None, None, 9, None, None]
    assert column(grid, 9) == [None, 1, None, 3, None, None, 9, None, None]
    assert column(grid, 72) == [None, 1, None, 3, None, None, 9, None, None]
    
    assert column(grid, 4) == [None, None, None, 1, None, 8, None, None, None]
    assert column(grid, 13) == [None, None, None, 1, None, 8, None, None, None]
    assert column(grid, 76) == [None, None, None, 1, None, 8, None, None, None]
    
    assert column(grid, 6) == [None, 9, None, None, None, None, 1, None, None]
    assert column(grid, 15) == [None, 9, None, None, None, None, 1, None, None]
    assert column(grid, 78) == [None, 9, None, None, None, None, 1, None, None]
    
    assert column(grid, 8) == [None, None, 3, None, None, 4, None, 5, None]
    assert column(grid, 17) == [None, None, 3, None, None, 4, None, 5, None]
    assert column(grid, 80) == [None, None, 3, None, None, 4, None, 5, None]

