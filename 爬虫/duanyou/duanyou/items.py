# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DuanyouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    	name=scrapy.Field() 
    	nurl=scrapy.Field()
 	platform=scrapy.Field()    # 平台
 	frames=scrapy.Field()       #画面
 	style=scrapy.Field()          #画风
 	theme=scrapy.Field()         #题材
 	pattern=scrapy.Field()      #模式
  	form=scrapy.Field()          #类型
  	feature=scrapy.Field()   #特征
        pay=scrapy.Field()     #收费
  	ranking=scrapy.Field()    #游戏榜
  	img=scrapy.Field()
 	