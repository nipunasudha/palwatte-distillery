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