// dependencies
var Io = require('socket.io'),
    redis = require('redis'),
    cookie = require('cookie'),
    serialize = require('node-serialize'),
    clientRedis = redis.createClient(6379, 'django-node-redis');
clientRedis.select(1);
// module
var Socket = function(config){
    this.io = Io.listen(3000);
};
// run socket
Socket.prototype.run = function(){
    var self = this;
    // set auth
    this.io.use(function(socket, next) {
       self.auth(socket, next);
    });
    // when a client connects
    this.io.sockets.on('connection', function(socket){
        // event join
        socket.emit('join', socket.handshake.user);
    });
};
// authentication
Socket.prototype.auth = function(socket, next){
    // get cookie token
    var userCookie = cookie.parse(socket.request.headers.cookie);
    // redis validation
    clientRedis.get('session:' + userCookie.nodejskey, (err, session) => {
        // error or not session
        if (err || !session) {
            return next(new Error('Not authorized.'));
        }
        // config session
        session = serialize.unserialize(session);
        socket.handshake.user = session.user;
        if (session.user == 'diegoug'){
            next()
        } else {
            console.log('no soy diegoug');
            return next(new Error('Not authorized.'));
        }
    });
};
// run server as stand alone
if(module.parent){
    // export module
    module.exports = Socket;
}else{
    var socket = new Socket();
    socket.run();
}