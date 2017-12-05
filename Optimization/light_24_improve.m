function main()
    x= 0:0.01:17.5;
    y= 0:0.01:12;
    m=length(y);
    n=length(x);
    [xx,yy]=meshgrid(x,y,'r');

    number = 24; % given 24 lights
    
    % initialize
    popsize=50;
    elite=0.2;
    maxiter=500;
    mutprob=0.2;

    pop=[];
    cost=[];
    for i=1:popsize
        sol=unifrnd(0,1,2,number);
        sol(1,:) = sol(1,:).*12;
        sol(2,:) = sol(2,:).*17.5;
        cost = [cost, costf(sol,xx,yy,m,n,number)];
        pop = [pop, sol];
    end

    topelite = floor(elite*popsize);

    % main iteration
    for i = 1:maxiter
        [ranked_cost,index_array] = sort(cost); 
        ranked = [];
        for r = 1:length(index_array)
            ranked = [ranked, pop(1:2, (number*(index_array(r)-1)+1):number*index_array(r))];
        end
        
        % REBUILD the pop
        pop = [];
        cost = [];
        % First: add elite generation
        pop = ranked(1:2, 1:topelite*number);
        for j = 1:topelite
            sol = pop(1:2, (number*(j-1)+1):number*j);
            cost = [cost, costf(sol,xx,yy,m,n,number)];
        end
        % Second: add descendant of the origin pop from mutate and crossover
        while (length(pop)/number)<popsize
            if rand<mutprob
                % mutate
                c = floor(rand*(topelite-1)+0.5)+1;
                sol = mutate(pop(1:2, (number*(c-1)+1):number*c), number);
                pop = [pop, sol];
                cost = [cost, costf(sol,xx,yy,m,n,number)];
            else
                % crossover
                c1 = floor(rand*(topelite-1)+0.5)+1;
                c2 = floor(rand*(topelite-1)+0.5)+1;
                r1 = pop(1:2, (number*(c1-1)+1):number*c1);
                r2 = pop(1:2, (number*(c2-1)+1):number*c2);
                sol = crossover(r1, r2, number);
                pop = [pop, sol];
                cost = [cost, costf(sol,xx,yy,m,n,number)];
            end
        end
        disp(ranked_cost(1));
    end
    
    % after main iteration
    result = ranked(1:2, 1:number);
    
    % Does the result meet the requirement?
    zz=0;
    for i=1:number
        zz = zz + 1./((yy-result(1,i)).^2+(xx-result(2,i)).^2+9);
    end
    AVG = sum(sum(zz))./(m*n);
    MAX = max(max(zz));
    if (MAX - AVG)./AVG > 1/3
        disp('not a good algo')
    else
        disp('a good algo')
    end
    
    % Plot the solution figure
    plot(result(1,:),result(2,:),'*r');
    axis([0 17.5 0 12]);
    figure;
    mesh(xx,yy,zz);
end
    
% calculate the cost
function cost=costf(sol,xx,yy,m,n,number)
    zz=0;
    for i=1:number
        zz = zz + 1./((yy-sol(1,i)).^2+(xx-sol(2,i)).^2+9);
    end
    AVG = sum(sum(zz))./(m*n);
    MAX = max(max(zz));
    cost = sum(sum((zz-AVG).^2));
end

% vec is a 2-d matrix, number is the length of the solution(number of lights)
function vec=mutate(vec,number)
    i = floor(rand*(number-1)+0.5)+1;
    flag = rand;
    if flag<0.25 & vec(1,i)>1 & vec(2,i)>1
        vec = [vec(1:2,1:i-1),[vec(1,i)-1,vec(2,i)-1]',vec(1:2,i+1:length(vec))];
    elseif flag<0.5 & vec(1,i)>1 & vec(2,i)<16.5
        vec = [vec(1:2,1:i-1),[vec(1,i)-1,vec(2,i)+1]',vec(1:2,i+1:length(vec))];
    elseif flag<0.75 & vec(1,i)<11 & vec(2,i)>1
        vec = [vec(1:2,1:i-1),[vec(1,i)+1,vec(2,i)-1]',vec(1:2,i+1:length(vec))];
    elseif vec(1,i)<11 & vec(2,i)<16.5
        vec = [vec(1:2,1:i-1),[vec(1,i)+1,vec(2,i)+1]',vec(1:2,i+1:length(vec))];
    else
    end
end

% r1 and r2 is 2-D matrix, just like parameter 'vec' in the mutate function
function vec=crossover(r1,r2,number)
    i = floor(rand*(number-1)+0.5)+1;
    vec = [r1(1:2,1:i), r2(1:2,i+1:length(r2))];
end