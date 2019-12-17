close all;

if 2~=exist('Output/PAQ2d/Data.mat','file')
    disp 'Datafile does not exist. Please ensure that PaQ2d.m is run before this file.'
    return
end

load('Output/PAQ2d/Data.mat')

minX = min(X);
rangeX = max(X) - minX;
normX = (X - minX)./rangeX;
normXstar = (Xstar - minX)./rangeX;

meanY = mean(y);
yShifted = y-meanY;

meanfunc = []; 
covfunc = {'covSum', {'covSEard','covNoise'}};
likfunc = @likGauss;

numIterations = 10;
ScoreList = [];
hypList = [];
initialParams = [];
for c = 1:numIterations
    hyp = struct('mean', [], 'cov', log(rand(1,4)), 'lik', log(10e-10));
    initialParams = [initialParams hyp];
    [hyp2, fX, iterations] = minimize(hyp, @gp, -2000, @infGaussLik, meanfunc, covfunc, likfunc, normX, yShifted);
    ScoreList = [ScoreList fX(end)];
    hypList = [hypList hyp2];
end

[bestScore, bestScoreIndex] = min(ScoreList);
besthyp = hypList(bestScoreIndex);

disp(['Expected variance: ' num2str(power(exp(besthyp.lik),2))])

[m, s2] = gp(besthyp, @infGaussLik, meanfunc, covfunc, likfunc, normX, yShifted, normXstar);

MSETest = sum(power(m+meanY-ystar,2))/length(ystar);
RMSETest  = sqrt(MSETest);
NRMSETest  = RMSETest/range(ystar);

[mTr, sTr2] = gp(besthyp, @infGaussLik, meanfunc, covfunc, likfunc, normX, yShifted, normX);

MSETraining = sum(power(mTr-yShifted,2))/length(ystar);
RMSETraining  = sqrt(MSETraining);
NRMSETraining  = RMSETraining/range(yShifted);


figure
[x1,x2] = meshgrid(linspace(-1.932,1.932,100),...
    linspace(0.534,3.142,25));

XtoPlot = (reshape([x1 x2], [numel(x1) 2]) - ...
    minX)./rangeX;

[mPl, sPl2] = gp(besthyp, @infGaussLik, meanfunc, covfunc, likfunc, normX, yShifted, XtoPlot);
fx = reshape(mPl+meanY, size(x1));
fx1 = reshape(mPl+meanY+2*sqrt(sPl2), size(x1));
fx2 = reshape(mPl+meanY-2*sqrt(sPl2), size(x1));

mesh(x1,x2,fx1,'FaceLighting','gouraud','LineWidth',0.3); hold on;
mesh(x1,x2,fx2,'FaceLighting','gouraud','LineWidth',0.3);

title("Plot of the predictive function's certainty", 'Interpreter', 'Latex')
xlabel('$$x_1$$', 'Interpreter', 'Latex')
ylabel('$$x_2$$', 'Interpreter', 'Latex')
zlabel('$$f(x)$$', 'Interpreter', 'Latex')
ax = gca;
outerpos = ax.OuterPosition;
ti = ax.TightInset; 
left = outerpos(1) + ti(1);
bottom = outerpos(2) + ti(2);
ax_width = outerpos(3) - ti(1) - ti(3);
ax_height = outerpos(4) - ti(2) - ti(4);
ax.Position = [left bottom ax_width ax_height];

fig = gcf;
fig.PaperPositionMode = 'auto';
fig_pos = fig.PaperPosition;
fig.PaperSize = [fig_pos(3) fig_pos(4)];

print(gcf, '-dpdf', 'Output/PAQ2d/pxVOrth.pdf');




