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

def test_makeGrid():
    assert len(problemList) == 81
    assert len(grid) == 81
    assert grid == problemList
