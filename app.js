var io   = require('socket.io')(server),
    url  = require('url'),
    sys  = require('sys'),
    express = require('express'),
    http=require('http');

var app = express();
var server = http.createServer(app);
server.listen(3000);

app.use(express.static('public'));
app.engine('.html', require('ejs').__express);
app.set('views', __dirname + '/public/views');
app.set('view engine', 'html');

app.get('/', function(req, res){
    res.render('index');
});
app.get('/about', function(req, res){
    res.render('about');
});

app.listen(4000);
