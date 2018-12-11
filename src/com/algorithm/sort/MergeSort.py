# -*- coding:UTF-8 -*-
"""
合并排序法
    算法的设计方法：分治法(递归)
        将原问题划分为n个较小规模与原问题相似的子问题，递归的解决这些子问题，然后合并其结果，就得到原问题的解
    步骤：
        1.分解：将n个元素分成n/2个元素的子序列
        2.解决：用合并排序法对两个子序列递归地排序
       *3.合并：合并两个已排好序的子序列以得到排序结果
       
                   合并排序法
            [ 1, 2, 2, 3, 4, 5, 6, 7 ]
合并      [2,4,5,7]             [1,2,3,6]
合并    [2,5]   [4,7]         [1,3]   [2,6]
合并  [5] [2]  [4] [7]      [1] [3]  [2] [6]        
"""


# A:待排序序列
# p:排序的开始位置
# r:排序的结束位置
# q:n/2个元素的子序列index位置
# 划分为n个较小规模与原问题相似的子问题，递归的解决这些子问题
# lgn表示以2为底n的对数，根据递归树推理得T(n)的渐进确界为Θ(nlgn),且递归树的层数为lgn+1层，即递归深度
def mergeSort(A, p, r):  # T(n)=2T(n/2)+Θ(n)+Θ(1),当n=1时,T(n)=Θ(1),当n>1时,T(n)=2T(n/2)+Θ(n)=Θ(nlgn) *Θ(n)+Θ(1)为线性函数Θ(n)*
    if p < r:  
        # 除法a/b可以为小数，须根据具体需求定义其精度
        q = int((r + p) / 2)  #--------------------------------分解：仅计算出子数组的中间位置，需要常量时间 D(n)=Θ(1)
        # 递归的对分解的子序列进行排序
        mergeSort(A, p, q)  #----------------------------------解决：递归的解决两个规模为n/2的子问题，时间为2T(n/2)
        mergeSort(A, q + 1, r)
        # 合并分解的子序列
        merge(A, p, q, r)  #-----------------------------------合并：在含有n个子数组上合并过程的时间为Θ(n)，C(n)=Θ(n)
    

# *对序列下标的计算
# 合并分解的子序列,递归到最后只剩一个元素与一个元素比较大小
def merge(A, p, q, r):  # 最优效率 ：T(n)=a*n+b,Θ(n)=n ;最坏效率T(n)=a*n*n+b*n+c,Θ(n)=n*n
    # 创建定长空序列
    LL = (q - p + 1)  #---------------------------------------c1
    LR = (r - q)  #-------------------------------------------c2
    AL = [None] * LL  #---------------------------------------c3
    AR = [None] * LR  #---------------------------------------c4
    # 用来判断子序列是否读取完了
    # inf 表示为正无穷大，-inf为负无穷大,infinite,转化为浮点型表示,java中存在常数表示该值
    MAX = float("inf")  #-------------------------------------c5
    # print(MAX) -- inf
    # 分解序列
    for i in range(0, LL):  #---------------------------------c6--E(0..n/2)tl
        # index = p + q - p + 1 + 1 - 1 = q
        AL[i] = A[p + i]  #-----------------------------------c7--E(0..n/2)(tl-1)
    AL.append(MAX)  #-----------------------------------------c8
    for i in range(0, LR):  #---------------------------------c9--E(0..n/2)tr
        # index = q + 1 + r - q + 1 - 1 = r
        AR[i] = A[(q + 1) + i]  #-----------------------------c10--E(0..n/2)(tr-1)
    AR.append(MAX)  #-----------------------------------------c11

    # 子序列索引值
    j = 0  #--------------------------------------------------c12
    k = 0  #--------------------------------------------------c13
    # 循环序列
    for f in range(p, r + 1):  #------------------------------c14--E(0..n)tf
        # 判断两个子序列中元素大小，进行排序
        if AL[j] <= AR[k]:  #---------------------------------c15--E(0..n-1)(tf-1)
            A[f] = AL[j]
            j += 1
        else:
            A[f] = AR[k]
            k += 1
"""
分治法分析：
  设T(n)为规模为n的问题运行时间，如何n的规模足够小，则问题的直接解的时间为常量，为Θ(1)
  假设我们将原问题分解为a个子问题，每一个的大小是原问题1/b，分解该问题的时间为D(n),合并问题的时间为C(n)
  则，得到递归式(递归的数学表示)
          Θ(1) 如何n<c(规模足够小)
  T(n)=   
          a*T(n/b)+D(n)+C(n) (规模足够大)
"""
            
if __name__ == '__main__':
    # A={2,1} or A=(2,1)为元组，TypeError: 'set' object does not support indexing
    A = [2, 1, 3, 8, 6, 22, 2, 10, 4, 7, 21, 55, 44]
    mergeSort(A, 0, len(A) - 1)
    print(A)