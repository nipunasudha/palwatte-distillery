$(function () {
    setInterval(fetchData, 6000)
})
var dataObj = {'cmd': 'PRINT', 'data': ["any", "thing", "here"]}
function fetchData() {
    console.log("======req sent======")
    // console.log(data)
    // $('#count').text(data[0])
    // $("#photo").prop('src', "/img/photoFromCam.jpg?" + new Date().getTime())

    paldi_post(dataObj, function (data) {
        console.log(data)
    })

}
function backendExit() {
    paldi_post({'cmd': 'EXIT', 'data': ''}, function (data) {
        console.log(data)
    })
}

function backendCrop() {
    paldi_post({'cmd': 'CROP', 'data': ''}, function (data) {
        console.log(data)
    })
}