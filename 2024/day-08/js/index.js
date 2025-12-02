const path = require('node:path')
const { getFile, readFile } = require('../../../tools/js')
const { parse } = require('./parse')
const { solvePart1 } = require('./solve-part-1')

const filename = path.join(__dirname, 'test.txt')
readFile(filename).then(data => {
  const lines = parse(data)
  const result = solvePart1(lines)
  console.log(result)
})

// const url = 'https://adventofcode.com/2024/day/8/input'
// getFile(url).then(data => {
//   const lines = parse(data)
//   const result = solvePart1(lines)
//   console.log(result)
// })
