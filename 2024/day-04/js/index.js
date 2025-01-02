const path = require('node:path')
const { getFile, readFile } = require('../../../tools/js')
const { parse } = require('./parse')
const { solvePart2 } = require('./solve-part-2')

// const filename = path.join(__dirname, 'test.txt')
// readFile(filename).then(data => {
//   const letters = parse(data)
//   const result = solvePart2(letters)
//   console.log(result)
// })

const url = 'https://adventofcode.com/2024/day/4/input'
getFile(url).then(data => {
  const letters = parse(data)
  const result = solvePart2(letters)
  console.log(result)
})
