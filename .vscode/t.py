#!/usr/bin/env python
#-*- coding:utf-8 -*-

#用集合去除重复元素
import pprint

list_num = ['1', '2', '3', '4']
list_result = []
for i in list_num:
    for j in list_num:
        for k in list_num:
            if len(set(i + j + k)) == 3:
                list_result += [int(i + j + k)]
print("能组成%d个互不相同且无重复数字的三位数: " % len(list_result))
pprint.pprint(list_result)
