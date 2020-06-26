# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pandas

class SpidersPipeline:
    def process_item(self, item, spider):

        # print('=======================================================================')
        # print(item)
        # print('=======================================================================')
        list = [item['mtitle'],item['mtype'],item['mdate']]
        movie = pandas.DataFrame(data=list)
        movie.to_csv('./moviemaoyan.csv', mode='a',encoding='utf8', index=False, header=False)

        return item