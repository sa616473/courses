function [J, grad] = linearRegCostFunction(X, y, theta, lambda)
%LINEARREGCOSTFUNCTION Compute cost and gradient for regularized linear 
%regression with multiple variables
%   [J, grad] = LINEARREGCOSTFUNCTION(X, y, theta, lambda) computes the 
%   cost of using theta as the parameter for linear regression to fit the 
%   data points in X and y. Returns the cost in J and the gradient in grad

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost and gradient of regularized linear 
%               regression for a particular choice of theta.
%
%               You should set J to the cost and grad to the gradient.
%



tempH = X * theta;
firstPart = (tempH - (y)).^2;
finalPart = sum(firstPart);
J = finalPart / (2*m);

tempLam = lambda / (2*m);
thetaSqr = sum(theta(2:size(theta)(1)).^2);
reg = tempLam * thetaSqr;

J = J + reg;

s = size(theta)(1);
temp7 = (tempH - y)' * X;
temp8 = temp7' ./m;

temp9 = lambda / m;
temp10 = temp9 .* theta;
grad(1) = temp8(1);
grad(2:s) = temp8(2:s) + temp10(2:s);






% =========================================================================

grad = grad(:);

end
