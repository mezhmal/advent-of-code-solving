const { sum } = require('../../../tools/js')

const solve = (leftList, rightList) => {
  const sortedLeftList = leftList.sort((a, b) => a - b)
  const sortedRightList = rightList.sort((a, b) => a - b)
  const distances = sortedLeftList.map((_, i) => Math.abs(sortedRightList[i] - sortedLeftList[i]))
  return sum(distances)
}

module.exports = { solve }
