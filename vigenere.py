__author__ = "Mergen Imeev"
# coding: utf-8

import sys
import codecs


def kasisky(text):
    kas_tuple = tuple(text[0 + i: 3 + i] for i in range(0, len(text) - 2))
    kas_dict = dict()
    kas_dict = {kas_tuple[i]: kas_dict.get(kas_tuple[i], []) + [i] for i in range(len(kas_tuple))}
    kas_tuple = tuple(item for sub in tuple([chunk[i + 1] - chunk[i] for i in range(len(chunk) - 1)] for chunk in kas_dict.values() if len(chunk) > 2) for item in sub)
    kas_dict = dict()
    kas_dict = {j: kas_dict.get(j, 0) + 1 for i in kas_tuple for j in tuple(div for div in range(2, i) if i % div == 0)}
    return tuple(x for x in kas_dict.items() if x[1] > max(kas_dict.values())/2)


def get_letters(text, key_len):
    letters = [dict.fromkeys(tuple('абвгдежзийклмнопрстуфхцчшщъыьэюя'.upper()), 0) for i in range(key_len)]
    for i in range(len(text)):
        letters[i % key_len][text[i]] += 1
    return tuple(tuple(y[1] for y in sorted(x.items())) for x in letters)


def vigenere(filename):
    fd = open(filename, encoding='utf-8')
    text = fd.read()
    fd.close()
    kas = kasisky(text)
    letters = get_letters(text, 6)
    #---------------------------------------------
    print(letters)
    double_index = tuple(max((sum(letters[j][x] * letters[k][(x + i) % 32] for x in range(32)) / sum(letters[j])/sum(letters[k]), j, k, i) for i in range(32)) for k in range(0, 6) for j in range(k))
    print(sorted(double_index, reverse = True))
    #---------------------------------------------
    key_word = (17, 14, 11, 13, 22, 5)
    aaa = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'.upper()
    print(''.join(tuple(aaa[(aaa.find(text[i]) + 32 - key_word[i % 6]) % 32] for i in range(len(text)))))


def main():
#    if len(sys.argv) != 2:
#        print('usage: python vigenere.py file')
#        sys.exit(1)
#    vigenere(sys.argv[1])
    vigenere('vigenere.txt')
    sys.exit(1)

if __name__ == '__main__':
    main()
