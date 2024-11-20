import pandas as pd


def datapre():
    dataSet = [
        [1, 's', -1],
        [1, 'm', -1],
        [1, 'm', 1],
        [1, 's', 1],
        [1, 's', -1],
        [2, 's', -1],
        [2, 'm', -1],
        [2, 'm', 1],
        [2, 'l', 1],
        [2, 'l', 1],
        [3, 'l', 1],
        [3, 'm', 1],
        [3, 'm', 1],
        [3, 'l', 1],
        [3, 'l', -1]
    ]
    return pd.DataFrame(dataSet, columns=['x1', 'x2', 'label'])


def bayes(test):
    data = datapre()
    x11 = []
    x22 = []
    for i in range(len(data)):
        if data.loc[i, 'label'] == 1:
            x11.append(data.loc[i])
        else:
            x22.append(data.loc[i])
    lapulasi(data, x11, x22, test)


def lapulasi(data, x11, x22, test):  # 拉普拉斯
    p1 = 1.0
    p2 = 1.0
    for j in range(len(test)):
        x = 0.0
        for k in range(len(x11)):
            if x11[k][j] == test[j]:
                x = x + 1.0
        p1 = p1 * ((x + 1.0) / (len(x11) + 2.0))

    for j in range(len(test)):
        x = 0.0
        for k in range(len(x22)):
            if x22[k][j] == test[j]:
                x = x + 1.0
        p2 = p2 * ((x + 1.0) / (len(x22) + 2.0))

    pc1 = len(x11) / len(data)
    pc2 = 1 - pc1
    p_good = p1 * pc1
    p_bad = p2 * pc2

    if p_good > p_bad:
        print('1')
    else:
        print('-1')


if __name__ == '__main__':
    testdata = [1, 's']
    bayes(testdata)
