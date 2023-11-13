from MyClasses import *

迭代次数 = 0
种群, 循环 = None, False

while not 循环:
    种群, 循环 = 遗传(种群=种群, 变异率=0.1)
    迭代次数 += 1
    print(f"迭代次数：{迭代次数}")

print(种群)

# 路径 = [3, 0, 3, 3, 1, 3, 0, 3]
# i = 测试模块(路径)
# print(i)