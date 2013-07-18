'use strict';


describe('Controller: MainCtrl', function () {

  // load the controller's module
  beforeEach(module('uiApp'));

  var MainCtrl,
    scope,
    httpMock;

  // Initialize the controller and a mock scope
  beforeEach(inject(function($controller, $rootScope, $httpBackend) {
    httpMock = $httpBackend;
    // create new scope
    scope = $rootScope.$new();
    // simulate response to GET /api/v1/probes
    httpMock.when('GET', '/api/v1/probes').respond({
        'probes': [{'name': 'R0', 'temperature': 65.60349898113955}]
    });
    // create controller with new scope and http mock
    MainCtrl = $controller('MainCtrl', { $scope: scope });
  }));

  it('should attach a fetched list of probles to the scope', function () {
    expect(scope.probes.length).toBe(0);
    httpMock.flush();
    expect(scope.probes.length).toBe(1);
  });
});
