# !/usr/bin/python3.4
# -*-coding:utf-8-*-
# 新建文件夹
import os

if __name__ == "__main__":
    try:
        os.mkdir("../zimu")
    except:
        pass
    try:
        os.mkdir("../jpg/letter")
    except:
        pass
    try:
        os.mkdir("../jpg/good")
    except:
        pass

    iconset = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
               'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for i in iconset:
        try:
            os.mkdir("../zimu/" + i)
        except:
            pass
