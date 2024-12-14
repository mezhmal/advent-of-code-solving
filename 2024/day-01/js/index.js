const path = require('node:path')
const { getFile, readFile } = require('../../../tools/js')
const { solvePart2 } = require('./solve-part-2')

const parse = (data) => {
  const leftList = []
  const rightList = []
  for (const item of data.split('\n')) {
    const [left, right] = item.split('   ')
    if (left && right) {
      leftList.push(Number.parseInt(left, 10))
      rightList.push(Number.parseInt(right, 10))
    }
  }
  return { leftList, rightList }
}

module.exports = { parse }

const url = 'https://adventofcode.com/2024/day/1/input'
getFile(url).then(data => {
  const { leftList, rightList } = parse(data)
  const result = solvePart2(leftList, rightList)
  console.log(result)
})
