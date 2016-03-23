% Reflect centers
% Reflect the centers east-west

clear;clc;close all;

load('centers_Amalia.mat')

%rC = [Centers_turbine(:,1) * -1 + max(Centers_turbine(:,1))
%Centers_turbine(:,2)]; (X only)
rC = [Centers_turbine(:,1) * -1 + max(Centers_turbine(:,1)) Centers_turbine(:,2) * -1 + max(Centers_turbine(:,2))];

figure
plot(Centers_turbine(:,2),Centers_turbine(:,1),'bo')
hold all
%plot(rC(:,1),rC(:,2),'rx')
legend('Reflected')
saveas(gcf,'Reflected.png')
axis equal

for r = 1:length(rC)
    fprintf('%.02f,',rC(r,1));
end
fprintf('\n')

for r = 1:length(rC)
    fprintf('%.02f,',rC(r,2));
end
fprintf('\n')