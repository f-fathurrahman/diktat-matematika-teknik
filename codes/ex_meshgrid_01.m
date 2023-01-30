% clear all; close all;

x = linspace(-5.0, 5.0, 100);
y = linspace(-5.0, 5.0, 100);

[X, Y] = meshgrid(x, y);

Z = X + 1i*Y;
W = Z.^2;

