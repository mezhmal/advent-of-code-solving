const parse = (data) => data.split('\n').filter(x => x).join('')

module.exports = { parse }
