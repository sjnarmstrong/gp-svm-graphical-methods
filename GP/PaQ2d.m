[x11,x21] = meshgrid(linspace(-1.932,-0.45,20),...
    linspace(0.534,3.142,10));
[x12,x22] = meshgrid(linspace(0.45,1.932,20),...
    linspace(0.534,3.142,10));
Xstar = [reshape(x11,1,[]) reshape(x12,1,[]);reshape(x21,1,[]) reshape(x22,1,[])];
Xstar = Xstar';
ystar = 2*cos(10*Xstar(:,1)) + 1.3*cos(sum(Xstar,2));

[x1,x2] = meshgrid(linspace(-1.932,1.932,100),...
    linspace(0.534,3.142,100));

fx = 2*cos(10*x1) + 1.3*cos(x1+x2);

%Ntraining = 100;
Ntraining = 65;

X = [((1.932-0.45)*rand(Ntraining,1)+0.45).*(randi([0,1],Ntraining,1)*2-1) ...
    (3.142-0.534)*rand(Ntraining,1)+0.534];

y = 2*cos(10*X(:,1)) + 1.3*cos(sum(X,2));

%Xstar = [((1.932-0.45)*rand(400,1)+0.45).*(randi([0,1],400,1)*2-1) ...
%    (3.142-0.534)*rand(400,1)+0.534];

%ystar = 2*cos(10*Xstar(:,1)) + 1.3*cos(sum(Xstar,2));

%Xstar = [((1.932-0.45)*rand(400,1)+0.45).*(randi([0,1],400,1)*2-1) ...
%    (3.142-0.534)*rand(400,1)+0.534];

%ystar = 2*cos(10*Xstar(:,1)) + 1.3*cos(sum(Xstar,2));


figure
%surf(x1,x2,fx,'FaceColor','interp','EdgeColor','none'); hold on;
mesh(x1,x2,fx,'FaceLighting','gouraud','LineWidth',0.3); hold on;
%surf(x1,x2,fx); hold on;
h(1) = scatter3(X(1:end,1),X(1:end,2),y,10,...
    'MarkerEdgeColor',[1 0 0],...
    'MarkerFaceColor',[1 0 0]);

h(2) = scatter3(Xstar(1:end,1),Xstar(1:end,2),ystar,...
    'MarkerEdgeColor',[0 1 0],...
    'MarkerFaceColor',[0 1 0]);
legend(h,'Training Data','Test Data','Location','northeast')

title('Plot of f(x_1,x_2)')
xlabel('x_1')
ylabel('x_2')
zlabel('f(x_1,x_2)')

if 7~=exist('Output/PAQ2d','dir')
    mkdir('Output/PAQ2d')
end

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

print(gcf, '-dpdf', 'Output/PAQ2d/fxOrth.pdf');
title('Front View of $$f(\mathbf{x})$$', 'Interpreter', 'Latex', 'FontSize', 22)
xlabel('$$x_1$$', 'Interpreter', 'Latex', 'FontSize', 22)
ylabel('$$x_2$$', 'Interpreter', 'Latex', 'FontSize', 22)
zlabel('$$f(x)$$', 'Interpreter', 'Latex', 'FontSize', 22)
view(0, 0);
ti = ax.TightInset; 
left = outerpos(1) + ti(1);
bottom = outerpos(2) + ti(2);
ax_width = outerpos(3) - ti(1) - ti(3);
ax_height = outerpos(4) - ti(2) - ti(4);
ax.Position = [left bottom ax_width ax_height];
print(gcf, '-dpdf', 'Output/PAQ2d/fxSide.pdf');
print(gcf, '-dpdf', 'Output/PAQ2d/fxFront.pdf');
view(90, 0);

title('Side View of $$f(\mathbf{x})$$', 'Interpreter', 'Latex', 'FontSize', 22)
xlabel('$$x_1$$', 'Interpreter', 'Latex', 'FontSize', 22)
ylabel('$$x_2$$', 'Interpreter', 'Latex', 'FontSize', 22)
zlabel('$$f(x)$$', 'Interpreter', 'Latex', 'FontSize', 22)
print(gcf, '-dpdf', 'Output/PAQ2d/fxSide.pdf');
view(0, 90);

title('Top View of $$f(\mathbf{x})$$', 'Interpreter', 'Latex', 'FontSize', 22)
xlabel('$$x_1$$', 'Interpreter', 'Latex', 'FontSize', 22)
ylabel('$$x_2$$', 'Interpreter', 'Latex', 'FontSize', 22)
zlabel('$$f(x)$$', 'Interpreter', 'Latex', 'FontSize', 22)
print(gcf, '-dpdf', 'Output/PAQ2d/fxTop.pdf');



figure
h(1) = scatter3(X(1:end,1),X(1:end,2),y,10,...
    'MarkerEdgeColor',[1 0 0],...
    'MarkerFaceColor',[1 0 0]);hold on;
h(2) = scatter3(Xstar(1:end,1),Xstar(1:end,2),ystar,'+',...
    'MarkerEdgeColor',[0 1 0],...
    'MarkerFaceColor',[0 1 0]);
legend(h,'Training Data','Test Data','Location','northeast')

title('Plot of f(x_1,x_2)')
xlabel('x_1')
ylabel('x_2')
zlabel('f(x_1,x_2)')

if 7~=exist('Output/PAQ2d','dir')
    mkdir('Output/PAQ2d')
end

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

print(gcf, '-dpdf', 'Output/PAQ2d/fxNoMeshOrth.pdf');
title('Frount View of $$f(\mathbf{x})$$', 'Interpreter', 'Latex', 'FontSize', 22)
xlabel('$$x_1$$', 'Interpreter', 'Latex', 'FontSize', 22)
ylabel('$$x_2$$', 'Interpreter', 'Latex', 'FontSize', 22)
zlabel('$$f(x)$$', 'Interpreter', 'Latex', 'FontSize', 22)
view(0, 0);
ti = ax.TightInset; 
left = outerpos(1) + ti(1);
bottom = outerpos(2) + ti(2);
ax_width = outerpos(3) - ti(1) - ti(3);
ax_height = outerpos(4) - ti(2) - ti(4);
ax.Position = [left bottom ax_width ax_height];
print(gcf, '-dpdf', 'Output/PAQ2d/fxFrontNoMesh.pdf');
view(90, 0);

title('Side View of $$f(\mathbf{x})$$', 'Interpreter', 'Latex', 'FontSize', 22)
xlabel('$$x_1$$', 'Interpreter', 'Latex', 'FontSize', 22)
ylabel('$$x_2$$', 'Interpreter', 'Latex', 'FontSize', 22)
zlabel('$$f(x)$$', 'Interpreter', 'Latex', 'FontSize', 22)
print(gcf, '-dpdf', 'Output/PAQ2d/fxSideNoMesh.pdf');
view(0, 90);

title('Top View of $$f(\mathbf{x})$$', 'Interpreter', 'Latex', 'FontSize', 22)
xlabel('$$x_1$$', 'Interpreter', 'Latex', 'FontSize', 22)
ylabel('$$x_2$$', 'Interpreter', 'Latex', 'FontSize', 22)
zlabel('$$f(x)$$', 'Interpreter', 'Latex', 'FontSize', 22)
print(gcf, '-dpdf', 'Output/PAQ2d/fxTopNoMesh.pdf');



save('Output/PAQ2d/Data.mat','X','y','Xstar','ystar')