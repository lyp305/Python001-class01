学习笔记

1，user-agent 模仿浏览器访问

2，BeautifulSoup find_all limit参数可以控制解析条数 实现抓取前10

3，Xpath 路径匹配

/ = 匹配指定路径  --鼠标点选 copy xpath

//  =  从上到下依次寻找

**//div[@class="hd"]**   

DIV有class属性 && 属性= hd

.  = 当前匹配位置向下找

..   = 当前匹配位置下一级向下找

4，Pipeline需要在settings.py中指定

5，xpath中 /text()和//text() ----//text() 获取标签中所有文本