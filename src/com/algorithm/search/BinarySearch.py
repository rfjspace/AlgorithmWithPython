# -*- coding:UTF-8 -*-
"""
算法的设计方法：分治法
    分解
    解决
    合并
"""
from getpass import _raw_input


# 二分查找法
# arrays:待查找的有序序列
# key:需要查找的对象
# sIndex:查找的开始位置
# eIndex:查找的结束位置
# 二叉树根节点为第一层
# 递归式:                                     递归树:(最坏情况)
#             c = Θ(1)    n=1时                         [1,3,4,6,7,10,20]
#       T(n)=                                         [1,3,4]    [6,7,10,20]
#             T(n/2) + D(n) + C(n)  n>1时                      [6,7]    [10,20]
#                                                                     [10]  [20]
# 设 递归树共有k层，则 n/2^(k-1)=1 即 k=lgn+1 *lgn为以2为底n的对数, 等比数列求和公式 S(n)=a1*(1-q^n)/(1-q) *q!=1
#       T(n)= (lgn+1)*(2*n+n/2+n/4+..+n/2^(k-1))
#           = c*n*lgn+c*n
#           = Θ(lgn)
def binarySearchByRecursive(arrays, key, sIndex, eIndex):
    # 被分解的序列
    print(sIndex, eIndex, arrays[sIndex:eIndex + 1])
    # 判断key值大概位置
    MIN = arrays[sIndex]
    MAX = arrays[eIndex]
    LEN = len(arrays[sIndex:eIndex + 1])
    if not (key <= MAX and key >= MIN):
        return False
    print(MIN, ' <= ' , key, ' <= ', MAX)
    # 将问题规模分解
    pIndex = int((sIndex + eIndex) / 2)
    if LEN > 1:
        if binarySearchByRecursive(arrays, key, sIndex, pIndex):
            return True
        elif binarySearchByRecursive(arrays, key, (pIndex + 1), eIndex):
            return True
        else :
            return False
    # 解决最小规模问题
    else:
        return search(arrays, key, pIndex)


# 最小规模问题，序列中只存在一个元素,即规模为1
def search(arrays, key, pIndex):
    if arrays[pIndex] == key:
        return True
    else :
        return False


# 二分查找法-迭代
#    通过迭代不断的寻找指定区间，直到锁定目标值
# arrays:待查找的有序序列
# key:需要查找的对象
# T(n)=a*lgn + C = Θ(lgn)
def binarySearchByIteration(arrays, key):
    LEN = len(arrays)
    # 初期化最大Index位置
    aIndex = LEN - 1
    # 初期化最小Index位置
    iIndex = 0
    # 保存上一层(二叉树)最大index
    pIndex = 0
    print(arrays)
    # 通过 i=2^n,对二叉树层数进行计算，用于控制迭代次数
    i = 1
    # 如果被查找序列长度为偶数，则在最后一层节点时，需多循环一次
    if LEN % 2 == 0:
        LEN = LEN + 1
    # 最小Index应小于最大Index，否则对不存在的元素，在计算区间时会造成序列index超界问题
    while int(LEN / i) != 0 and iIndex <= aIndex:  #------------------迭代次数为 k=lgn+1次
        # 重新定义区间临界
        MAX = arrays[aIndex]
        MIN = arrays[iIndex]
        print(MIN, '..' , MAX)
        if key <= MAX and key >= MIN:
            # 保存最大index，用于计算另一分支的最大index
            pIndex = aIndex
            # 计算当前最大index
            aIndex = int((aIndex + iIndex) / 2)
            # 设置当前最小index
            iIndex = iIndex
            # 存在可继续分解的区间时，即存在下一层树时
            i = i * 2
        else:
            # 计算当前最小index
            iIndex = aIndex + 1
            # 计算当前最大index
            aIndex = pIndex
    # 查找到最后一层时,判断是否存在于key相同的值，存在则为True，反之为False
    else:
        if iIndex == aIndex and key == arrays[iIndex]:
            return True
        else:
            return False

# 算法导论 2.3-7
# T(n)=Θ(nlgn)
# 第一层循环:for a in arrays ---------------------------------规模为n+c
# 计算差值:sub = x - a
# 第二层循环:使用二分查找法，查找sub是否存在于arrays中--------------规模为a*lgn+c
#         存在则存在两个数之和等于x的元素，不存在则不存在两个数之和等于x的元素

        
if __name__ == '__main__':
    key = 21
    arrays = [1, 2, 3, 4, 5, 6, 7, 10, 20, 30, 40]
#     while key != -1:
#         key = int(_raw_input())
#         sIndex = 0
#         eIndex = len(arrays) - 1
#         checkExist = binarySearchByRecursive(arrays, key, sIndex, eIndex)
#         print(checkExist)
    checkExist = binarySearchByIteration(arrays, key)
    print(checkExist)

