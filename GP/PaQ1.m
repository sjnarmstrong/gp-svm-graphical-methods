close all
x = linspace(-1,1,1000);

seeds = randi([0 10000],1,5);
plotRandFunctions(x,1,4,0,0,seeds);
plotRandFunctions(x,1,0.25,0,0,seeds);
plotRandFunctions(x,9,4,0,0,seeds);
plotRandFunctions(x,1,4,10,0,seeds);
plotRandFunctions(x,1,64,0,0,seeds);
plotRandFunctions(x,1,4,0,5,seeds);

plotRandFunctions(x,0,0,1,0,seeds);
plotRandFunctions(x,0,0,10,0,seeds);
plotRandFunctions(x,0,0,100,0,seeds);

plotRandFunctions(x,0,0,0,1,seeds);
plotRandFunctions(x,0,0,0,10,seeds);
plotRandFunctions(x,0,0,0,100,seeds);

plotRandFunctions(x,1,0.1,0,0,seeds);
plotRandFunctions(x,1,1,0,0,seeds);
plotRandFunctions(x,1,10,0,0,seeds);


plotRandFunctions(x,10,10,0,0,seeds);
plotRandFunctions(x,100,10,0,0,seeds);