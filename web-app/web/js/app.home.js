$(function () {

    var data = {
        // A labels array that can contain any sort of values
        labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
        // Our series array that contains series objects or in this case series data arrays
        series: [
            [5, 2, 4, 2, 0, 5, 2, 4, 2, 0],
            [3, 7, 7, 7, 1, 2, 3, 8, 0, 9],
            [13, 17, 17, 17, 11, 12, 13, 18, 10, 9],
        ]
    };

// Create a new line chart object where as first parameter we pass in a selector
// that is resolving to our chart container element. The Second parameter
// is the actual data object.
    new Chartist.Line('.ct-chart', data);


})
