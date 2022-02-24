from lxml import html

def use_xPath_demo():
    """"将html文件中的内容，使用xpath进行提取"""
    #读取文件中的内容
    f = open("./index.html",'r',encoding="utf-8")
    s = f.read() #这里已经把html内容获取到了
    # print(s,type(s))
    selector = html.fromstring(s)
    # print(selector)
    #解析h1标题
    h1 = selector.xpath('/html/body/h1/text()')
    # print(h1)
    #解析ul里面的内容
    ul = selector.xpath('/html/body/ul/li')
    # for li in ul:
    #     print(li.xpath('text()')[0])
    #解析ul下的指定内容
    ul2 = selector.xpath('/html/body/ul/li[@class="important"]/text()')
    print(ul2[0])
    #获取a标签的内容
    a1=selector.xpath('//div/a[@href="www.baidu.com"]/text()')
    print(a1[0])
    #获取a标签的属性值
    a2=selector.xpath('//div/a[@href="www.baidu.com"]/@href')
    print(a2[0])
    #获取p标签的内容
    p = selector.xpath('//body/p[last()]/text()')

    print(p)
    f.close()

if __name__ =='__main__':
    use_xPath_demo()

