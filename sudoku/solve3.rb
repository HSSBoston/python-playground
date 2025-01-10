def makeGrid(line)
  spaceRemovedLine = line.gsub(/\s/, "")
  spaceRemovedLine.split(//).map{ |str| str == "." ? nil: str.to_i }
end

def gridStr(grid, pad="\n")
  (0..8).map{ |row_i|
    grid[9*row_i, 9].map{ |val|
      (val || ".") }.join("") }.join(pad)
end

def printGrid(grid, pad="\n")
  print gridStr(grid, pad) + "\n"
end

def row(grid, cell_i)
  grid.slice(9 * (cell_i / 9), 9)
end

def column(grid, cell_i)
  (0..8).map{ |k| grid[9 * k + cell_i % 9] }
end

def square(grid, cell_i)
  (0..8).map{ |k| grid[9*(3*(cell_i/9/3)+(k/3)) + 3*(cell_i%9/3) + (k%3)]}
end

def usableNumbers(grid, cell_i)
    (1..9).is_a - usedNumbers(grid, cell_i)
end

def usedNumbers(grid, cell_i)
    (row(grid, cell_i).compact +
     column(grid, cell_i).compact +
     square(grid, cell_i).compact).uniq

def emptyCells(grid)
    (0..80).select{ |cell_i| !grid[cell_i]}
end

def nextEmptyCell(emptyCells)
  if emptyCells.empty?
    return [nil, nil]
  else
    candidates = emptyCells.map{ |emptyCell_i|
                   [emptyCell_i, usableNumbers(grid, emptyCell_i)] }
    orderedCandidates = candidates.sort_by{ |candidate| candidate[1].length }
    return orderedCandidates[0]

def solve(grid)
  emptyCells = emptyCells(grid)
  if emptyCells.empty?
    retrun grid
  else
    cell_i, usableNumbers = nextEmptyCell(emptyCells)
    usableNumbers.each do |val|
      grid[cell_i] = val
      if solve(grid)
        return true
      end
    end
    grid[cell_i] = nil
      return false
  end
end

solutions = []
expected = []

ARGF.each do |line|
  grid = makeGrid(line)
  solve(grid)
  solutions.push(grid)
end

expected.push("485937612" +
              "136258947" +
              "297164853" +
              "342516798" +
              "859742361" +
              "761389524" +
              "978425136" +
              "614893275" +
              "523671489")

(solutions.size).times do |sol_i|
  if gridStr(solutions[sol_i], pad="") == expected[sol_i]
    puts puts "Solution " + (sol_i + 1).to_s + ": Correct"
    printGrid(solutions[sol_i])
  else
    puts "Solution " + (sol_i + 1).to_s + ": Incorrect"
  end
  puts "--------------------"
end
