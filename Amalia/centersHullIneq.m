% Reflect centers
% Reflect the centers east-west

clear;clc;close all;

load('centers_Amalia.mat')

turbineX = Centers_turbine(:,2)+2000.;
turbineY = Centers_turbine(:,1)+2000.;

figure
plot(turbineX,turbineY,'bo')
hold all

axis equal

V = [turbineX, turbineY];

k = convhulln(V);
c = mean(V(unique(k),:));
V=V-repmat(c,[size(V,1) 1]);
A  = NaN*zeros(size(k,1),size(V,2));
rc=0;
for ix = 1:size(k,1)
    F = V(k(ix,:),:);
    if rank(F,1e-5) == size(F,1)
        rc=rc+1;
        A(rc,:)=F\ones(size(F,1),1);
    end
end
A=A(1:rc,:);
b=ones(size(A,1),1);
b=b+A*c';
% eliminate dumplicate constraints:
[null,I]=unique(num2str([A b],6),'rows');
A=A(I,:); % rounding is NOT done for actual returned results
b=b(I);

figure('renderer','zbuffer')
hold on
plot(turbineX,turbineY,'r.')
[x,y]=ndgrid(0:10:9000);
p=[x(:) y(:)]';
p=(A*p <= repmat(b,[1 length(p)]));
p = double(all(p));
p=reshape(p,size(x));
h=pcolor(x,y,p);
set(h,'edgecolor','none')
set(h,'zdata',get(h,'zdata')-1) % keep in back
axis equal
set(gca,'color','none')
title('A*x <= b  (1=True, 0=False)')
colorbar

save('Amalia_locAndHull.mat', 'A', 'b', 'turbineX', 'turbineY')


