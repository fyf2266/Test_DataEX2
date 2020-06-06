import requests
from bs4 import BeautifulSoup


def GetHtmlText(url, headers):
    try:
        response = requests.get(url, timeout=30, headers=headers)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        return response.text
    except:
        return "产生异常"


if __name__ == '__main__':
    url = "https://python123.io/ws/demo.html"

    Chrome_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/83.0.4103.97 Safari/537.36 "
    }

    data = GetHtmlText(url, Chrome_headers)
    soup = BeautifulSoup(data, 'html.parser')   # 'html.parser'为bs4中的HTML解析器
    print(soup.prettify())  # 将网上的页面规范式输出
    print(soup.title)
    print(soup.a)
    print(soup.a.name)
    print(soup.a.parent.name)
    print(soup.a.attrs)
    print(soup.a.attrs['href'])
    print(soup.a.string)
