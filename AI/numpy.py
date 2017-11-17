#encoding=utf-8
import numpy as np

#改变数组的维度
1、ravel（）  #转为一维，多维数组本身不变
2、flatten（） #等价于ravel（），多维数组本身不变
3、Arr.shape = (2, 3) #使用reshape来设置维度，此时多维数组变量Arr的维度将改变
4、Arr.transpose()    #转秩，  在线性代数中， 转置矩阵是很常见的操作。对于多维数组，也可以
5、resize（） 和 reshape（）  #功能一样，但resize会直接修改所操作的数组


#多维数组的组合：
>>> a=np.arange(9).reshape(3, 3)
>>> b = 2 * a
>>> a
array([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]])
>>> b
array([[ 0,  2,  4],
       [ 6,  8, 10],
       [12, 14, 16]])
#水平组合
>>> np.hstack((a,b))
array([[ 0,  1,  2,  0,  2,  4],
       [ 3,  4,  5,  6,  8, 10],
       [ 6,  7,  8, 12, 14, 16]])
#hstack 等价于 concatenate函数
>>> np.concatenate((a,b), axis=1)  #axis 必须为1
array([[ 0,  1,  2,  0,  2,  4],
       [ 3,  4,  5,  6,  8, 10],
       [ 6,  7,  8, 12, 14, 16]])
#垂直组合
>>> np.vstack((a, b))
array([[ 0,  1,  2],
       [ 3,  4,  5],
       [ 6,  7,  8],
       [ 0,  2,  4],
       [ 6,  8, 10],
       [12, 14, 16]])
>>> np.concatenate((a,b), axis=0)
array([[ 0,  1,  2],
       [ 3,  4,  5],
       [ 6,  7,  8],
       [ 0,  2,  4],
       [ 6,  8, 10],
       [12, 14, 16]])
>>> np.row_stack((a,b))
array([[ 0,  1,  2],
       [ 3,  4,  5],
       [ 6,  7,  8],
       [ 0,  2,  4],
       [ 6,  8, 10],
       [12, 14, 16]])

分割函数：
hsplit, vsplit, dsplit, split
数组的属性：
  shape， dtype等
  ndim： 数组的维数
  size:  数组元素的总个数；
  itemsize： 数组中元素所占用内存；
  nbytes: 整个数组所占用的空间；
  T：     数组转秩
![image](https://github.com/cp542524698/work/blob/master/AI/np_ndarray.png)
  
