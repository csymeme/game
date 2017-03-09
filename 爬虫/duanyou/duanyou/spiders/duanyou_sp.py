#_*_ coding: utf-8_*_
import re
import json
from scrapy.selector import Selector
try:
	from scrapy.spider import Spider
except:
	from scrapy.spider import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from scrapy.contrib.spiders import CrawlSpider, Rule
from duanyou.items import DuanyouItem
from scrapy.http import Request
from scrapy.contrib.linkextractors import LinkExtractor
class duanyou_sp(CrawlSpider):
	name="duanyousp"
	allowed_domins=["newgame.17173.com"]
	start_urls=[
		"http://newgame.17173.com/game-list-0-0-0-0-0-0-0-0-0-0-1-2.html"
	]
	rules=[
		Rule(LinkExtractor(allow=("game-list-0-0-0-0-0-0-0-0-0-0-1-2.html\?page\=([\d]+)",),), follow=True, callback='parse_item')
	]
	def parse_item(self,response):
		items=[]
		sel=Selector(response)
		base_url=get_base_url(response)
		sites_even=sel.xpath('//h2[@class="tit"]')
		for sit in sites_even:
			item=DuanyouItem()
			item['name']=sit.xpath('a/text()').extract()
			item['nurl']=sit.xpath('a/@href').extract()[0]
			items.append(item)
		return Request(item['nurl'],meta={'item':item},callback=self.parse2)

	def parse2(self,response):
		sel=Selector(response)
		item = response.meta['item']
		item['img']=sel.xpath('//div[@class="avatar-box"]/img/@src').extract()
		content=sel.xpath('//span[@class="con"]/a/text()').extract()
		item['platform']=content[0]
		item['frames']=content[1]
		item['style']=content[2]
		item['theme']=content[4]
		item['pattern']=content[5]
		item['form']=content[6]
		item['feature']=content[7:-1]
		item['pay']=sel.xpath('//span[@class="con"]/span')
		item['ranking']=sel.xpath('//div[@class="qdprank"]/a').extract()
		return item