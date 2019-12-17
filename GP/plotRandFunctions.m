function plotRandFunctions( x, theta0, theta1, theta2, theta3, seeds )
    k = @(x0,x1,Theta0,Theta1,Theta2,Theta3) ...
        Theta0*exp(-(Theta1/2.0)*(x'-x).^2) ...
        + Theta2 + (Theta3*(x'*x));
    
    rng(seeds(1));
    y1 = mvnrnd(zeros(size(x)),k(x,x,theta0,theta1,theta2,theta3));
    rng(seeds(2));
    y2 = mvnrnd(zeros(size(x)),k(x,x,theta0,theta1,theta2,theta3));
    rng(seeds(3));
    y3 = mvnrnd(zeros(size(x)),k(x,x,theta0,theta1,theta2,theta3));
    rng(seeds(4));
    y4 = mvnrnd(zeros(size(x)),k(x,x,theta0,theta1,theta2,theta3));
    rng(seeds(5));
    y5 = mvnrnd(zeros(size(x)),k(x,x,theta0,theta1,theta2,theta3));


    figure('PaperPositionMode', 'auto');
    plot(x,y1,x,y2,x,y3,x,y4,x,y5,'LineWidth',3);
    title("Samples of y using $$\mathbf{\theta}=$$("+theta0+','+theta1+','+theta2+','+theta3+')', 'FontSize', 22,'Interpreter','latex');
    xlabel('x', 'FontSize', 20);
    ylabel('y', 'FontSize', 20);
    set(gca,'FontSize',20)
    
    if 7~=exist('Output/PAQ1','dir')
        mkdir('Output/PAQ1')
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
    
    print(gcf, '-dpdf', ['Output/PAQ1/rY' strrep(num2str(theta0),'.','p') '_' strrep(num2str(theta1),'.','p') '_' strrep(num2str(theta2),'.','p') '_' strrep(num2str(theta3),'.','p') '.pdf']);
end