title("Frount View of predictive function's certainty", 'Interpreter', 'Latex', 'FontSize', 19)
xlabel('$$x_1$$', 'Interpreter', 'Latex', 'FontSize', 19)
ylabel('$$x_2$$', 'Interpreter', 'Latex', 'FontSize', 19)
zlabel('$$f(x)$$', 'Interpreter', 'Latex', 'FontSize', 19)
view(0, 0);
ti = ax.TightInset; 
left = outerpos(1) + ti(1);
bottom = outerpos(2) + ti(2);
ax_width = outerpos(3) - ti(1) - ti(3);
ax_height = outerpos(4) - ti(2) - ti(4);
ax.Position = [left bottom ax_width ax_height];
print(gcf, '-dpdf', 'Output/PAQ2d/pxVOrthFront.pdf');
view(90, 0);

title("Side View of predictive function's certainty", 'Interpreter', 'Latex', 'FontSize', 19)
xlabel('$$x_1$$', 'Interpreter', 'Latex', 'FontSize', 19)
ylabel('$$x_2$$', 'Interpreter', 'Latex', 'FontSize', 19)
zlabel('$$f(x)$$', 'Interpreter', 'Latex', 'FontSize', 19)
print(gcf, '-dpdf', 'Output/PAQ2d/pxVOrthSide.pdf');
view(0, 90);

title("Top View  of predictive function's certainty", 'Interpreter', 'Latex', 'FontSize', 19)
xlabel('$$x_1$$', 'Interpreter', 'Latex', 'FontSize', 19)
ylabel('$$x_2$$', 'Interpreter', 'Latex', 'FontSize', 19)
zlabel('$$f(x)$$', 'Interpreter', 'Latex', 'FontSize', 19)
print(gcf, '-dpdf', 'Output/PAQ2d/pxVOrthTop.pdf');



fxReal = 2*cos(10*x1) + 1.3*cos(x1+x2);

figure
%surf(x1,x2,fxReal); hold on;
surf(x1,x2,fx,'FaceLighting','gouraud','LineWidth',0.3);

title("Plot of the predictive function", 'Interpreter', 'Latex')
xlabel('$$x_1$$', 'Interpreter', 'Latex')
ylabel('$$x_2$$', 'Interpreter', 'Latex')
zlabel('$$f(x)$$', 'Interpreter', 'Latex')

ax = gca;
outerpos = ax.OuterPosition;
ti = ax.TightInset; 
left = outerpos(1) + ti(1);
bottom = outerpos(2) + ti(2);
ax_width = outerpos(3) - ti(1) - ti(3);
ax_height = outerpos(4) - ti(2) - ti(4);
ax.Position = [left bottom ax_width ax_height];

fig = gcf;
fig.PaperPositionMode = 'auto';
fig_pos = fig.PaperPosition;
fig.PaperSize = [fig_pos(3) fig_pos(4)];

print(gcf, '-dpdf', 'Output/PAQ2d/PxErrOrth.pdf');

figure
surf(x1,x2,abs(fxReal-fx)); hold on;

nonoiseY = 2*cos(10*X(1:end,1)) + 1.3*cos(X(1:end,1)+X(1:end,2));

h(1) = scatter3(X(1:end,1),X(1:end,2),abs(mTr+meanY-nonoiseY),10,...
    'MarkerEdgeColor',[1 0 0],...
    'MarkerFaceColor',[1 0 0]);


nonoiseYStar = 2*cos(10*Xstar(1:end,1)) + 1.3*cos(Xstar(1:end,1)+Xstar(1:end,2));

h(2) = scatter3(Xstar(1:end,1),Xstar(1:end,2),abs(m+meanY-nonoiseYStar),...
    'MarkerEdgeColor',[0 1 0],...
    'MarkerFaceColor',[0 1 0]);
legend(h,'Training Errors','Test Errors','Location','northeast')
%mesh(x1,x2,fx,'FaceLighting','gouraud','LineWidth',0.3);

title("Plot of absolute error", 'Interpreter', 'Latex')
xlabel('$$x_1$$', 'Interpreter', 'Latex')
ylabel('$$x_2$$', 'Interpreter', 'Latex')
zlabel('Error', 'Interpreter', 'Latex')

