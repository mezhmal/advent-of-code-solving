const path = require('node:path')
const { expect, test } = require('@jest/globals')
const { getFile, readFile } = require('../../../tools/js')
const { parse } = require('./parse')
const { solvePart2 } = require('./solve-part-2')

test('day 5. part 2 (short test)', async () => {
  const filename = path.join(__dirname, '../test.txt')
  const data = await readFile(filename)
  const lines = parse(data)
  const result = solvePart2(lines)
  expect(result).toBe(123)
})

test('day 5. part 2 (full test)', async () => {
  const url = 'https://adventofcode.com/2024/day/5/input'
  const data = await getFile(url)
  const letters = parse(data)
  const result = solvePart2(letters)
  expect(result).toBe(5273)
})
