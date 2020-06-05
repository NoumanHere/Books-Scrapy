# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

class BookspiderSpider(scrapy.Spider):
    name = 'bookspider'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']


    def parse(self,response):
        books = response.xpath('//h3/a/@href').extract()
        for book in books:
            absolute_url = response.urljoin(book)
            yield Request(absolute_url,callback=self.parse_book)

        next_page = response.xpath("//li[@class = 'next']/a/@href").get()
        print(next_page)
        if next_page:
            yield Request(response.urljoin(next_page))

    def parse_book(self,response):
        title = response.xpath('//h1/text()').get()
        price = response.xpath('//p[1]/text()').get()
        description = response.xpath('//article[@ class ="product_page"]/p/text()').get()
        image_url = response.xpath('//img/@src').extract_first()
        image_url = image_url.replace('../../','http://books.toscrape.com/')
        yield {
            'title':title ,          
            'price':  price,
            'image_url':  image_url,
            'description': description
        }
    # def parse(self, response):
    #     All_data = response.xpath('//div/section/div[2]/ol/li')
    #     titles = All_data.xpath('.//article/h3/a/text()').get()
    #     prices = All_data.xpath('.//article/div[2]/p/text()').get()
    #     for val in All_data:
    #         yield{
    #         "Title":val.xpath('.//article/h3/a/text()').get(),
    #         "Price":val.xpath('.//article/div[2]/p/text()').get()
    #         }
    #     next_page = response.xpath("//li[@class = 'next']/a/@href").get()
    #     print(next_page)
    #     if next_page:
    #         yield Request(response.urljoin(next_page),callback = self.parse)
     