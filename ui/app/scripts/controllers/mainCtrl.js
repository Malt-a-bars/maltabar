// jshint indent:2
'use strict';

angular.module('uiApp')
.controller('MainCtrl', ['$scope', '$http', '$log', 'sse',
	function($scope, $http, $log, sse) {
		$scope.model = {};
		$scope.model.temperatures = [];
		$scope.model.heating = false;

		// Heater

		$http.get('/api/v1/is_heating')
		.success(function(res) {
			$scope.model.heating = res.value;
			$log.log('is_heating: ', $scope.model.heating);
		});

		$scope.heaterOn = function() {
			$http.get('/api/v1/heater/on')
			.success(function(res) {
				$scope.model.heating = true;
				$log.log('setting heater on');
			});
		};

		$scope.heaterOff = function() {
			$http.get('/api/v1/heater/off')
			.success(function(res) {
				$scope.model.heating = false;
				$log.log('setting heater off');
			});
		};

		$scope.toggleHeater = function() {
			if ($scope.model.heating) {
				$scope.heaterOff();
			} else {
				$scope.heaterOn();
			}
		};


		// Temperature probes

		$scope.refreshTemps = function() {
			$http.get('/api/v1/probes')
			.success(function(res) {
				$scope.model.temperatures = res.probes;
				$log.log('forced load temperatures: ', $scope.model.temperatures);
			});
		}

		$scope.refreshTemps()


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