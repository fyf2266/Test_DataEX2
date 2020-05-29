import pandas as pd
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn.tree import export_graphviz

filename = '../data/data5/sales_data.xls'
data = pd.read_excel(filename, index_col='序号')  # 将’序号‘列下的数据设置为index顺序

# 将数据‘好’，‘是’，‘高’标签为1，其他为-1
data[data == u'好'] = 1
data[data == u'是'] = 1
data[data == u'高'] = 1
data[data != 1] = -1
x = data.iloc[:, :3].astype(int)
y = data.iloc[:, 3].astype(int)

dtc = DTC(criterion='entropy')  # 建立决策树模型，基于信息熵
dtc.fit(x, y)  # 训练模型
print("准确度：%s" % dtc.score(x, y))

x = pd.DataFrame(x)
print(x.columns)
with open("../tmp/tree.dot", 'w') as f:
    export_graphviz(dtc, feature_names=x.columns, out_file=f)
