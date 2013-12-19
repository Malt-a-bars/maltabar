// jshint indent:2
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

		sse.on('message', function(msg) {
			var data = JSON.parse(msg.data);
			console.log('sse message received with data: ', data);
			if (data.temperatures) {
				console.log('the message contains temperatures: ', data.temperatures);
				$scope.model.temperatures = data.temperatures;
				$scope.$apply();
			}
		});
	}
]);