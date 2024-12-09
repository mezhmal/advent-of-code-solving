const session = '53616c7465645f5fc2201a5eb86dc12398b1a62a706449b8dedf4a31b2662e3064605277c593bdc9d05cdde4a995f32e46c944d8032f9d26e4a2a89c26cfb835'

const getFile = async (url) => {
    const response = await fetch(url,  {
        headers: {
            cookie:  `session=${session}`
        }
    })
    return response.text()
}

module.exports = { getFile }
