% Definim sistemul neliniar, unde 
%z(1) = x, z(2) = y
f = @(t,z) [
    z(1) - z(1)^2 - z(1)*z(2);              % x' = x - y
    2*z(2) + 2*z(1)*z(2) - z(2)^2     % y' = x + y - x^2
];

% Definim intervalul de timp de simulare
tspan = [0 10];

% Definim coordonatele inițiale ale punctelor 
init = [
    0.2 0.2;
    0.5 0.5;
    1 1;
];

figure;
hold on;

% Formăm traiectoriile punctelor definite anterior
for i = 1:size(init,1)
    [t,z] = ode45(f, tspan, init(i,:)'); 
    plot(z(:,1), z(:,2), 'LineWidth', 1.5)
end

% Afișăm punctele de echilibru
plot(0,0,'ro','MarkerSize',8,'LineWidth',2) 
plot(0,2,'ko','MarkerSize',8,'LineWidth',2) 
plot(1,0,'go','MarkerSize',8,'LineWidth',2) 
plot(-1/3,4/3,'ko','MarkerSize',8,'LineWidth',2)

xlabel('x');
ylabel('y');
title('Planul fazelor - Sistem neliniar ex 1');
grid on;

legend('pct 1','pct 2','pct 3','(0,0) punct instabil','(1,0) punct sa','(0,2) punct stabil','(-1/3,4/3) punct sa');