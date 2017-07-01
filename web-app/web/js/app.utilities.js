var URLS = {"get": "http://localhost:5000/get", "post": "http://localhost:5000/post"};
$(function () {
    update_info()
    setInterval(function () {
        update_info()
    }, 8000)
})
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
    if (data.mystatcode === undefined) {
        return
    }
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

function update_info() {
    /*
     {'cam_stat': True,
     'cam_height': 480.0,
     'cam_width': 640.0,
     'plat_bit': 'AMD64',
     'plat_os': 'Windows-10-10.0.15063-SP0',
     'plat_proc': 'Intel64 Family 6 Model 61 Stepping 4, GenuineIntel'}
     */

    paldi_get(null, "http://localhost:5000/get-info", function (data) {
        $("#camstat").text(data.cam_stat ? "ON" : "OFF")
        $("#camstat").css("color", data.cam_stat ? "#2ecc71" : "#e74c3c")
        $("#camstat").fadeIn(200)
        //-------------------------------------------------
        $("#sysinfo").text("")
        $("#sysinfo").append("Camera : " + (data.cam_stat ? "ON" : "OFF") + "<br>")
        $("#sysinfo").append("Frame Width : " + data.cam_width + "<br>")
        $("#sysinfo").append("Frame Height : " + data.cam_height + "<br>")
        $("#sysinfo").append("OS : " + data.plat_os + "<br>")
        $("#sysinfo").append("CPU : " + data.plat_proc + "<br>")
        $("#sysinfo").append("Architecture : " + data.plat_bit + "<br>")
    })
}