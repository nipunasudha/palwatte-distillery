$(function () {
})

var dataObj = {'cmd': 'PRINT', 'data': ["any", "thing", "here"]}
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

function reloadIframe() {
    // hackishly force iframe to reload
    var iframe = document.getElementById("photo-iframe");
    iframe.src = iframe.src;
}