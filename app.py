#!/usr/bin/python
import urllib.request

# список с сайтами, откуда нужно украсть фавикон

target = ["google.com", "vk.com", "ya.ru", "youtube.com"]

# дергаем файл и сохраняем
for site in target:
    print (site)
    urllib.request.urlretrieve ("https://"+ site + "/favicon.ico", "/app/images/" + site +".ico")
    print("favicon from " + site + " has been stolen")
