from 请求 import *
url=询问("需要爬取的网页")
code=请求网页("get",url)
弹出(code.text)
