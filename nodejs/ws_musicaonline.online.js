var request = require('request')
var cheerio = require('cheerio')
var http = require('http')
var url = require('url')
var stringify = require('json-stringify')

function getObjectStringList(htmlSource) {
  var inicio = 'var playlist'
  var fin = ');'
  var str = htmlSource
  inicio = str.lastIndexOf(inicio)
  fin = str.indexOf(fin, inicio) + fin.length
  var objetoHTML = str.substring(inicio, fin)
  return objetoHTML
}

//para acceder: localhost:9999/?enlace=
console.log('Escuchando...  curl "http://localhost:9999/?url=http://www.musicaonline.online/de-moda.com"')
http.createServer(function(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');

  var url_parts = url.parse(req.url, true)
  var query = url_parts.query
  console.log(query)

  request.get({
    url: query.url,
  }, function(error, response, body) {
    if (!error && response.statusCode == 200) {
      //console.log(body)
      var list = getObjectStringList(body)

      function jPlayerPlaylist(objeto, lista) {
        return lista
      }

      eval(list)
        //console.log(playlist)

      res.end(stringify(playlist, null, 2, {
          offset: 2
        })) // + '\n'
    } else {
      console.log('Error :', error)
    }
  })

}).listen(9999)
