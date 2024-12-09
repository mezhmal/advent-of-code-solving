const path = require('node:path')
const { expect, test } = require('@jest/globals')
const { readFile } = require('../../../tools/js')
const { solve } = require('./solve')
const { parse } = require('.')

test('day 1. part 1 (short test)', async () => {
  const filename = path.join(__dirname, 'test.txt')
  const data = await readFile(filename)
  const { leftList, rightList } = parse(data)
  const result = solve(leftList, rightList)
  expect(result).toBe(11)
})

test('day 1. part 1 (full test)', async () => {
  const filename = path.join(__dirname, 'test.txt')
  const data = await readFile(filename)
  const { leftList, rightList } = parse(data)
  const result = solve(leftList, rightList)
  expect(result).toBe(2031679)
})
