import numpy as np
from math import exp, sqrt, pi


def getDataSet():
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

    features = ['x1', 'x2']

    featureDic = {}
    for i in range(len(features)):
        featureList = [example[i] for example in dataSet]
        uniqueFeature = list(set(featureList))
        featureDic[features[i]] = uniqueFeature

    dataSet = np.array(dataSet)
    return dataSet, features, featureDic              # 返回数据集，特征词，特征元素


def countProLap(dataSet, index, value, classLabel, N):        # 拉普拉斯平滑
    extrData = dataSet[dataSet[:, -1] == classLabel]
    count = 0
    for data in extrData:
        if data[index] == value:
            count += 1
    return (count + 1) / (float(len(extrData)) + N)


def trainNB0(dataSet, features, featureDic):
    dict = {}                                          # 求类条件概率
    for feature in features:
        index = features.index(feature)
        dict[feature] = {}
        if feature != '密度' and feature != '含糖量':
            featIList = featureDic[feature]
            for value in featIList:
                PisCond = countProLap(dataSet, index, value, '1', len(featIList))
                pNoCond = countProLap(dataSet, index, value, '0', len(featIList))
                dict[feature][value] = {}
                dict[feature][value]["是"] = PisCond
                dict[feature][value]["否"] = pNoCond
        else:
            for label in ['1', '0']:
                dataExtra = dataSet[dataSet[:, -1] == label]
                extr = dataExtra[:, index].astype("float64")
                aver = extr.mean()
                var = extr.var()

                labelStr = ""
                if label == '1':
                    labelStr = '是'
                else:
                    labelStr = '否'

                dict[feature][labelStr] = {}
                dict[feature][labelStr]["平均值"] = aver
                dict[feature][labelStr]["方差"] = var

    length = len(dataSet)                                 # 求类先验概率
    classLabels = dataSet[:, -1].tolist()
    dict["好瓜"] = {}
    dict["好瓜"]['是'] = (classLabels.count('1') + 1) / (float(length) + 2)
    dict["好瓜"]['否'] = (classLabels.count('0') + 1) / (float(length) + 2)
    return dict


def NormDist(mean, var, xi):
    return exp(-((float(xi) - mean) ** 2) / (2 * var)) / (sqrt(2 * pi * var))


def classifyNB(data, features, bayesDis):
    pGood = bayesDis['好瓜']['是']
    pBad = bayesDis['好瓜']['否']
    for feature in features:
        index = features.index(feature)
        if feature != '密度' and feature != '含糖量':
            pGood *= bayesDis[feature][data[index]]['是']
            pBad *= bayesDis[feature][data[index]]['否']
        else:
            pGood *= NormDist(bayesDis[feature]['是']['平均值'], bayesDis[feature]['是']['方差'], data[index])
            pBad *= NormDist(bayesDis[feature]['否']['平均值'], bayesDis[feature]['否']['方差'], data[index])
    retClass = ""
    if pGood > pBad:
        retClass = "好瓜"
    else:
        retClass = "坏瓜"

    return pGood, pBad, retClass


def test_accuracy(dataSet, features, bayesDis):          # 精确率
    cnt = 0.0
    for data in dataSet:
        _, _, pre = classifyNB(data, features, bayesDis)
        if (pre == '好瓜' and data[-1] == '1') or (pre == '坏瓜' and data[-1] == '0'):
            cnt += 1
    return cnt / float(len(dataSet))


def main():
    dataSet, features, featureDic = getDataSet()
    dic = trainNB0(dataSet, features,featureDic)
    for each in dic.items():
        print(each)
    p1, p0, pre = classifyNB(dataSet[0], features, dic)
    print('\n',dataSet[0])
    print(f"p1 = {p1}")
    print(f"p0 = {p0}")
    print(f"pre = {pre}")
    print("train data set accuracy = ", test_accuracy(dataSet, features, dic))


if __name__ == '__main__':
    main()
