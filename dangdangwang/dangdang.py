import requests
from lxml import html
def spider():
    """爬取当当网的数据"""
    url = "http://search.dangdang.com/?key=9787115428028&act=input"
    #获取html内容
    html_data = requests.get(url).text
    #xpath对象
    selector = html.fromstring(html_data)
    #找到书本列表
    ul_list=selector.xpath('//div[@id="search_nature_rg"]/ul/li')
    print(len(ul_list))
    for li in ul_list:
        #标题
        title=li.xpath('a/@title')
        print(title[0])
        #购买链接
        link = li.xpath('a/@href')
        print(link[0])
        #价格
        price=li.xpath('p[@class="price"]/span[@class="search_now_price"]/text()')
        print(price[0])
        print("--------------------------------")

    # ul_list = selector.xpath('//div[@id=”search_nature_rg“]/ul/li')


if __name__ =='__main__':
    spider()
