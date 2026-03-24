% See the slides posted on canvas for problems

% Example 1
f = @(t,y) -3*y + exp(-t); % y'=f(t,y)
[tt,yy] = ode45(f,[0,2],1);
plot(tt,yy)
yy(end)


% Example 2
f = @(t,z) [z(2);-7*sin(z(1))];
[tt,zz] = ode45(f,[0,20],[3;0]);
figure
plot(tt,zz(:,1),'b','DisplayName','\theta(t) (nonlinear)')
hold on
plot(tt,zz(:,2),'r','DisplayName','d\theta/dt')
% analytic linearized solution: theta(t)=3*cos(sqrt(7)t)
plot(tt,3 * cos(sqrt(7).*tt),'k--','DisplayName','\theta_{linear}')
hold off
xlabel('t')
legend('Location','best')

% Example 3
f = @(t,z) [z(2);-z(2)-z(1)-(z(1))^3];
[tt,zz] = ode45(f,[0,20],[-3;8]);
figure
plot(tt,zz(:,1),'b','DisplayName','x(t)')
hold on


