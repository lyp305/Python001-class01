学习笔记
1，
python连接mysql  ---pymysql 插件
执行顺序
开始-创建connection-获取cursor-CRUD(查询并获取数据)-关闭cursor-关闭connection-结束

pipeline组件中
from_crawler初始化时建立连接 开启游标
close_spider处理结束时 关闭游标和连接

2，

@classmethod  ： 装饰器方法 
返回的cls会被类的实例接受传给 _init_