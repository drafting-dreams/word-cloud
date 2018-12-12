const express = require('express')
const app = express()
const port = process.env.PORT || 3000

app.get('/', function (req, resp) {
  resp.sendFile(`${__dirname}/dist/index.html`)
})

app.use(express.static('dist'), express.static('dist'))

app.get('/api/wordCloud', function(req, res) {
  const fileName = req.query.fileName
  const { spawn } = require("child_process")
  const pythonProcess = spawn('python',["wd.py", fileName])
  console.log('start spawn')

  let re
  pythonProcess.stdout.on('data', data => {
    re = decodeURIComponent(escape(data)).split("'")[1]
  })
  pythonProcess.on('close', () => {
    console.log('done')
    console.log(typeof(re))
    res.send(re)
  })
})

app.get('*', function (req, resp) {
  resp.redirect('/')
})

app.listen(port, () => console.log(`app listening on port ${port}!`))