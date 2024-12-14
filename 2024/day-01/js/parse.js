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
