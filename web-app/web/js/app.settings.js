var dataObj = {'cmd': 'PRINT', 'data': ["any", "thing", "here"]}

function backendExit() {
    paldi_post({'cmd': 'EXIT', 'data': ''}, function (data) {
        console.log(data)
    })
}

function backendCrop() {
    paldi_post({'cmd': 'CROP', 'data': ''}, null)
}

function fetchData() {
    console.log("======req sent======")
    // console.log(data)

    // $("#photo").prop('src', "/img/photoFromCam.jpg?" + new Date().getTime())

    paldi_post(dataObj, function (data) {
        console.log(data)
        $('#count').text("Fetched " + data['data'][0] + " resposes from camera")
        $("#photo").prop('src', outputPath + "?" + new Date().getTime())
    })

}

function startCamera() {
    paldi_get(null, "http://localhost:5000/startcam", function () {
        location.reload()

    })
    $('#btn-startcam').prop("disabled", true);
    $('#btn-stopcam').prop("disabled", true);
}
function stopCamera() {
    paldi_get(null, "http://localhost:5000/stopcam", function () {
        location.reload()

    })
    $('#btn-stopcam').prop("disabled", true);
    $('#btn-startcam').prop("disabled", true);
}