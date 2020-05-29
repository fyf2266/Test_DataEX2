import pandas as pd
from sklearn.linear_model import LogisticRegression as LR

filename = '../data/data5/bankloan.xls'
data = pd.read_excel(filename)
x = data.iloc[:,:8].values  # 从头读取数据到第八行（不包括第八行）
y = data.iloc[:,8].values   # 从第八行开始读取
lr = LR()           # 建立逻辑回归模型
lr.fit(x,y)         # 用筛选后的特征数据来训练模型
print('模型的平均准确度为：%s' % lr.score(x,y))