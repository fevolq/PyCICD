#!-*- coding:utf-8 -*-
# python3.7
# CreateTime: 2023/7/4 19:15
# FileName: 脚本

def add(*args):
    result = 0
    for value in args:
        result += value
    print(f'add: {" + ".join([str(value) for value in args])} = {result}')
    return result


def multi(*args):
    result = 1
    for value in args:
        result *= value
    print(f'multi: {" x ".join([str(value) for value in args])} = {result}')
    return result


if __name__ == '__main__':
    add(1, 2, 3)
    multi(1, 2, 3)
