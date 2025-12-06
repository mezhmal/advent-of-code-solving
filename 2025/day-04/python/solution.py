roll = '@'
removed_roll = 'x'

Grid = list[list[str]]

def get_grid_dimentions(grid:Grid) -> tuple[int,int]:
    height = len(grid)
    width = len(grid[0])
    return (height, width)

def can_roll_be_accessed(grid:Grid, i:int, j:int) -> bool:
  width, height = get_grid_dimentions(grid)
  rolls_around = 0
  for k in range(max(i-1,0), min(i+2,height)):
    for l in range(max(j-1,0), min(j+2,width)):
      if (k != i or l != j) and grid[k][l] == roll:
        rolls_around += 1
  return rolls_around < 4

def part1(data:list[str]) -> int:
  accumulator = 0
  grid:Grid = [list(line.strip()) for line in data]
  width, height = get_grid_dimentions(grid)
  for i in range(height):
    for j in range(width):
      if grid[i][j] == roll and can_roll_be_accessed(grid, i, j):
        accumulator += 1

  return accumulator

def remove_accessible_rolls(grid:Grid) -> tuple[Grid, int]:
  removed = 0
  width, height = get_grid_dimentions(grid)
  for i in range(height):
    for j in range(width):
      if grid[i][j] == roll and can_roll_be_accessed(grid, i, j):
        removed += 1
        grid[i][j] = removed_roll
  return (grid, removed)

def part2(data:list[str]) -> int:
  accumulator = 0
  grid:Grid = [list(line.strip()) for line in data]
  while True:
    grid, removed = remove_accessible_rolls(grid)
    accumulator += removed
    if removed == 0:
      break

  return accumulator
