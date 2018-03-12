import jsonp from 'common/js/jsonp'
import axios from 'axios'

const options = {
  param: 'jsonCallback'
}

export function getBgImage() {
  const url = 'https://bing.ioliu.cn/v1'

  const data = {
    w: 1920,
    h: 1080,
    d: 0,
    type: 'json'
  }

  return jsonp(url, data)
}

export function getWeather() {
  let ip =''

  return getIp().then((res) => {
    ip = res.query

    return axios.get('/api/weather', {
      params: {ip: ip}
    }).then((res) => {
      return Promise.resolve(res.data)
    })
  })
}

function getIp() {
  const url = 'http://ip-api.com/json'

  return jsonp(url)
}
