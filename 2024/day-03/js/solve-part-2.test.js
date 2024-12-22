const path = require('node:path')
const { expect, test } = require('@jest/globals')
const { getFile, readFile } = require('../../../tools/js')
const { parse } = require('./parse')
const { solvePart2 } = require('./solve-part-2')

test('day 3. part 2 (short test)', async () => {
  const filename = path.join(__dirname, 'test-2.txt')
  const data = await readFile(filename)
  const reports = parse(data)
  const result = solvePart2(reports)
  expect(result).toBe(48)
})

test('day 3. part 2 (full test)', async () => {
  const url = 'https://adventofcode.com/2024/day/3/input'
  const data = await getFile(url)
  const reports = parse(data)
  const result = solvePart2(reports)
  expect(result).toBe(82857512)
})
