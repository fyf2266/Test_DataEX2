import requests
from bs4 import BeautifulSoup


def getHtmlText(url, headers):
    try:
        response = requests.get(url, timeout=30, headers=headers)
        response.raise_for_status()  # 如果状态不是200，引发HttpError异常
        response.encoding = response.apparent_encoding
        return response.text
    except:
        return "产生异常"


if __name__ == "__main__":
    url = "https://www.zhihu.com"

    Chrome_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/83.0.4103.97 Safari/537.36 "
    }
    demo = getHtmlText(url, Chrome_headers)
    # print(demo)
    soup = BeautifulSoup(demo, 'html.parser')
    print(soup.prettify())
