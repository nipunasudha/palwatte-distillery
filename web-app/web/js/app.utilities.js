var URLS = {"get": "http://localhost:5000/get", "post": "http://localhost:5000/post"};

function paldi_post(data, callback) {
    $.ajax({
        type: "POST",
        url: URLS.post,
        data: data,
        success: function (data) {
            // console.log(data)

            if (callback && typeof(callback) === "function") {

                callback(data)
            }

        },
        error: function () {
            console.log("Error occured!")
        },
        dataType: "json"
    })
}

function paldi_get(data, callback) {
    $.ajax({
        type: "GET",
        url: URLS.get,
        data: data,
        success: function (data) {
            // console.log(data)
            if (callback && typeof(callback) === "function") {

                callback(data)
            }
        },
        error: function () {
            console.log("Error occured!")
        },
        dataType: "json"
    })
}

