const { parseRulesAndUpdates, getRules, checkIfUpdateCorrectlyOrdered, getMiddleNumber } = require("./solve-part-1")

const checkIfUpdateIncorrectlyOrdered = (update) => !checkIfUpdateCorrectlyOrdered(update)

const orderIncorrectlyOrderedUpdate = (update) => {
  let correctlyOrderedUpdate = [...update]
  while (checkIfUpdateIncorrectlyOrdered(correctlyOrderedUpdate)) {
    for (let i = 0; i < correctlyOrderedUpdate.length - 1; i++) {
      const [before] = getRules(correctlyOrderedUpdate[i])
      if (before.includes(correctlyOrderedUpdate[i + 1])) {
        [correctlyOrderedUpdate[i], correctlyOrderedUpdate[i + 1]] = [correctlyOrderedUpdate[i + 1], correctlyOrderedUpdate[i]]
      }
    }
  }
  return correctlyOrderedUpdate
}

const solvePart2 = (lines) => {
  const [_, updates] = parseRulesAndUpdates(lines)
  const incorrectlyOrderedUpdates = updates.filter(checkIfUpdateIncorrectlyOrdered)
  const middleNumbers = incorrectlyOrderedUpdates.map(orderIncorrectlyOrderedUpdate).map(getMiddleNumber)

  return middleNumbers.reduce((a, b) => a + b, 0)
}

module.exports = { solvePart2 }
