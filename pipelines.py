# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DazhongPipeline(object):
    def process_item(self, item, spider):
        a = r"C:\python\d\add.txt"
        with open(a, 'a') as f:
            for i in range(len(item['kou'])):

                f.write(item['name'][i] + '\n')         #写入店名
                f.write(item['add'][i] + '\n')          #写入地址
                f.write('口味:' + item['kou'][i] + '\n')          #写入口味
                f.write('环境:' + item['huan'][i] + '\n')         #写入环境
                f.write('服务:' + item['fu'][i] + '\n')           #写入服务
                f.write('\n')

        return item
