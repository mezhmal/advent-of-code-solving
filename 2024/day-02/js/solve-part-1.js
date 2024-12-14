const splitByPairs = (report) => report.slice(0, -1).map((value, i) => [value, report[i + 1]])

const isReportSafe = (report) => {
  const pairs = splitByPairs(report)
  const [firstValue, secondValue] = pairs[0]
  if (firstValue > secondValue) {
    return pairs.every(([v1, v2]) => v1 > v2 && (v1 - v2) < 4)
  }
  if (firstValue < secondValue) {
    return pairs.every(([v1, v2]) => v1 < v2 && (v2 - v1) < 4)
  }
  return false
}

const solvePart1 = (reports) => reports.filter(isReportSafe).length

module.exports = { solvePart1 }
