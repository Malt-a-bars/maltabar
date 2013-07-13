'use strict';

angular.module('uiApp')
  .controller('MainCtrl', function ($scope, $http) {
    $scope.probes = [];
    $http.get('http://localhost:5000/api/v1/probes')
    .success(function(res) {
        $scope.probes = res.probes;
      });

  });
