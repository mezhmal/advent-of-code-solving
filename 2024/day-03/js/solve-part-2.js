const excludePattern = /don't\(\).*?do\(\)/g
const mulPattern = /mul\(\d{1,3},\d{1,3}\)/g

const solvePart2 = (memory) => {
  const enabledMemory = `do()${memory}`.split("don't()").map(part => `don't()${part}do()`).map(part => part.replace(excludePattern, '')).join('')
  const instructions = Array.from(enabledMemory.matchAll(mulPattern), (x) => x[0])
  const multipliers = instructions.map(instruction => Array.from(instruction.matchAll(/\d{1,3}/g), (x) => Number.parseInt(x[0], 10)))
  return multipliers.reduce((acc, [m1, m2]) => acc + m1 * m2, 0)
}

module.exports = { solvePart2 }
