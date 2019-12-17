load('data1_assignment3.mat')

[x1,x2] = meshgrid(linspace(0.45,1.932,25),...
    linspace(0.534,3.142,25));
fx = 2*cos(x1) + 1.3*cos(x1+x2);

figure
surf(x1,x2,fx); hold on;
[x1,x2] = meshgrid(linspace(-1.932,-0.45,25),...
    linspace(0.534,3.142,25));
fx = 2*cos(x1) + 1.3*cos(x1+x2);
surf(x1,x2,fx);
h(1) = scatter3(X(1:end,1),X(1:end,2),y,10,...
    'MarkerEdgeColor',[1 0 0],...
    'MarkerFaceColor',[1 0 0]);

h(2) = scatter3(Xstar(1:end,1),Xstar(1:end,2),ystar,...
    'MarkerEdgeColor',[0 1 0],...
    'MarkerFaceColor',[0 1 0]);
legend(h,'Training Data','Test Data','Location','northeast')

title('3D Plot of $$f(\mathbf{x})$$', 'Interpreter', 'Latex')
xlabel('$$x_1$$', 'Interpreter', 'Latex')
ylabel('$$x_2$$', 'Interpreter', 'Latex')
zlabel('$$f(x)$$', 'Interpreter', 'Latex')

if 7~=exist('Output/PAQ2','dir')
    mkdir('Output/PAQ2')
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

print(gcf, '-dpdf', 'Output/PAQ2/fxOrth.pdf');



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
print(gcf, '-dpdf', 'Output/PAQ2/fxFront.pdf');
view(90, 0);

title('Side View of $$f(\mathbf{x})$$', 'Interpreter', 'Latex', 'FontSize', 22)
xlabel('$$x_1$$', 'Interpreter', 'Latex', 'FontSize', 22)
ylabel('$$x_2$$', 'Interpreter', 'Latex', 'FontSize', 22)
zlabel('$$f(x)$$', 'Interpreter', 'Latex', 'FontSize', 22)
print(gcf, '-dpdf', 'Output/PAQ2/fxSide.pdf');
view(0, 90);

title('Top View of $$f(\mathbf{x})$$', 'Interpreter', 'Latex', 'FontSize', 22)
xlabel('$$x_1$$', 'Interpreter', 'Latex', 'FontSize', 22)
ylabel('$$x_2$$', 'Interpreter', 'Latex', 'FontSize', 22)
zlabel('$$f(x)$$', 'Interpreter', 'Latex', 'FontSize', 22)
print(gcf, '-dpdf', 'Output/PAQ2/fxTop.pdf');


figure
h(1) = scatter3(X(1:end,1),X(1:end,2),y,10,...
    'MarkerEdgeColor',[1 0 0],...
    'MarkerFaceColor',[1 0 0]);hold on;
h(2) = scatter3(Xstar(1:end,1),Xstar(1:end,2),ystar,...
    'MarkerEdgeColor',[0 1 0],...
    'MarkerFaceColor',[0 1 0]);
legend(h,'Training Data','Test Data','Location','northeast')

title('Plot of $$f(\mathbf{x})$$', 'Interpreter', 'Latex')
xlabel('$$x_1$$', 'Interpreter', 'Latex')
ylabel('$$x_2$$', 'Interpreter', 'Latex')
zlabel('$$f(x)$$', 'Interpreter', 'Latex')

if 7~=exist('Output/PAQ2','dir')
    mkdir('Output/PAQ2')
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

print(gcf, '-dpdf', 'Output/PAQ2/fxNoMeshOrth.pdf');
view(0, 0);
ti = ax.TightInset; 
left = outerpos(1) + ti(1);
bottom = outerpos(2) + ti(2);
ax_width = outerpos(3) - ti(1) - ti(3);
ax_height = outerpos(4) - ti(2) - ti(4);
ax.Position = [left bottom ax_width ax_height];
print(gcf, '-dpdf', 'Output/PAQ2/fxNoMeshFront.pdf');
view(90, 0);
print(gcf, '-dpdf', 'Output/PAQ2/fxNoMeshSide.pdf');
view(0, 90);
print(gcf, '-dpdf', 'Output/PAQ2/fxNoMeshTop.pdf');