import numpy as np
import operator


def KNN(data: np.ndarray, dataSet: np.ndarray, labels: list, k: int):
    '''
    此为KNN算法，使用欧氏距离公式计算两个点之间的距离
    :param data:待判断数组，一维
    :param dataSet:数据集，二维
    :param labels:数据集对应的标签
    :param k:邻居个数
    :return:待判断数组的标签
    '''
    ### 获取基本信息
    L = dataSet.shape[0]  # 获取数据集样本个数

    ### 计算待判断数据与数据集中数据的距离
    x = np.tile(data, (L, 1)) - dataSet  # 计算输入样本与每个数据集样本的差值
    x = x ** 2
    x = x.sum(axis=1)
    距离 = x ** 0.5  # 得到欧式距离
    距离索引 = 距离.argsort()  # 对距离进行排序，返回排序后的索引

    ### 为带判断数据打上对应标签
    得分 = {}  # 存储每个样本的类别及其投票数
    for i in range(k):  # 循环 k 次，即找出距离最近的 k 个样本
        label = labels[距离索引[i]]  # 获取距离第 i 近的样本的类别
        得分[label] = 得分.get(label, 0) + 1  # 对该类别的投票数加一
    得分排序 = sorted(得分.items(), key=operator.itemgetter(1), reverse=True)  # 对投票数进行排序
    return 得分排序[0][0]  # 返回投票数最多的类别作为最终分类结果