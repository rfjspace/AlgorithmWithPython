# -*- coding:UTF-8 -*-
"""
冒泡排序法
"""


# 冒泡排序法
# arrays:待排序序列
# T(n)=c0+c1n+c2E(1..n)tj+..+C=Θ(n^2)
def bubblesSort(arrays):
    pValue = None  #-----------------------------------------------------c0
    for i in range(0, len(arrays)):  #-----------------------------------c1--n
        # 每次从后向前会将最小的元素排到前面，所以前面的有序序列，不需要迭代
        for j in range(len(arrays) - 1, i, -1):  #-----------------------c2--E(1..n)tj=n(n+1)/2
            if arrays[j] < arrays[j - 1]:  #-----------------------------c3--E(1..n)(tj-1)
                pValue = arrays[j - 1]  #--------------------------------c4--E(1..n)(tj-1)
                arrays[j - 1] = arrays[j]  #-----------------------------c5--E(1..n)(tj-1)
                arrays[j] = pValue  #------------------------------------c6--E(1..n)(tj-1)


if __name__ == '__main__':
    arrays = [5, 3, 2, 9, 6, 8, 7, 7, 20, 21, 20, 9]
    bubblesSort(arrays)
    print(arrays)
