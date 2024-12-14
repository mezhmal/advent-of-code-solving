const path = require('node:path')
const { expect, test } = require('@jest/globals')
const { getFile, readFile } = require('../../../tools/js')
const { parse } = require('./parse')
const { solvePart2 } = require('./solve-part-2')

test('day 1. part 2 (short test)', async () => {
  const filename = path.join(__dirname, 'test.txt')
  const data = await readFile(filename)
  const { leftList, rightList } = parse(data)
  const result = solvePart2(leftList, rightList)
  expect(result).toBe(31)
})

test('day 1. part 2 (full test)', async () => {
  const url = 'https://adventofcode.com/2024/day/1/input'
  const data = await getFile(url)
  const { leftList, rightList } = parse(data)
  const result = solvePart2(leftList, rightList)
  expect(result).toBe(19678534)
})