ax = gca;
outerpos = ax.OuterPosition;
ti = ax.TightInset; 
left = outerpos(1) + ti(1);
bottom = outerpos(2) + ti(2);
ax_width = outerpos(3) - ti(1) - ti(3);
ax_height = outerpos(4) - ti(2) - ti(4);
ax.Position = [left bottom ax_width ax_height];

fig = gcf;
fig.PaperPositionMode = 'auto';
fig_pos = fig.PaperPosition;
fig.PaperSize = [fig_pos(3) fig_pos(4)];

print(gcf, '-dpdf', 'Output/PAQ2d/PxAbsError.pdf');

figure
surf(x1,x2,abs(fxReal-fx));
%mesh(x1,x2,fx,'FaceLighting','gouraud','LineWidth',0.3);

title("Plot of absolute error", 'Interpreter', 'Latex')
xlabel('$$x_1$$', 'Interpreter', 'Latex')
ylabel('$$x_2$$', 'Interpreter', 'Latex')
zlabel('Error', 'Interpreter', 'Latex')

ax = gca;
outerpos = ax.OuterPosition;
ti = ax.TightInset; 
left = outerpos(1) + ti(1);
bottom = outerpos(2) + ti(2);
ax_width = outerpos(3) - ti(1) - ti(3);
ax_height = outerpos(4) - ti(2) - ti(4);
ax.Position = [left bottom ax_width ax_height];

fig = gcf;
fig.PaperPositionMode = 'auto';
fig_pos = fig.PaperPosition;
fig.PaperSize = [fig_pos(3) fig_pos(4)];

print(gcf, '-dpdf', 'Output/PAQ2d/PxAbsErrorNoPoints.pdf');



figure
[x1,x2] = meshgrid(linspace(0.45,1.932,100),...
    linspace(0.534,3.142,25));

XtoPlot = (reshape([x1 x2], [numel(x1) 2]) - ...
    minX)./rangeX;

[mPl, sPl2] = gp(besthyp, @infGaussLik, meanfunc, covfunc, likfunc, normX, yShifted, XtoPlot);
fx = reshape(mPl+meanY, size(x1));

fxReal = 2*cos(10*x1) + 1.3*cos(x1+x2);
surf(x1,x2,abs(fxReal-fx)); hold on;


[x1,x2] = meshgrid(linspace(-1.932,-0.45,100),...
    linspace(0.534,3.142,25));

XtoPlot = (reshape([x1 x2], [numel(x1) 2]) - ...
    minX)./rangeX;

[mPl, sPl2] = gp(besthyp, @infGaussLik, meanfunc, covfunc, likfunc, normX, yShifted, XtoPlot);
fx = reshape(mPl+meanY, size(x1));

fxReal = 2*cos(10*x1) + 1.3*cos(x1+x2);
surf(x1,x2,abs(fxReal-fx));
%mesh(x1,x2,fx,'FaceLighting','gouraud','LineWidth',0.3);

title("Plot of absolute error", 'Interpreter', 'Latex')
xlabel('$$x_1$$', 'Interpreter', 'Latex')
ylabel('$$x_2$$', 'Interpreter', 'Latex')
zlabel('Error', 'Interpreter', 'Latex')

ax = gca;
outerpos = ax.OuterPosition;
ti = ax.TightInset; 
left = outerpos(1) + ti(1);
bottom = outerpos(2) + ti(2);
ax_width = outerpos(3) - ti(1) - ti(3);
ax_height = outerpos(4) - ti(2) - ti(4);
ax.Position = [left bottom ax_width ax_height];

fig = gcf;
fig.PaperPositionMode = 'auto';
fig_pos = fig.PaperPosition;
fig.PaperSize = [fig_pos(3) fig_pos(4)];

print(gcf, '-dpdf', 'Output/PAQ2d/PxAbsErrorNoPointsNoCentre.pdf');


