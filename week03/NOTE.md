学习笔记
1,性能
CPU密集型--计算处理多--- 单进程性能=多线程性能
IO密集型--查询数据库、网路请求处理多-多线程有优势

2,管道的资源抢占问题，加锁--->队列

3,python GIL锁 ---每个进程只有一个GIL锁  遇到IO操作释放GIL让出CPU