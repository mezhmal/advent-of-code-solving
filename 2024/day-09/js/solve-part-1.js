const getAntennaPositions = (lines) => {
  const antennaPositions = []
  for (let y = 0; y < lines.length; y++) {
    for (let x = 0; x < lines[0].length; x++) {
      if (/\w/.test(lines[y][x])) {
        antennaPositions.push({ frequency: lines[y][x], x, y })
      }
    }
  }
  return antennaPositions
}

const solvePart1 = (lines) => {
  const antennaPositions = getAntennaPositions(lines)
  console.log(antennaPositions)
  return 14
}
module.exports = { solvePart1 }
