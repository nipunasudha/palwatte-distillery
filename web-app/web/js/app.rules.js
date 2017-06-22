$(function () {

})
function gettest() {
    alert("get test")
}
var app = new Vue({
    el: '#app',
    data: {
        rules: {}
    },
    created: function () {
        var self = this;
        $.ajax({
            url: 'http://localhost:5000/get-rules',
            method: 'GET',
            success: function (data) {
                var data_str = JSON.stringify(eval('(' + data + ')'));
                var data_obj = JSON.parse(data_str);
                console.log(data_obj)
                self.rules = data_obj.data;
            },
            error: function (error) {
                alert(JSON.stringify(error));
            }
        });

        console.log(self.rules)
        console.log("Done")
    },

    methods: {

        editRule: function (varID) {

            app.invokeEditQuestion("Ethyl Concentration", varID)
        },
        invokeEditQuestion: function (ruleName, varID) {
            $.Zebra_Dialog('Are you sure you want to edit the rule "' + ruleName + '"?',
                {
                    'type': 'warning',
                    'title': 'Edit Confirmation',
                    animation_speed_hide: 150,
                    animation_speed_show: 150,
                    'buttons': [
                        {
                            caption: 'Yes', callback: function () {

                        }
                        },
                        {
                            caption: 'No', callback: function () {
                        }
                        }
                    ]
                }
            );
        },
        deleteRule: function (varID) {
            app.invokeDeleteQuestion("Ethyl Concentration", varID)
            // alert(varID)
        },
        invokeDeleteQuestion: function (ruleName, varID) {
            $.Zebra_Dialog('Are you sure you want to delete the rule "' + ruleName + '"?',
                {
                    'type': 'warning',
                    'title': 'Delete Confirmation',
                    animation_speed_hide: 150,
                    animation_speed_show: 150,
                    'buttons': [
                        {
                            caption: 'Yes', callback: function () {
                            console.log(app.filterObject(app.rules, varID))
                            // delete app.rules[app.filterObject(app.rules, varID)];
                            app.rules.splice(app.filterObject(app.rules, varID), 1)
                        }
                        },
                        {
                            caption: 'No', callback: function () {
                        }
                        }
                    ]
                }
            );
        },
        filterObject: function (arr, searchKey) {
            for (var i = 0; i < arr.length; i++) {

                if (arr[i]["variableID"] === searchKey) {
                    return i;
                }

            }
        }
    }
})