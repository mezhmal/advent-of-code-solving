const path = require('node:path')
const { expect, test } = require('@jest/globals')
const { getFile, readFile } = require('../../../tools/js')
const { parse } = require('./parse')
const { solvePart1 } = require('./solve-part-1')

test('day 5. part 1 (short test)', async () => {
  const filename = path.join(__dirname, 'test.txt')
  const data = await readFile(filename)
  const lines = parse(data)
  const result = solvePart1(lines)
  expect(result).toBe(143)
})

test('day 5. part 1 (full test)', async () => {
  const url = 'https://adventofcode.com/2024/day/5/input'
  const data = await getFile(url)
  const letters = parse(data)
  const result = solvePart1(letters)
  expect(result).toBe(5639)
})
