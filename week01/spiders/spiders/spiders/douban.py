# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from spiders.items import SpidersItem


class DoubanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self, response):
        # 打印网页的url
        # print(response.url)
        # # 打印网页的内容
        # print(response.text)
        # print('=============================')

        movies = Selector(response=response).xpath('//div[@class="movie-item film-channel"]')
        index = 1
        for movie in movies:
            # print(movie)
            # print('============================================================')
            if index > 10:
                break

            mtitleList = movie.xpath('../div[1]/div[2]/a/div/div[1]/span[1]/text()').extract()
            mtitle = ''.join(mtitleList).strip()
            # print(mtitle)
            mtypeList = movie.xpath('../div[1]/div[2]/a/div/div[2]//text()').extract()
            mtype = ''.join(mtypeList).replace('\n','').replace(' ','')
            # print(mtype)
            mtimeList = movie.xpath('../div[1]/div[2]/a/div/div[4]//text()').extract()
            mtime = ''.join(mtimeList).replace('\n','').replace(' ','')
            # print(mtime)

            item = SpidersItem()
            item['mtitle'] =mtitle
            item['mtype'] =mtype
            item['mdate'] =mtime

            index = index +1
            yield item