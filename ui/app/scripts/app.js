// jshint indent:4
'use strict';

angular.module('uiApp', ['wijmo', 'maltabar'])
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
