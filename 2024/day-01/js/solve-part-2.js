const solvePart2 = (leftList, rightList) => leftList.reduce((acc, value) => acc + value * rightList.filter(v => v === value).length, 0)

module.exports = { solvePart2 }
