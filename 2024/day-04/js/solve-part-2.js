const checkXmas = (letters, colIndex, rowIndex) => {
    if (letters[rowIndex][colIndex] !== 'A') {
        return false
    }

    return (letters[rowIndex - 1][colIndex - 1] === 'M' && letters[rowIndex + 1][colIndex + 1] === 'S' ||
        letters[rowIndex - 1][colIndex - 1] === 'S' && letters[rowIndex + 1][colIndex + 1] === 'M') &&
        (letters[rowIndex - 1][colIndex + 1] === 'M' && letters[rowIndex + 1][colIndex - 1] === 'S' ||
            letters[rowIndex - 1][colIndex + 1] === 'S' && letters[rowIndex + 1][colIndex - 1] === 'M')
}

const solvePart2 = (letters) => {
    const rows = letters.length
    const cols = letters[0].length

    if (rows <= 3 || cols <= 3) {
        return 0
    }

    let counter = 0
    for (let colIndex = 1; colIndex < cols - 1; colIndex++) {
        for (rowIndex = 1; rowIndex < rows - 1; rowIndex++) {
            if (checkXmas(letters, colIndex, rowIndex)) {
                counter++
            }
        }
    }

    return counter
}

module.exports = { solvePart2 }
