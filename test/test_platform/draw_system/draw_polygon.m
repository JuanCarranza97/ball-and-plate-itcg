function [points]=draw_polygon(radius,number,height)
    x=[];
    y=[];
    z=[];
    loop = 1;
    for angle=0:(360/number):360
        x(loop)=radius*cosd(angle);
        y(loop)=radius*sind(angle);
        z(loop)=height;
        loop=loop+1;
    end
    points=[x;y;z];
    plot3(x,y,z);
    grid on;
end
