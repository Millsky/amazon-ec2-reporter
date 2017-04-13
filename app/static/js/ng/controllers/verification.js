var ngEC2Controllers = angular.module('ngEC2.controllers',[]);
ngEC2Controllers.controller('userLogin',['$scope','$http',function($scope,$http){
    /* OUR APPLICATION STATE VARS */
    $scope.hasSubmittedCredentials = false;
    $scope.requestPending = false;
    $scope.requestSucceeded = false;
    /* Model for AWS API KEY Input */
    $scope.AWSAPIKey = "";
    /* Model for AWS API Secret Input */
    $scope.AWSAPISecretKey = "";
    /* KEEP TRACK EC2 Resp */
    $scope.instances = [];
    /* Usually this would be broken out into another file that contains all API Access */
    $scope.submitCredentials = function(){
        var data = { "aws_access_key_id":$scope.AWSAPIKey.trim(),"aws_secret_access_key":$scope.AWSAPISecretKey.trim()};
        $scope.hasSubmittedCredentials = true;
        $scope.requestPending = true;
        $http.post('/api/ec2Info', data).then(credentialsSuccess,credintialsError);
    }
    
    function credentialsSuccess(res){
        $scope.requestPending = false;
        $scope.requestSucceeded = true;
        $scope.instances = res.data;
    }

    function credintialsError(res){
        $scope.requestPending = false;
        $scope.loginError = true;
    }


}]);

ngEC2Controllers.controller('infoTable',['$scope',function($scope){
   
}]);