function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta

temp = X * theta;
temp1 = ones(size(temp)).*e.^(temp);
temp2 = 1 ./temp1;
temp3 = 1 + temp2;
H = 1 ./ temp3;

firstPart = (-y).*log(H);
secondPart = (1-y).*log(1-H);
finalPart = firstPart - secondPart;
s = size(theta)(1);
temp4 = theta(2:s).^2;
temp5 = sum(temp4);
temp6 = lambda / (2*m);
tempLam = temp6.*temp5;
J = (sum(finalPart)/m) + tempLam;

temp7 = (H-y)'* X;
temp8 = temp7'./m;

temp9 = lambda/ m;
temp10 = temp9 .* theta;
grad(1) = temp8(1);
grad(2:s) = temp8(2:s) + temp10(2:s);


% =============================================================

end
