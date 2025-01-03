const cache = []
const rules = []
const updates = []

const parseRulesAndUpdates = (lines) => {
  for (const line of lines) {
    if (line.includes('|')) {
      rules.push(line.split('|').map(x => +x))
    } else {
      updates.push(line.split(',').map(x => +x))
    }
  }
}

const getRules = (number) => {
  if (cache[number] !== undefined) {
    return cache[number]
  }

  const before = rules.filter(([_, second]) => second === number).map(([first, _]) => first)
  const after = rules.filter(([first, _]) => first === number).map(([_, second]) => second)
  cache[number] = [before, after]
  return cache[number]
}

const checkIfUpdateCorrectlyOrdered = (update) => {
  const numbersBefore = []
  const numbersAfter = [...update]

  while (numbersAfter.length) {
    const number = numbersAfter.shift()
    const [rulesBefore, rulesAfter] = getRules(number)

    if (numbersBefore.some(nb => rulesAfter.includes(nb))) {
      return false
    }
    if (numbersAfter.some(na => rulesBefore.includes(na))) {
      return false
    }
    numbersBefore.push(number)
  }

  return true
}

const getMiddleNumber = (update) => update[(update.length - 1) / 2]

const solvePart1 = (lines) => {
  parseRulesAndUpdates(lines)
  const correctlyOrderedUpdates = updates.filter(checkIfUpdateCorrectlyOrdered)
  const middleNumbers = correctlyOrderedUpdates.map(getMiddleNumber)

  return middleNumbers.reduce((a, b) => a + b, 0)
}

module.exports = { solvePart1 }
