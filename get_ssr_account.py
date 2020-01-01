import requests
import re
url = "https://github.com/Alvin9999/new-pac/wiki/ss%E5%85%8D%E8%B4%B9%E8%B4%A6%E5%8F%B7"
# print(r.content)


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  # 如果状态不是200，引发HTTPError异常#
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "exception!!"


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


if __name__ == "__main__":
    get_html = getHTMLText(url)
    reg1 = re.compile("<p><strong>.*com</p>")
    servers = reg1.findall(get_html)
    reg2 = re.compile("<p>.*?加.*")
    portocals = reg2.findall(get_html)
    for ind, server in enumerate(servers):
        print(cleanhtml(server))
        print(cleanhtml(portocals[ind]))
