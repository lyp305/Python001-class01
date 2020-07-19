学习笔记
pandas 默认第一行是表头
无表头：取第一列 用一列做表头名字

df[0:3]  ==　0行开始 显示3行

df[0:]  全部

df3.dropna()  删除有空值的行

df3.dropna(axis=1)  删除有空值的列

df2.drop_duplicates()   去重 留重复的第一列

df2.drop_duplicates(keep='last')  去重 留重复的最后一列   keep = false 全部删除

df.iloc[0:3, [0,3]]          0到3行  0和3列