function request_ocr() {
    $.ajax({
        url: 'http://localhost:5000/get-ocr',
        method: 'GET',
        success: function (data) {
            var data_str = JSON.stringify(eval('(' + data + ')'));
            var data_obj = JSON.parse(data_str);
            console.log("--- SnapOCR ---")
            console.log(data_obj)
        },
        error: function (error) {
            alert(JSON.stringify(error));
        }
    });
}

