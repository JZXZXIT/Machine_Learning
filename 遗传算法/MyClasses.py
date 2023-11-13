import heapq
import random

__all__ = [
    '测试模块',
    '遗传'
]

test_地图 = [
    [0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0]
]

test_种群 = [
    [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 2, 2],
    [1, 2, 3, 2, 1, 3, 1, 2, 3, 3, 0, 3, 3, 3, 2, 1],
    [3, 3, 3, 3, 3, 3, 3, 3, 1, 3, 2, 3, 1, 1, 1, 0],
    [2, 2, 2, 1, 1, 1, 3, 0, 0, 0, 0, 2, 3, 3, 3, 3],
    [2, 0, 0, 3, 2, 1, 2, 0, 3, 3, 3, 2, 1, 0, 0, 3]
]

def 测试模块(路径, 地图=None):
    '''
    键入路径，计算距离终点的距离
    默认位于最下层的第一个位置
    :param 路径: 0,1,2,3  上下左右
    :return: 距离终点的距离
    '''
    ### 赋予默认值
    if 地图 is None:
        地图 = test_地图.copy()

    ### 获取初始信息
    x = 0
    y = len(地图) - 1
    Mx = len(地图[0]) - 1
    My = y
    距离 = Mx

    ### 根据路径判断位置
    for 方向 in 路径:
        if 方向 == 2 and x >= 1:
            x -= 1
        if 方向 == 3 and x <= (Mx-1):
            x += 1
        if 方向 == 0 and y >= 1:
            y -= 1
        if 方向 == 1 and y <= (My-1):
            y += 1

        ## 判断是否成功前进
        if 地图[y][x] == 1:
            break

        ## 若成功前进，则更新距离
        距离 = Mx - x

    return 距离


def 遗传(种群=None, 地图=None, 变异率=0.1):
    '''
    建立一个初始种群
    定义适应度函数（测试模块）
    挑选种群中的最佳个体
    交叉、变异创建新一代
    :param 种群:
    :param 地图:
    :param 变异率:
    :return:
    '''
    ### 赋予默认值
    if 地图 is None:
        地图 = test_地图.copy()
    if 种群 is None:
        种群 = test_种群.copy()

    ### 定义基本信息
    分割段数 = 3
    最佳个体数量 = 2
    子代数量 = None  # 种群个体数不变

    ### 获取基本信息
    个体个数 = len(种群)
    DNA长度 = len(种群[0])
    每段长度 = DNA长度 // 分割段数
    if 子代数量 is None:
        子代数量 = 个体个数

    ### 挑选种群中的最佳的两个个体
    结果 = []
    for 个体 in 种群:
        结果.append(测试模块(个体, 地图))
    最佳个体 = []
    最佳结果 = heapq.nsmallest(最佳个体数量, 结果)
    print(最佳结果[0])
    print(结果)
    for i in 最佳结果:
        索引 = 结果.index(i)
        最佳个体.append(种群[索引])
        if i == 0:
            return 种群[索引], True

    ### 交叉和变异
    子种群 = []
    ## 将最佳个体切片
    最佳个体切片 = []
    for 个体 in 最佳个体:
        个体切片 = []
        for i in range(分割段数):
            if i == 分割段数-1:
                个体切片.append(个体[每段长度 * i:])
            else:
                个体切片.append(个体[每段长度 * i:每段长度 * (i+1)])
        最佳个体切片.append(个体切片)
    ## 生成子代
    for _ in range(子代数量):
        个体 = []
        for i in range(分割段数):
            j = random.randint(0, 最佳个体数量-1)  # 可以改为轮盘赌
            for DNA in 最佳个体切片[j][i]:
                ## 变异
                if random.randint(1, 100) <= (变异率*100):
                    DNA = random.randint(0, 3)
                个体.append(DNA)
        子种群.append(个体)

    return 子种群, False