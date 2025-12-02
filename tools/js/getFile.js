const session = '53616c7465645f5f157decf2d7f3d756d6b1c0dfd2902aef874c32c3ce930a47ac3457097487b6c9673eb6e37f7befb54ab0571bfac7cf73c46b975255a0d933'

const getFile = async (url) => {
    const response = await fetch(url,  {
        headers: {
            cookie:  `session=${session}`
        }
    })
    return response.text()
}

module.exports = { getFile }
