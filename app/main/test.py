import requests
from lxml import html

url = 'http://www.mmjpg.com/home/2'


def alla():
    response = requests.get(url).content
    selector = html.fromstring(response)
    urls = []
    for i in selector.xpath("//ul/li/a/@href"):
        urls.append(i)
    print(urls[0])
    return urls


def aad():
    print(af())


def af():
    fileurl = alla()[0]
    header = {
        # 'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
        # 'Accept - Encoding': 'gzip, deflate',
        # 'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.5',
        # 'Connection': 'Keep-Alive',
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
        'Referer': fileurl}
    response = requests.get(fileurl, headers=header).content
    sel = html.fromstring(response)
    return sel.xpath("//div[@class='content']/a/img/@src")[0]


def download():
    fileurl = af()
    print(fileurl)
    header = {
        # 'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
        # 'Accept - Encoding': 'gzip, deflate',
        # 'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.5',
        # 'Connection': 'Keep-Alive',
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
        'Referer': fileurl}

    with open('a.jpg', 'wb') as f:
        f.write(requests.get(fileurl, headers=header, timeout=3).content)


if __name__ == '__main__':
    download()
