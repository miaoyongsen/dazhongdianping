# -*- coding: utf-8 -*-
import scrapy
from dazhong.items import DazhongItem

class DianqingSpider(scrapy.Spider):
    name = 'dianping'
    allowed_domains = ['dianping.com']
    start_urls = ['http://www.dianping.com/beijing/ch10/g311']

    def parse(self, response):
        item = DazhongItem()
        zong = response.xpath('//*[@id="shop-all-list"]/ul/li')
        #获得地址
        a = []
        n = []
        k = []
        h = []
        f = []
        for i in zong:
            add = i.xpath('./div[4]/a[2]/@data-address|./div[3]/a[2]/@data-address').extract()          #获得地址
            a = a + add
            name = i.xpath('./div[2]/div[1]/a[1]/h4/text()').extract()                              #获得店名
            n = n + name

            kou = i.xpath('./div[2]/span/span[1]/b/span[1]/@class').extract()[0]                    #获取口味，第一位
            kou_s = self.pipei(kou)
            shu = i.xpath('./div[2]/span/span[1]/b/text()').extract()[0]                            #获得口味，小数点
            kouwei = kou_s + shu
            if shu != '.1' and shu != '':
                shi = i.xpath('./div[2]/span/span[1]/b/span[2]/@class').extract()[0]                #或的口味，第二位
                shi_s = self.pipei(shi)
                kouwei = kouwei + shi_s
            k.append(kouwei)

            huan = i.xpath('./div[2]/span/span[2]/b/span[1]/@class').extract()[0]                   #获得环境，第一位
            huan_s = self.pipei(huan)
            huan_shu = i.xpath('./div[2]/span/span[2]/b/text()').extract()[0]                       #获得环境，小数点
            huanjing = huan_s + huan_shu
            if huan_shu != '.1' and huan_shu != '':
                huan_shi = i.xpath('./div[2]/span/span[2]/b/span[2]/@class').extract()[0]           #获得环境，第二位
                huan_shis = self.pipei(huan_shi)
                huanjing = huanjing + huan_shis
            h.append(huanjing)

            fu = i.xpath('./div[2]/span/span[3]/b/span[1]/@class').extract()[0]                     #获得服务，第一位
            fu_s = self.pipei(fu)
            fu_shu = i.xpath('./div[2]/span/span[3]/b/text()').extract()[0]                         #获得服务，小数点
            fuwu = fu_s + fu_shu
            if fu_shu != '.1' and fu_shu != '':
                fu_shi = i.xpath('./div[2]/span/span[3]/b/span[2]/@class').extract()[0]             #获得服务，第二位
                fu_shis = self.pipei(fu_shi)
                fuwu = fuwu + fu_shis
            f.append(fuwu)

        item['add'] = a
        item['name'] = n
        item['kou'] = k
        item['huan'] = h
        item['fu'] = f
        return item

    def pipei(self,m):
        if m == 'hobx0x':
            return '9'
        elif m == 'hobbtz':
            return '8'
        elif m == 'hobsgz':
            return '7'
        elif m == 'hobo5a':
            return '6'
        elif m == 'hob3xn':
            return '5'
        elif m == 'hobzg8':
            return '4'
        elif m == 'hob5xj':
            return '3'
        elif m == 'hobxm0':
            return '2'
        elif m == 'hob5n5':
            return '0'
        else:
            return None