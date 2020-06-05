import pandas as pd

# 参数初始化
filename = '../data/data5/sales_data.xls'
data = pd.read_excel(filename, index_col='序号')

# 将数据标签化，‘好’，‘是’，‘高’表示1
data[data == '好'] = 1
data[data == '是'] = 1
data[data == '高'] = 1
data[data != 1] = 0
x = data.iloc[:, :3].astype(int)
y = data.iloc[:, 3].astype(int)

from keras.models import sequential
