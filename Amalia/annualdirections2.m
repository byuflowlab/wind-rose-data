function [speedCenters,directionCenters,binsizes,speedEdges,directionEdges] = annualdirections2()

    files = dir('OWEZ_M_181_200*');

    directions = cell(1,length(files));
    speeds = cell(1,length(files));

    for month = 1:length(files)
        month
        file = files(month).name;
        [directions{month},speeds{month}] = importmonth((file(1:end-4)));
    end

    directions = cell2mat(directions');
    speeds = cell2mat(speeds');

    speedEdges = 0:1.0:ceil(max(speeds));
    directions(directions>(360-2.5)) = directions(directions>(360-2.5)) - 360;

    directionEdges = (0:5:360) - 2.5;

    binsizes = hist2(speeds, directions, speedEdges, directionEdges);
    binsizes = binsizes';
    binsizes = binsizes(1:end-1,1:end-1);

    speedCenters = (speedEdges(1:end-1)+speedEdges(2:end))/2;
    directionCenters = (directionEdges(1:end-1)+directionEdges(2:end))/2;





 