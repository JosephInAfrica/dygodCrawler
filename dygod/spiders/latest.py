# -*- coding: utf-8 -*-
import scrapy
from dygod.items import snapshotItem,filmItem,pageItem
from scrapy.loader import ItemLoader
from scrapy.http import Request
from scrapy_redis.spiders import RedisSpider


class LatestSpider(RedisSpider):
    name = 'latest'
    redis_key = 'latest:start_urls'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    # def start_requests(self):
    #     url = 'https://www.dy2018.com/html/gndy/dyzz/index.html'
    #     yield Request(url, headers=self.headers)


    def parse(self, response):

        links=response.xpath('//div//table//td/b/a')
        nexts=response.xpath('//div[@class="x"]/a/@href').extract()

        for nextpage in nexts:
            yield Request(url="https://www.dy2018.com"+nextpage,callback=self.parse)

        item=snapshotItem()
        for link in links:
            item['pageUrl']=link.css("a::attr('href')").extract_first().encode('utf8')
            yield Request(url="https://www.dy2018.com"+item['pageUrl'],callback=self.parseDetail)
            item['name']=link.xpath('text()').extract_first().encode('utf8')
            yield item



    def parseDetail(self,response):
        film=filmItem()
        film['name']=response.xpath('//div[@class="title_all"]//h1//text()').get()
        film['picUrl']=response.xpath('//div[@id="Zoom"]//p//img//@src').extract()
        film['downloadUrl']=response.xpath('//div[@id="Zoom"]//a//@href').extract()
        film['details']=response.xpath('//div[@id="Zoom"]//p//text()').extract()

        yield film




