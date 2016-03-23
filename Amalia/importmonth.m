function [directions, speeds] = importmonth(file)  
    
    [~, ~, raw0_0] = xlsread([file,'.xls'],file,'AN:AN');
    [~, ~, raw0_1] = xlsread([file,'.xls'],file,'AS:AS');
    raw = [raw0_0,raw0_1];
    raw(cellfun(@(x) ~isempty(x) && isnumeric(x) && isnan(x),raw)) = {''};

    %% Exclude rows with non-numeric cells
    J = ~all(cellfun(@(x) isnumeric(x) || islogical(x),raw),2); % Find rows with non-numeric cells
    raw(J,:) = [];

    %% Exclude rows with blank cells
    J = any(cellfun(@(x) isempty(x) || (ischar(x) && all(x==' ')),raw),2); % Find row with blank cells
    raw(J,:) = [];
    
    %% Exclude rows with -99999
    J = any(cellfun(@(x) (x==-99999),raw),2); % Find row with blank cells
    raw(J,:) = [];
    
    %% Create output variable
    data = reshape([raw{:}],size(raw));
    
    %% Exclude below-rated speeds
    
    %% Allocate imported array to column variable names
    directions = data(:,1);
    speeds     = data(:,2);
    

end