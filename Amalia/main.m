%Main function

clear;clc;close all;

[speedbins,directionbins,binsizes] = annualdirections();


%% Analysis

%Grab 8 m/s wind rose
spIdx = find(speedbins==8,1);
counts8 = binsizes(spIdx,:);
counts = sum(binsizes);

%% Make a plot
close all;
figure; plot(directionbins(1:end-1),counts8)
hold all
plot(directionbins(1:end-1),counts)
legend('Counts8','Counts All')

% pTime is percent time in a given bin
pTime = counts/sum(counts);

for p = 1:length(pTime)
  fprintf('%f',pTime(p))
  if p < length(pTime)
      fprintf(',')
  end
end

totalTimeinHours = 10 * sum(counts)/60