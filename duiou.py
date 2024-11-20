"""
感知机学习算法的对偶形式：
输入：训练集T, 学习率
输出：a
感知机模型：f(x)=sign(∑N i=1 αi*yi*xi*x + ∑N i=1 αi*yi), ai = ni*η
算法步骤：
1.初始化a=0,n=0(其中a=(a1,a2,...,aN), η=(η1,η2,...,ηN))
2.在训练集中选取数据(xi,yi)
3.如果yi*(∑N i=1 αi*yi*xi*x + ∑N i=1 αi*yi)<=0(误分类点),则进行参数更新:
ai<-ai+η,即为更新ni*η<-ni*η+η,即ni<-ni+1
4.转至2，直至训练集中没有误分类点。

学习算法的直观解释：
当一个实例点被误分类，即位于分离超平面的错误一侧时，则调整w和b的值，使得分离超平面向该错误分类点
的一侧移动，以减少该错误分类点与超平面间的距离，直至超平面越过该误分类点使其被正确分类。

"""

import numpy as np
import matplotlib.pyplot as plt

# 训练集
x_true = np.array([[3, 3], [4, 3]])
x_false = np.array([[1, 1]])
x_all = np.vstack([x_true, x_false])
y = [1] * len(x_true) + [-1] * len(x_false)
n = len(x_all)

a = np.zeros(n)
b = 0  # 偏置
lr = 1  # 学习率

Gram = x_all.dot(x_all.T)  # 计算G


# 更新该样本点参数 检查是否有错误分类点
def check():
    global a, b  # 全局变量（便于修改全局变量a和b）
    i = 0
    # 循环判断每一个样本有没有误分类，有则更新参数重新开始判断
    # 默认无错误分类点
    flag = False
    # 检查所有样本点
    while i < n:
        error = 0
        for j in range(n):
            error += a[j] * y[j] * Gram[j, i]
        if y[i] * (error + b) <= 0:  # 有负样本
            # 错误分类
            flag = True
            # 更新该样本点参数
            a[i] += lr
            b += lr * y[i]
            print('a = {},b = {}'.format(a, b))
            i = 0
        else:
            i += 1
    return flag


if __name__ == "__main__":
    flag = False
    for i in range(100):
        # 无错误分类点，结束迭代
        if not check():  # check返回False，表示无错误分类点
            flag = True
            break
        # 有错误分类点，需继续迭代
    if flag:
        print("100次迭代，可以完成正确分类！")
    else:
        print("100次迭代，不可完成正确分类！")

w = np.zeros(2)
for j in range(n):
    w += a[j] * y[j] * x_all[j]

plot_x = [0, 1, 2, 3, 4, 5]
plot_y = [-(x * w[0] + b) / w[1] for x in plot_x]
plt.figure(figsize=(5, 5))
plt.scatter([x[0] for x in x_true], [x[1] for x in x_true], c='dodgerblue')
plt.scatter([x[0] for x in x_false], [x[1] for x in x_false], c='aquamarine')
plt.plot(plot_x, plot_y, c='dimgrey')
plt.xlim(0, 5.0)  # 坐标轴
plt.ylim(0, 5.0)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.pause(0.001)
plt.show()
