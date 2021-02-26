var express = require("express");
var app = express();

app.get("/", function(request, response){
	response.send("Some response was sent.")
});

app.listen(5000, function(){
	console.log("Server started . . .")
});