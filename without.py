from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

# 加载iris数据集
iris = load_iris()
data = iris.data
target = iris.target

# 将数据集分成训练集和测试集
x_train, x_test, y_train, y_test = train_test_split(data, target, test_size=0.3)

# 创建高斯朴素贝叶斯模型
model = GaussianNB()

# 训练模型
model.fit(x_train, y_train)

# 预测测试集
y_pred = model.predict(x_test)

# 计算准确率
accuracy = sum(y_pred == y_test) / len(y_test)
print("准确率为：%.2f" % accuracy)
