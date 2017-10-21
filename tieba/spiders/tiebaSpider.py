#-*- coding:utf-8-*-
import scrapy
from tieba.items import TiebaItem
import sys
reload(sys)
sys.setdefaultencoding("GB2312")

class TiebaSpider(scrapy.Spider):
    name = 'tieba'
    start_urls = [
        'http://c.tieba.baidu.com/p/5314244186'
        ]

    def parse(self, response):
        node_lists = response.xpath('//div[@class="l_post l_post_bright j_l_post clearfix  "]')
        items = []
        for node in node_lists:
            item = TiebaItem()
            item['name'] = node.xpath('div/ul/li[@class="d_name"]/a/text()').extract()
            item['comment'] = node.xpath('div/div[@class="p_content  "]/cc/div/text()').extract()
            #items.append(item)
            yield item#每执行一次传递给管道文件pipelines，同时还会返回继续执行后面的代码
        #return items
    
