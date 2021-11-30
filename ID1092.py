#!/usr/bin/python3

url_list = []
try:
    while(1):
        url_list.append(input().split("/"))
except EOFError:
    pass

for url in url_list:
    if ("?" in url[-1]):
        url_detial_1 = url[-1].split("?")
    else:
        url_detial_1 = [url[-1], ""]
    if ("#" in url_detial_1[-1]):
        url_detial_2 = url_detial_1[-1].split("#")
    else:
        url_detial_2 = [url_detial_1[-1], ""]
    if (":" in url[2]):
        print("{" + "'hostname': '{}', 'port': '{}', 'protocol': '{}', 'query': '{}', 'fragment': '{}'".format((url[2].split(":"))[0], (url[2].split(":"))[1], url[0][:-1], url_detial_2[0], url_detial_2[1]) + "}")
    else:
        print("{" + "'hostname': '{}', 'protocol': '{}', 'query': '{}', 'fragment': '{}'".format(url[2], url[0][:-1], url_detial_2[0], url_detial_2[1]) + "}")
