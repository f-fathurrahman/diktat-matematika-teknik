% clear all; close all;

x = [0, 1, 2];
y = [3, 5, 6, 7];

[x, y] = meshgrid(x, y)

z = x + 1i*y
w = z.^2

