var URLS = {"get": "http://localhost:5000/get", "post": "http://localhost:5000/post"};

function paldi_post(data, callback) {

    $.ajax({
        type: "POST",
        url: URLS.post,
        data: data,
        success: function (data) {
            console.log(data)
            toast(data)
            if (callback && typeof(callback) === "function") {

                callback(data)
            }

        },
        error: function (data) {
            console.log(data)
            toast({mystatcode: "ERROR", mystat: "Server Unavailable."})
        },
        dataType: "json"
    })
}

function paldi_get(data, URL, callback) {
    if (URL === undefined) {
        URL = URLS.get;
    }

    $.ajax({
        type: "GET",
        url: URL,
        data: data,
        success: function (data) {
            console.log(data)
            toast(data)
            if (callback && typeof(callback) === "function") {

                callback(data)
            }
        },
        error: function (data) {
            console.log(data)
            toast({mystatcode: "ERROR", mystat: "Server Unavailable."})
        },
        dataType: "json"
    })
}

function toast(data) {
    //{detected_text: Array(2), mystatcode: "OCR0", mystat: "Success."}
    var title = data.mystat
    var scode = data.mystatcode.substr(data.mystatcode.length - 1)
    var toastBody = "Status code: " + data.mystatcode

    if (scode == 'S') {
        scode = "success"
    } else if (scode == 'I') {
        scode = "info"

    } else if (scode == 'W') {
        scode = "warning"

    } else if (scode == 'D') {
        scode = "error"

    } else {
        scode = "error"

    }


    toastr[scode](toastBody, title)
}
