const path = require('node:path')
const { getFile, readFile } = require('../../../tools/js')
const { parse } = require('./parse')
const { solvePart2 } = require('./solve-part-2')

const url = 'https://adventofcode.com/2024/day/1/input'
getFile(url).then(data => {
  const { leftList, rightList } = parse(data)
  const result = solvePart2(leftList, rightList)
  console.log(result)
})
