const parse = (data) => data.split('\n').filter(line => line.length > 0).map((line) => line.split(' ').map(value => Number.parseInt(value, 10)))

module.exports = { parse }
