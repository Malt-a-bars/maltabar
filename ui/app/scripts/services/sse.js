// jshint indent:2
'use strict';

angular.module('maltabar', [])
.factory('sse', [function() {
	var source;
	if(typeof(EventSource)!=='undefined') {
		source = new EventSource('/api/v1/stream');
		return {
			on: function(event, cb) {
				source.addEventListener(event, cb, false);
			}
		};
	}
	return { on: angular.noop };
}]);
