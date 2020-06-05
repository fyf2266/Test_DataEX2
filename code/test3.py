import pandas as pd
import xlrd

'''
df = pd.read_excel("../data/catering_dish_profit.xls")
# data = df.head() #默认读取前五行数据
print("获取到所有数据：\n{0}".format(df))
df1 = pd.read_excel("../data/catering_dish_profit.xls",sheet_name='选课课程') #通过指定表单名来读取
# df1 = pd.read_excel("../data/catering_dish_profit.xls",sheet_name=1) #通过表单索引来读取
# df1 = pd.read_excel("../data/catering_dish_profit.xls",sheet_name=['选课课程',1]) #通过混合方法指定
# df1 = pd.read_excel("../data/catering_dish_profit.xls",sheet_name=[0,1]) #通过索引可以同时指定多个表单
print("\n{0}".format(df1))
'''

'''
data = xlrd.open_workbook('../data/catering_fish_congee.xls')#打开Excel表格
table1 = data.sheet_by_index(0)#通过索引获取相应Sheet数据
table2 = data.sheet_by_name('Sheet2')#通过名称获取Sheet数据
Trow1 = table1.nrows #获取table1的行数值
Trow2 = table2.ncols #获取table2的列数值
for i in range(Trow1):
    print(table1.row_values(i))
for i in range(Trow2):
    print(table2.col_values(i))
'''

df = pd.read_excel("../data/catering_dish_profit.xls")
data = df.iloc[0].values  # 读取第一行数据，不包含表头
# data = df.iloc[[1,2]].values # 读取第一行及第二行数据
# data = df.iloc[1,2] #读取第一行第二列的数据
# data = df.iloc[[1,2],['菜品名']]
# data = df.iloc[:,['盈利']]
print("读取指定行的数据：{0}".format(data))
print("输出行号列表", df.index.values)
print("输出列标题", df.columns.values)
print("输出值", df.sample(1).values)
print("输出值\n", df['盈利'].values)

'''
df = pd.read_excel("../data/catering_dish_profit.xls")
test_data = [] # 用于存放字典的列表
for i in df.index.values:
    row_data = df.ix[i,['菜品名','菜品ID','盈利']].to_dict()
    test_data.append(row_data)
print("最终数据：{0}".format(test_data))
'''
