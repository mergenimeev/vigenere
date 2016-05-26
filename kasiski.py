__author__ = "Mergen Imeev"
# coding: utf-8

import sys


def divisors(text):
    tmp_tuple = tuple(text[0 + i: 3 + i] for i in range(0, len(text) - 2))
    tmp_dict = dict()
    for i in range(len(tmp_tuple)):
        tmp_dict[tmp_tuple[i]] = tmp_dict.get(tmp_tuple[i], []) + [i]
    tmp_tuple = tuple(item for sub in tuple([chunk[i + 1] - chunk[i] for i in range(len(chunk) - 1)] \
                for chunk in tmp_dict.values() if len(chunk) > 2) for item in sub)
    tmp_dict = dict()
    for i in tmp_tuple:
        for j in tuple(div for div in range(2, i) if i % div == 0):
            tmp_dict[j] = tmp_dict.get(j, 0) + 1
    return tuple(x for x in tmp_dict.items() if x[1] > max(tmp_dict.values())/2)