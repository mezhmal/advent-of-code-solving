const fs = require('node:fs')

const readFile = (fileName) => new Promise((resolve, reject) => {
    fs.readFile(fileName, 'utf8', (err, data) => {
        if (err) { reject(err) }
        resolve(data);
    })
})

module.exports = { readFile }
