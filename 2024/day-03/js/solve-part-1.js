const pattern = /mul\(\d{1,3},\d{1,3}\)/g

const solvePart1 = (memory) => {
  const instructions = Array.from(memory.matchAll(pattern), (x) => x[0])
  const multipliers = instructions.map(instruction => Array.from(instruction.matchAll(/\d{1,3}/g), (x) => Number.parseInt(x[0], 10)))
  return multipliers.reduce((acc, [m1, m2]) => acc + m1 * m2, 0)
}

module.exports = { solvePart1 }
