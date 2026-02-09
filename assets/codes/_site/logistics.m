// adapted for octave/matlab using claude;
// you can run it online at https://octave-online.net
// or in matlab

yrs = linspace(1790, 1950, 17);
pop = [3.929, 5.308, 7.240, 9.638, 12.866, 17.069, 23.192, ...
       31.433, 38.558, 50.156, 62.948, 75.996, 91.972, 105.711, ...
       122.775, 131.669, 150.697];
P0 = 3.929;
a = 0.0313395;
b = 0.000158863;

population = @(t) a ./ (b + (a / P0 - b) .* exp(-a * (t - 1790)));

t = linspace(1790, 2025, 200);
plot(t, population(t), 'r'); % Use 'r' for red color
hold on;
scatter(yrs, pop, 'filled');
hold off;
xlabel('Year');
ylabel('Population (millions)');
title('Population Growth Over Time');
grid on;
figure;

abs_errs = abs(pop - population(yrs));
scatter(yrs, abs_errs, 'filled', 'DisplayName', 'Absolute Error (mil)');
hold on;
rel_errs = abs(pop - population(yrs)) ./ pop * 100;
scatter(yrs, rel_errs, 'filled', 'DisplayName', 'Relative Error (%)');
legend show;
hold off;
xlabel('Year');
ylabel('Error');
title('Errors in Population Estimates');
grid on;

