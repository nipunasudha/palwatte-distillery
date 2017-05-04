$(function () {

})
function gettest() {
    alert("get test")
}
var app = new Vue({
    el: '#app',
    data: {
        message: 'Hello Vue!',
        rules: [{
            variableID: "V001",
            variableName: "Fermenter Temperature",
            minDangerValue: 20,
            minWarningValue: 30,
            maxWarningValue: 60,
            maxDangerValue: 80,
            priority: "High"
        }, {
            variableID: "V002",
            variableName: "Blending Speed",
            minDangerValue: null,
            minWarningValue: null,
            maxWarningValue: 2000,
            maxDangerValue: 4500,
            priority: "Low"
        }, {
            variableID: "V003",
            variableName: "Ethyl Concentration",
            minDangerValue: 0.732,
            minWarningValue: 0.655,
            maxWarningValue: 0.932,
            maxDangerValue: 1.347,
            priority: "Low"
        }]
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