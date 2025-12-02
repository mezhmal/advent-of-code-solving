const { sum } = require('../../../tools/js')

const operators = {
  plus: '+',
  mult: '*',
}

const parseLine = (line) => {
  const [testValue, numbers] = line.split(':')
  return {
    testValue: Number.parseInt(testValue, 10),
    numbers: numbers.trim().split(' ').map(value => Number.parseInt(value, 10))
  }
}

const combinedOperatorsCache = {}

const combineOperators = (count) => {
  if (combinedOperatorsCache[count]) {
    return combinedOperatorsCache[count]
  }

  const plusesOnly = [...Array(count).keys()].map(() => operators.plus)
  const multesOnly = [...Array(count).keys()].map(() => operators.mult)

  const result = [
    [...plusesOnly],
    [...multesOnly],
  ]
  for (let i = 1; i < count; i++) {
    result.push([...[...Array(i).keys()].map(() => operators.plus), ...[...Array(count - i).keys()].map(() => operators.mult)])
    result.push([...[...Array(i).keys()].map(() => operators.mult), ...[...Array(count - i).keys()].map(() => operators.plus)])
  }

  for (let i = 1; i < count - 1; i++) {
    const oneMult = [...plusesOnly]
    oneMult[i] = operators.mult
    result.push([...oneMult])
    const onePlus = [...multesOnly]
    onePlus[i] = operators.plus
    result.push([...onePlus])
  }
  combinedOperatorsCache[count] = result

  return result
}

const calc = (numbers, operatorSequence) => operatorSequence.reduce((acc, operator, i) => {
  switch (operator) {
    case operators.plus:
      return acc + numbers[i + 1]
    case operators.mult:
      return acc * numbers[i + 1]
    default:
      return acc
  }
}, numbers[0])

const calcVariants = (numbers) => combineOperators(numbers.length - 1).map(operatorSequence => calc(numbers, operatorSequence))

const determine = (line) => calcVariants(line.numbers).some((variant) => variant === line.testValue)

const solvePart1 = (lines) => sum(lines.map(parseLine).filter(determine).map(line => line.testValue))

module.exports = { solvePart1 }
