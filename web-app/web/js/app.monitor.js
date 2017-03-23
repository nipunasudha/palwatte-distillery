var interval
$(function () {
    manualFetch()
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


function autoFetch() {
    fetchData()
    interval = setInterval(fetchData, 600)
}

function manualFetch() {
    clearInterval(interval);
    fetchData();
}