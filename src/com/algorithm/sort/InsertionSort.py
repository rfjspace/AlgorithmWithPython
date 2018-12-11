# -*- coding:UTF-8 -*-
"""
插入排序法
    算法的设计方法：增量法
        在排好序的数组A[1..j-1]后，将A[j]插入，形成排好序的数组A[j]
"""


def insertionSort(srcArrays, sc):
    if len(srcArrays) <= 0 :
        print("Length Of List Is Zero")
        return srcArrays
    if sc != 'A' and sc != 'D':
        print("Parameter Of Method Is Invalid")
        return srcArrays
    # range(p1,p2),生成p1-p2(p2除外)连续的整数的列表,相当于p1=p1+1
    for i in range(1, len(srcArrays)):  #--------------------------------------c1---n
        # 每次取得原列表的值放入到新列表中,最后的元素只占位，是无效的值，从0～i-1的元素为有效元素
        key = srcArrays[i]  #--------------------------------------------------c2---n-1
        j = i - 1  #-----------------------------------------------------------c3---n-1
        # 因为新列表为比较大小结果后插入，则为有序列表，不需要遍历所有元素
        while j >= 0 and srcArrays[j] > key:  #--------------------------------c4---E(1~n)tj
            # 交换元素位置
            srcArrays[j + 1] = srcArrays[j]  #---------------------------------c5---E(1~n)(tj-1)
            # 循环控制条件
            j = j - 1  #-------------------------------------------------------c6---E(1~n)(tj-1)
        # 找到插入位置后j仍会自减1,j+1才是需要插入的位置
        srcArrays[j + 1] = key  #----------------------------------------------c7---n-1
    return srcArrays
"""
插入排序法的算法分析:c1~cn为常数
T(n)=c1*n+c2*(n-1)+c3*(n-1)+c4*(E(1~n)tj)+c5*(E(1~n)(tj-1))+c6*(E(1~n)(tj-1))+c7*(n-1)
最佳效率 tj=1时，即完全有序
    =(c1+c2+c3+c4+c7)n-(c2+c3+c4+c7)
    =a*n+b
    =Θ(n)
最坏效率 (数列求和公式)E(1~n)A=n*(A1+An)/2,平均效率
    =a*n*n+b*n-c
    =Θ(n*n)
"""
#   # 列表(List)长度可动态增长,初期定义时长度为0
#   chdArrays = []
#   # range(p1,p2),生成p1-p2(p2除外)连续的整数的列表,相当于p1=p1+1
#   for i in range(0, len(srcArrays)):
#       # 虽然列表(List)长度可动态增长，但需要通过append()方法增长
#       chdArrays.append(srcArrays[i])
#       # 每次取得原列表的值放入到新列表中,最后的元素只占位，是无效的值，从0～i-1的元素为有效元素
#       # 循环完所有元素，确定插入位置之后交换位置，效率要比上面的代码低的多
#       # 确定插入的位置，默认插入在数组最后
#       iIndex = len(chdArrays) - 1
#       # range(p1,p2,p3)，生成p1-p2(p2除外)连续的整数的列表,相当于p1=p1+p3
#         for j in range(len(chdArrays) - 1, -1, -1): 
#             # 取得插入的最小位置
#             if sc == 'A' and chdArrays[j] > srcArrays[i]: 
#                 iIndex = j
#             if sc == 'D' and chdArrays[j] < srcArrays[i]: 
#                 iIndex = j
#         # 列表(List)是引用的地址，当改变地址中的值时列表跟着改变，函数参数的类型：值引用与地址引用              
#         swap(chdArrays, iIndex) 
#         # 向新列表中插入值
#         chdArrays[iIndex] = srcArrays[i]  
#   return chdArrays
# 从指定位置向后移动一位
# def swap(arrays, sIndex):
#     for k in range(len(arrays) - 1, sIndex, -1): 
#         arrays[k] = arrays[k - 1] 
#     return arrays
"""
算法的设计方法：分治法
"""


# 分治法
# srcArrays:待排序列，为引用传递
# sIndex:起始位置
# eIndex:结束位置
# 递归式：                                  递归树：
#             c = Θ(1)             n=1时                      [1,2,3,4]
#       T(n)=                                            [1,3,4]     [2]
#             T(n-1) + D(n) + C(n) n>1时             [1,4]     [3]
#           = Θ(n*n)                              [1]   [4]
def insertionSortByRecursive(srcArrays, sIndex, eIndex):
    # 分解 每次要分解的序列位置
    eI = eIndex - 1
    # 解决
    if eI > 0:
        insertionSortByRecursive(srcArrays, sIndex, eI)
    # 合并
    merge(srcArrays, sIndex, eIndex)

    
# 循环不等式    
def merge(arrays, sIndex, eIndex):
    aL = arrays[sIndex:eIndex]
    aR = arrays[eIndex]
    print(aL)
    print(aR)
    i = len(aL) - 1
    while i >= 0 and aL[i] > aR:
        arrays[i + 1] = arrays[i]
        i -= 1
    arrays[i + 1] = aR

    
if __name__ == '__main__':
    srcArrays = [18, 17, 19, 20, 3, 55, 44, 1, 1, 1]
#   chdArraysAsc = insertionSort(srcArrays, 'A')
#   print('ASC :', chdArraysAsc)
#     chdArraysDesc = insertionSort(srcArrays, 'D')
#     print('DESC:', chdArraysDesc)
#     arrays=swap(srcArrays,3)
#     print(arrays)      
    insertionSortByRecursive(srcArrays, 0, 9)
    print(srcArrays)
