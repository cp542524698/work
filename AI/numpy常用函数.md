文件读写
eg：将一个单位矩阵存储到文件中：
>>> i3 = np.eye(3)
>>> i3
array([[ 1.,  0.,  0.],
       [ 0.,  1.,  0.],
       [ 0.,  0.,  1.]])
>>> np.savetxt("eye.txt", i3)

CSV文件：
  CSV（Comma-Separated Value， 逗号分隔值）格式，Excel可以处理CSV文件; numpy中使用loadtxt来载入csv文件
  c, v = np.loadtxt('data.csv', delimiter=',', usecols=(6,7), unpack=True)
  '''
    delimiter: 分隔符类型
    usecols：  元组，获取第7、8段的数据；
    unpack：  True，分拆存储不同列的数据
  '''
  np.max(c), np.min(v) 最值计算
  np.ptp(c)            #极值计算，即最大值与最小值之差
  np.median(c)         #中间值
  np.msort(c)          #排序
  np.var(c)            #方差；方差能够体现变量变化的程度。在我们的例子中，方差还可以告诉我们投资风险的大小。
  
  
