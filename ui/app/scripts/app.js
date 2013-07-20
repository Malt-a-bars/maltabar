// jshint indent:4
'use strict';

//angular.module('uiApp', ['charts'])
angular.module('uiApp', ['wijmo'])

    .config(function($routeProvider) {
        $routeProvider
            .when('/', {
                templateUrl: 'views/main.html',
                controller: 'MainCtrl'
            })
            .otherwise({
                redirectTo: '/'
            });
    });
