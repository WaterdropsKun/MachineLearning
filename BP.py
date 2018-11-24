import numpy as np
from sklearn.datasets import load_digits
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt

# 载入数据
digits = load_digits()
print(digits.images.shape)
# 显示图片
plt.imshow(digits.images[0], cmap='gray')
plt.show()
plt.imshow(digits.images[1], cmap='gray')
plt.show()
plt.imshow(digits.images[2], cmap='gray')
plt.show()

# 数据
X = digits.data
# 标签
y = digits.target
print(X.shape)
print(y.shape)

# 数据切分
# 1/4为测试集，3/4为训练集
X_train, X_test, y_train, y_test = train_test_split(X, y)

# 标签二值化
labels_train = LabelBinarizer().fit_transform(y_train)

# 定义一个神经网络，结构：64-100-10
# 定义输入层到隐含层之间的权值矩阵
V = np.random.random((64, 100)) * 2 - 1
# 定义隐含层到输出层之间的权值矩阵
W = np.random.random((100, 10)) * 2 - 1

# 激活函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 激活函数导数
def dsigmoid(x):
    return x * (1 - x)

# 训练模型
def train(X, y, steps=10000, lr=0.11):
    global V, W
    for n in range(steps):
        # 随机选取一个数据
        i = np.random.randint(X.shape[0])
        # 获取一个数据
        x = X[i]
        x = np.atleast_2d(x)

        # BP算法公式
        # 计算隐含层的输出
        L1 = sigmoid(np.dot(x, V))
        # 计算输出层的输出
        L2 = sigmoid(np.dot(L1, W))
        # 计算L2_delta, L1_delta
        L2_delta = (y[i] - L2) * dsigmoid(L2)
        L1_delta = L2_delta.dot(W.T) * dsigmoid(L1)
        # 更新权值
        W += lr * L1.T.dot(L2_delta)
        V += lr * x.T.dot(L1_delta)

        # 每训练1000次预测一次准确率
        if n % 1000 == 0:
            output = predict(X_test)
            predictions = np.argmax(output, axis=1)   # axis=1行最大
            acc = np.mean(np.equal(predictions, y_test))
            print("step: ", n, "acc: ", acc)

def predict(x):
    L1 = sigmoid(np.dot(x, V))
    L2 = sigmoid(np.dot(L1, W))
    return L2

train(X_train, labels_train, 30000)

output = predict(X_test)
predictions = np.argmax(output, axis=1)
print(classification_report(predictions, y_test))
print(confusion_matrix(predictions, y_test))








