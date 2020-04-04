import requests
import re
import os
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36'
}   #伪装身份
response = requests.get('https://www.vmgirls.com/13679.html' , headers=headers)
###print(response.request.headers)
html = response.text

dir_name = re.findall('<h1 class="post-title h3">(.*?)</h1>', html)[-1]   #自动创建文件夹并且读取网页里的名字作为文件名
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

urls = re.findall('<a href="(.*?)" alt=".*?" title=".*?">', html)   #正则表达式
print(urls)

for url in urls:   #下载图片
    file_name = url.split('/')[-1]
    response = requests.get(url, headers=headers)
    with open(dir_name + '/' + file_name,'wb') as f:
        f.write(response.content)


