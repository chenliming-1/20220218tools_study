import requests
import  json
def get_book():
    """获取书本信息"""
    url = "https://teacher-tr.test.klxuexi.net/tr/api/dict/baseDocs"
    res = requests.get(url)
    print(res.text,type(res))
    print(res.status_code)
    print(res.encoding)

if __name__ == "__main__":
    get_book()