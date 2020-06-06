import requests


def getHtmlText(url, headers):
    try:
        response = requests.get(url, timeout=30, headers=headers)
        # 或者使用requests.request('get',url,timeout=30, headers=headers)
        response.raise_for_status()  # 如果状态不是200，引发HttpError异常
        response.encoding = response.apparent_encoding  # 如果header中不存在charset，则认为编码为ISO‐8859‐1
        return response.text
    except:
        return "产生异常"


if __name__ == "__main__":
    url = "https://www.zhihu.com"
    Chrome_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/83.0.4103.97 Safari/537.36 "
    }  # 因为知乎不允许requests直接访问，需要定制可以访问的headers的信息
    print(getHtmlText(url, Chrome_headers))
