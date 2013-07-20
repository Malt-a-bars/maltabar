// jshint indent:4
'use strict';

//Person class
function Person(data) {
    this.ID = data.ID;
    this.Company = data.Company;
    this.Name = data.Name;
    this.Sales = data.Sales;
}

angular.module('uiApp')
    .controller('MainCtrl', ['$scope', '$http', '$log',
        function($scope, $http, $log) {

            $scope.list = [
                new Person({
                    ID: "ANATR",
                    Company: "Ana Trujillo Emparedados y helados",
                    Name: "Ana Trujillo",
                    Sales: 8900
                }),
                new Person({
                    ID: "ANTON",
                    Company: "Antonio Moreno Taqueria",
                    Name: "Antonio Moreno",
                    Sales: 4500
                }),
                new Person({
                    ID: "AROUT",
                    Company: "Around the Horn",
                    Name: "Thomas Hardy",
                    Sales: 7600
                }),
                new Person({
                    ID: "BERGS",
                    Company: "Berglunds snabbkop",
                    Name: "Christina Berglund",
                    Sales: 3200
                })
            ];

            $scope.probes = [];
            $http.get('/api/v1/probes')
                .success(function(res) {
                    $scope.probes = res.probes;
                });

            //$http.get('views/basicAreaChart.json').success(function(data) {
                //$scope.exampleChart = data;
                //$log.log('chart set to:', data);
            //});

        }
    ]);