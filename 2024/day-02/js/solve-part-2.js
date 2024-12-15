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

const checkReportWithTolerateSingleBadLevel = (report) => report.map((_, i) => {
  const reportCopy = [...report]
  reportCopy.splice(i, 1)
  return reportCopy
}).some(isReportSafe)

const solvePart2 = (reports) => reports.filter(checkReportWithTolerateSingleBadLevel).length

module.exports = { solvePart2 }
