const path = require('node:path')
const { getFile, readFile } = require('../../../tools/js')
const { parse } = require('./parse')
const { solvePart1 } = require('./solve-part-1')

const url = 'https://adventofcode.com/2024/day/2/input'
getFile(url).then(data => {
  const reports = parse(data)
  const result = solvePart1(reports)
  console.log(result)
})
