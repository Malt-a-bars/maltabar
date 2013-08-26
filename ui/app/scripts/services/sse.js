// jshint indent:4
'use strict';

angular.module('maltabar', [], function($provide) {
    $provide.factory('sse', [ '$rootScope', function($rootScope) {

        var model;

        // handles the callback from the received event
        var handleCallback = function (msg) {
            $rootScope.$apply(function () {
                console.log('model before: ', model);
                console.log('msg.data: ', msg.data);
                var update = JSON.parse(msg.data);
                model = update;
                console.log('model after:', model);
            });
        };

        return function(url, modelToUpdate) {
            model = modelToUpdate;
            var source = new EventSource(url);
            source.addEventListener('message', handleCallback, false);

        }

    }]);
});