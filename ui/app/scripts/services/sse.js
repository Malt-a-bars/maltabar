// // define the module we're working with
// var app = angular.module('sse', []);

// // define the ctrl
// function statCtrl($scope) {

//     // the last received msg
//     $scope.msg = {};

//     // handles the callback from the received event
//     var handleCallback = function (msg) {
//         $scope.$apply(function () {
//             $scope.msg = JSON.parse(msg.data)
//         });
//     }

//     var source = new EventSource('/stats');
//     source.addEventListener('message', handleCallback, false);
// }