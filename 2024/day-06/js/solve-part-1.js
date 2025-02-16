const directions = {
  'up': 'up',
  'right': 'right',
  'down': 'down',
  'left': 'left'
}

const symbols = {
  guard: '^',
  clean: '.',
  dirty: 'X',
  obstacle: '#'
}

class Lab {
  guard = {
    direction: directions.up
  }

  constructor(lines) {
    this.field = lines.map(line => line.split(''))
    this.height = this.field.length
    this.width = this.field[0].length
    this.guard.y = this.field.findIndex(row => row.includes(symbols.guard))
    this.guard.x = this.field[this.guard.y].findIndex(col => col === symbols.guard)
    this.field[this.guard.y][this.guard.x] = symbols.dirty
  }

  moveGuard() {
    if (this.guardIsOnFieldEdge) {
      return
    }

    switch (this.guard.direction) {
      case directions.up:
        if (this.field[this.guard.y - 1][this.guard.x] === symbols.obstacle) {
          this.guard.direction = directions.right
        } else {
          this.guard.y -= 1
          this.field[this.guard.y][this.guard.x] = symbols.dirty
        }
        break
      case directions.right:
        if (this.field[this.guard.y][this.guard.x + 1] === symbols.obstacle) {
          this.guard.direction = directions.down
        } else {
          this.guard.x += 1
          this.field[this.guard.y][this.guard.x] = symbols.dirty
        }
        break
      case directions.down:
        if (this.field[this.guard.y + 1][this.guard.x] === symbols.obstacle) {
          this.guard.direction = directions.left
        } else {
          this.guard.y += 1
          this.field[this.guard.y][this.guard.x] = symbols.dirty
        }
        break
      case directions.left:
        if (this.field[this.guard.y][this.guard.x - 1] === symbols.obstacle) {
          this.guard.direction = directions.up
        } else {
          this.guard.x -= 1
          this.field[this.guard.y][this.guard.x] = symbols.dirty
        }
        break
    }
  }

  get guardIsOnFieldEdge() {
    return this.guard.x === 0 || this.guard.x === (this.width - 1) ||
      this.guard.y === 0 || this.guard.y === this.height - 1
  }

  go() {
    while (!this.guardIsOnFieldEdge) {
      this.moveGuard()
    }
  }

  get dirtyPositions() {
    return this.field.reduce((acc, row) => acc + row.filter(pos => pos === symbols.dirty).length, 0)
  }
}

const solvePart1 = (lines) => {
  const lab = new Lab(lines)
  lab.go()
  return lab.dirtyPositions
}

module.exports = { solvePart1, Lab }
