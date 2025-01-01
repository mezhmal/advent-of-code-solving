const getVerticalLines = (letters) => {
  const rows = letters.length
  const cols = letters[0].length

  const lines = []
  for (let colIndex = 0; colIndex < cols; colIndex++) {
    const line = []
    for (let rowIndex = 0; rowIndex < rows; rowIndex++) {
      line[rowIndex] = letters[rowIndex][colIndex]
    }
    lines[colIndex] = line.join('')
  }
  return lines
}

const getDiagonalSlashLines = (letters) => {
  const rows = letters.length
  const cols = letters[0].length

  const lines = []
  let rowIndex = 0
  let colIndex = 0
  while (rowIndex < rows && colIndex < cols) {
    let i = 0
    const line = []
    while ((rowIndex - i) >= 0 && (colIndex + i) < cols) {
      line[i] = letters[rowIndex - i][colIndex + i]
      i++
    }
    lines.push(line.join(''))

    if (rowIndex < (rows - 1)) {
      rowIndex++
    } else {
      colIndex++
    }
  }
  return lines
}

const getDiagonalBackSlashLines = (letters) => {
  const rows = letters.length
  const cols = letters[0].length

  const lines = []
  let rowIndex = rows - 1
  let colIndex = 0
  while (rowIndex >= 0 && colIndex < cols) {
    let i = 0
    const line = []
    while ((rowIndex + i) < rows && (colIndex + i) < cols) {
      line[i] = letters[rowIndex + i][colIndex + i]
      i++
    }
    lines.push(line.join(''))

    if (rowIndex > 0) {
      rowIndex--
    } else {
      colIndex++
    }
  }
  return lines
}

const count = (line) => (line.match(/XMAS/g) || []).length

const countInLines = (lines) => lines.reduce((acc, line) => acc + count(line), 0)

const solvePart1 = (letters) => {
  const horizontalDirect = [...letters]
  const horizontalReversed = horizontalDirect.map(str => str.split('').reverse().join(''))

  const verticalDirect = getVerticalLines(letters)
  const verticalReversed = verticalDirect.map(str => str.split('').reverse().join(''))

  const diagonalSlashDirect = getDiagonalSlashLines(letters)
  const diagonalSlashReversed = diagonalSlashDirect.map(str => str.split('').reverse().join(''))

  const diagonalBackSlashDirect = getDiagonalBackSlashLines(letters)
  const diagonalBackSlashReversed = diagonalBackSlashDirect.map(str => str.split('').reverse().join(''))

  return countInLines(horizontalDirect) + countInLines(horizontalReversed) +
    countInLines(verticalDirect) + countInLines(verticalReversed) +
    countInLines(diagonalSlashDirect) + countInLines(diagonalSlashReversed) +
    countInLines(diagonalBackSlashDirect) + countInLines(diagonalBackSlashReversed)
}

module.exports = { solvePart1 }
