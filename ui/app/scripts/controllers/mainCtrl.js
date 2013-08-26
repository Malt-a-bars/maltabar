// jshint indent:4
'use strict';

angular.module('uiApp')
.controller('MainCtrl', ['$scope', '$http', '$log', 'sse',
    function($scope, $http, $log, sse) {
        $scope.model = {};
        $scope.model.temperatures = [];

        $http.get('/api/v1/probes')
        .success(function(res) {
            $scope.model.temperatures = res.probes;
            $log.log('forced load temperatures: ', $scope.model.temperatures);
        });

        $scope.sse = sse('/api/v1/stream', $scope.model);
    }
    ]);