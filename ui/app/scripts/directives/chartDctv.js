/*global $:false */
/*global Highcharts:false */
// jshint indent:4
'use strict';

// adapted from https://github.com/rootux/angular-highcharts-directive

//angular.module('charts', [])
angular.module('uiApp')
    .directive('highChart', ['$log',
        function($log) {
            $log.log('Initialized directive "charts"');
            return {
                restrict: 'E',
                template: '<div></div>',
                scope: {
                    chartData: '=value'
                },
                transclude: true,
                replace: true,
                link: function(scope, element, attrs) {
                    var chartsDefaults = {
                        chart: {
                            renderTo: element[0],
                            type: attrs.type || null,
                            height: attrs.height || null,
                            width: attrs.width || null
                        }
                    };

                    //Update when charts data changes
                    scope.$watch(function() {
                        return scope.chartData;
                    }, function(value) {
                        if (!value) {return;}
                        // We need deep copy in order to NOT override original chart object.
                        // This allows us to override chart data member and still the keep
                        // our original renderTo will be the same
                        var deepCopy = true;
                        var newSettings = {};
                        $.extend(deepCopy, newSettings, chartsDefaults, scope.chartData);
                        var chart = new Highcharts.Chart(newSettings);
                        $log.log('chart object:', chart);
                    });
                }
            };

        }
    ]);