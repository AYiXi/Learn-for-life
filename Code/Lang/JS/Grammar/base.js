// foreach
names.forEach(element => {
    results[element] = []
    // 不能用 results.element
})

// ajax
$.ajax({
    url: 'http://192.168.3.21:9001/?shouquanhao=CN209384670U',
    type: 'GET',
    // jsonpCallback:'test',
    dataType: 'jsonp',
    success: function (data) {
        console.log(data)
    }
});