var btn = document.getElementById('btn')
var container = document.getElementById('outcontainer')

var url = 'http://127.0.0.1:8000/'

$.ajax({
    method: 'GET',
    url: url,
    success: function (data) {
        console.log(data.title);
    },
    error: function(error) {
        console.log(error)
    }
})

btn.addEventListener('click', function() {
    var ourRequest = new XMLHttpRequest();
    ourRequest.open('GET', url);
    ourRequest.onload = function() {
        console.log(ourRequest.responseText)
        var ourData = JSON.parse(ourRequest.responseText)
        console.log(ourData);
    }
    ourRequest.send();
})

