function [speedbins,directionbins,binsizes] = annualdirections()


files = dir('OWEZ_M_181_200*');

speedbins = [0,(4:16)];
directionbins = [2.5:5:357.5];
binsizes = zeros(length(speedbins),length(directionbins)-1);

for month = 1:length(files)
 month
 file = files(month).name;
 [directions,speeds] = importmonth((file(1:end-4)));
 for i = 1:length(directions)
    speed = speeds(i);
    speedbin = 0;
    bin = 0;
    if speed>speedbins(end)
        speedbin = length(speedbins);
    end
    while speedbin == 0
       bin = bin + 1;
       if speed>=speedbins(bin) && speed < speedbins(bin+1);
            speedbin =  bin;
       end
    end
    direction = directions(i);
    directionbin = 0;
    bin = 0;
    if direction>directionbins(end)
        directionbin = 1;
    end    
    while directionbin == 0
       bin = bin + 1;
       if direction>=directionbins(bin) && direction < directionbins(bin+1);
            directionbin =  bin;
       end       
    end
    binsizes(speedbin,directionbin) = binsizes(speedbin,directionbin) + 1;
 end
end




 