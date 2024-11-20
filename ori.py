import numpy as np
import matplotlib.pyplot as plt

x_true = np.array([[3,3],[4,3]])
x_false = np.array([[1,1]])
y = [1]* len(x_true) + [-1] * len(x_false)
x_all = np.vstack([x_true,x_false])

w = np.array([0,0])
lr = 1
b = 0
i = 0
# 循环判断每一个样本有没有误分类，有则更新参数重新开始判断
while i<len(x_all):
    if y[i]*(w.dot(x_all[i].T)+b) <= 0:
        w = w + lr * y[i] * x_all[i]
        b = b + lr * y[i]
        i = 0
        print('w = {},b = {}'.format(w,b))
    else:
        i += 1
print('平面S为：{:.2f}x1 + {:.2f}x2 {} = 0'.format(w[0],w[1], str(b) if b < 0 else '+'+str(b)))
plot_x = [0,1,2,3,4,5]
plot_y = [-(x*w[0]+b)/w[1] for x in plot_x]
plt.figure(figsize =(10,10))
plt.scatter([x[0] for x in x_true], [x[1] for x in x_true] , c = 'blue')
plt.scatter([x[0] for x in x_false], [x[1] for x in x_false] , c = 'red')
plt.plot(plot_x , plot_y , c = 'black')
# plt.text(0.5,4.5,'Func:{:.2f}x1 + {:.2f}x2 {} = 0'.format(w[0],w[1], str(b) if b < 0 else '+'+str(b)),fontsize=15,
# color = "green",style = "italic")
plt.xlim(0, 5.0)
# 坐标轴
plt.ylim(0, 5.0)
plt.xlabel('x1', fontsize = 16)
plt.ylabel('x2', fontsize = 16)
plt.pause(0.001)
plt.show()
