%% 程序初始化
clc
clear
load('\data.mat')
change = zeros([300 1440*7]);%记录换电情况
Co = normrnd(82,2,[1 100000]);%电池容量分布（均值，标准差，矩阵大小）
Ct = min(Co.*normrnd(0.8,0.1,[1 100000]),Co);%电池电量初始分布
car = zeros([5 100000]);%汽车状态矩阵初始化
now_trans = trans(:,:,1);%初始化转移车辆的概率
now_times = times(:,:,1);%初始化转移需要的时间(单位是秒）
now_distance = distance(:,:,1);%初始化转移需要的路程(单位是千米）

%% 每一辆车的数据的初始化
car(1,:) = Co;%第1行为电池容量
car(2,:) = Ct;%第2行为当前时刻电量
pre = 100000.*sum(now_trans,2)./sum(sum(now_trans));%记录了三百个中心点每个中心点初始时刻有多少车
kk = pre(1);
for i = 1:300
    k = floor(kk);
    k_1 = floor(kk-pre(i));
    for j = k_1+1:k
        car(3,j) = i;
    end
    if i < 300
    kk = kk+pre(i+1);
    end
end
car(3,100000) = 300;
%第3行为当前所在地，使用第一页的状态转移矩阵进行初始化
for i = 1:100000
    f = sum(now_trans(car(3,i),:));
    if f ~= 0%判断是否这个中心点没有车辆前往下一个目标
        car(4,i) = randsrc(1,1,[1:300;now_trans(car(3,i),:)./sum(now_trans(car(3,i),:))]);
        car(5,i) = car(5,i)+now_times(car(3,i),car(4,i))/60;%累计时间（即完成本次订单之后的时间）
    else
        car(5,i) = car(5,i)+1;%在原地停一分钟
    end
    car(2,i) = car(2,i) - now_distance(car(3,i),car(4,i))/1000*0.205;%计算之后剩余电量（电量可能为负）
end
%第4行为前往目的地，第5行为完成订单时的时间（未来式）

%% 开始循环进行每一次的订单分析，步长一分钟
t = 361;
while(t < 1440*7)
    %判断现在该使用哪一页并进行数据的迁移
    if (mod(t,120) == 0)&&(mod(t,1440) >= 360)
        selmod = ceil(t/1440);
        sel = t/120-selmod*3+1;
        now_trans = trans(:,:,sel);
        now_times = times(:,:,sel);
        now_distance = distance(:,:,sel);
    end
    disp(1)
    %判断上一个订单是否执行完毕，如果执行完毕就开始执行下一个订单（同时进行充电操作）
    if mod(t,1440) >= 360%六点之后才开始
        for i = 1:100000
            if t > car(5,i)%判断是否订单已经到达时效
                if car(2,i) < unifrnd(0.15,0.3)*car(1,i) %充电触发，0.15到0.3倍电池容量的均匀分布
                    change(car(4,i),t) = 1+change(car(4,i),t);%记录换电需求
                    car(2,i) = abs(unifrnd(0.9,1)*car(1,i));%进行充电操作，瞬时
                end
                car(3,i) = car(4,i);%到达目的地
                f = sum(now_trans(car(3,i),:));
                if f ~= 0%判断是否这个中心点没有车辆前往下一个目标
                    car(4,i) = randsrc(1,1,[1:300;now_trans(car(3,i),:)./sum(now_trans(car(3,i),:))]);
                    car(5,i) = car(5,i)+now_times(car(3,i),car(4,i))/60;%累计时间（即完成本次订单之后的时间）

                else
                    car(5,i) = car(5,i)+1;%在原地停一分钟
                end
                car(2,i) = car(2,i) - now_distance(car(3,i),car(4,i))/1000*0.205;%计算之后剩余电量
            end
        end
    end
    disp(t)
    %零点到六点仅仅执行有订单的车辆（实际上我们不需要进行任何操作）
    %每天五点五十九分进行电量重置和时间重置
    if mod(t,1440) == 359
        for i = 1:100000
            if car(2,i) < unifrnd(0.15,0.3)*car(1,i) %充电触发，0.15到0.3倍电池容量的均匀分布
                change(car(4,i),t) = 1;%记录换电需求
            end
        end
    Ct = min(Co.*normrnd(0.8,0.1,[1 100000]),Co);%电池电量初始分布
    car(2,:) = Ct;%第2行为当前时刻电量
    car(5,:) = (1440*floor(t/1440)+360)+zeros(1,100000);%时间重置为当天的早上六点
    end
    t = t+1;
end

%% 保存数据
save('all.mat')