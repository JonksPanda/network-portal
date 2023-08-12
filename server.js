const http = require('http');
const fs = require('fs');
//var links = fs.readFileSync("./data/sites.json");

const PORT = 80;


fs.readFile('./html/index.html', function (err, html) {

    if (err) throw err;

    http.createServer(function (request, response) {
        response.writeHeader(200, { "Content-Type": "text/html" });
        response.write(html);
        response.end();
    }).listen(PORT);
});