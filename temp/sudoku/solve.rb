def makeGrid(line)
  spaceRemovedLine = line.gsub(/\s/, "")
  p spaceRemovedLine.split(//).map{ |str| str == "." ? nil: str.to_i }
  
end

def printGrid(grid, pad="\n")
  print (0..8).map{ |row_i|
    grid[9*row_i, 9].map{ |val|
      (val || ".") }.join("") }.join(pad), "\n"
end

ARGF.each do |line|
  grid = makeGrid(line)
  printGrid(grid)
  
end