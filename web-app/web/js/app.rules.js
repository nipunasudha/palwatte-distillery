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
            variableID: "V001",
            variableName: "Ethyl Concentration",
            minDangerValue: 0.732,
            minWarningValue: 0.655,
            maxWarningValue: 0.932,
            maxDangerValue: 1.347,
            priority: "Low"
        }]
    },
    methods: {

        editRule: function () {
            app.invokeEditQuestion("Ethyl Concentration")
        },
        invokeEditQuestion: function (ruleName) {
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
        deleteRule: function () {
            app.invokeDeleteQuestion("Ethyl Concentration")
        },
        invokeDeleteQuestion: function (ruleName) {
            $.Zebra_Dialog('Are you sure you want to delete the rule "' + ruleName + '"?',
                {
                    'type': 'warning',
                    'title': 'Delete Confirmation',
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
        }
    }
})