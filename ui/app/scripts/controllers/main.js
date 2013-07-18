'use strict';

// return the chart object
function get_chart() {
    return {
        xAxis: {
            categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        },

        plotOptions: {
            series: {
                cursor: 'pointer',
                point: {
                    events: {
                        click: function() {
                            alert ('Category: '+ this.category +', value: '+ this.y);
                        }
                    }
                }
            }
        },

        series: [{
            data: [29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4]
        }]
    };
}

angular.module('uiApp')
.controller('MainCtrl', ['$scope', '$http', '$log', function ($scope, $http, $log) {

    $scope.probes = [];
    //  $http.get('/api/v1/probes')
    //  .success(function(res) {
    //   $scope.probes = res.probes;
    // });

    // $http.get("views/basicAreaChart.json").success(function(data) {
    //   $scope.example_chart = data;
    //   $log.log('chart set');
    //   //console.log($scope.basicAreaChart);
    // });

    $scope.example_chart = get_chart();


}]);