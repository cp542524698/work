### 平衡二叉树（AVL树）

### 定义

  - 非叶子节点最多有两个子节点
  - 非叶子节点数据分布规则为左边的子节点小当前节点的值，右边的子节点大于当前节点的值(这里值是基于自己的算法规则而定的，比如hash值)； --- 中序遍历，则得到有序数列
  - 树的左右子树的层级相差不大于1；              ---- 平衡的约束
  - 没有值相等的节点；
  
### 平衡因子
  为了方便起见，给 出该节点左子树与右子树的高度差，称为节点的平衡因子（BF）

    平衡因子 = 节点左子树的高度 - 节点右子树的高度

  平衡二叉树的平衡因子只能是-1， 0， 1

###  平衡二叉树的插入
    当在平衡二叉树上插入一个节点时，有可能导致该树"失衡", 这时候就需要通过旋转来使之恢复平衡
![avatar](https://github.com/tianser/work/blob/master/001_dataStruct/pic/avl_insert.png)

  - 对于不平衡的处理流程：
    - 先计算出每个节点的平衡因子[绝对值]，如图：
![avatar](https://github.com/tianser/work/blob/master/001_dataStruct/pic/avl_handle_no_balance.png)    
    - 从新增节点出发到根节点所经过的节点中第一个不平衡的节点，则该节点为目标节点； 如图：
![avatar](https://github.com/tianser/work/blob/master/001_dataStruct/pic/avl_handle_no_balance.png)  
    - 处理目标节点为根的子树来达到平衡【通过旋转】
 
### 平衡二叉树的平衡调整（旋转）的四种类型：
  - 新增节点在根的左子树的左子树上（加在该节点的左边/右边）【LL旋转】
![avatar](https://github.com/tianser/work/blob/master/001_dataStruct/pic/avl_LL_rorate.png) 
  ==
![avatar](https://github.com/tianser/work/blob/master/001_dataStruct/pic/avl_rorate_LL_2.png) 
  - 新增节点在根的左子树的右子树上（加在该节点的左边/右边）【LR旋转】
![avatar](https://github.com/tianser/work/blob/master/001_dataStruct/pic/avl_rorate_RL.png)  
  

  - 新增节点在根的右子树的左子树上【RL旋转】
![avatar](https://github.com/tianser/work/blob/master/001_dataStruct/pic/avl_rorate_LR.png)

  - 新增节点在根的右子树的右子树【RR旋转】
![avatar](https://github.com/tianser/work/blob/master/001_dataStruct/pic/avl_rorate_RR.png) 
  ==
![avatar](https://github.com/tianser/work/blob/master/001_dataStruct/pic/avl_rorate_RR_2.png)  
  
