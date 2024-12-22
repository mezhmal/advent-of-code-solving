const { solvePart1 } = require("./solve-part-1")

const enabler = 'do()'
const disabler = "don't()"
const excludePattern = new RegExp(`${disabler}.*?${enabler}`, 'g')

const solvePart2 = (memory) => {
  const enabledMemory = `${enabler}${memory}`
    .split(disabler)
    .map(part => `${disabler}${part}${enabler}`)
    .map(part => part.replace(excludePattern, ''))
    .join('')
  return solvePart1(enabledMemory)
}

module.exports = { solvePart2 }
