
var express        = require("express"),
    app            = express(),
    bodyParser     = require("body-parser"),
    methodOverride = require("method-override");

// Example Route
var router = express.Router();
router.get('/', function(req, res) {
    res.send("Hello world!");
});
app.use(router);

// Start server
app.listen(process.env.NODEJS_PORT, function() {
    console.log("Node server running on http://localhost:"+process.env.NODEJS_PORT);
});
