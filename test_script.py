#!-*- coding:utf-8 -*-
# python3.7
# CreateTime: 2023/7/6 11:42
# FileName:

import random
import unittest
from functools import reduce

import script


def gen_args():
    number = random.randint(5, 9)
    return random.choices(list(range(0, 10)), k=number)


class TestScript(unittest.TestCase):

    def test_add(self):
        for _ in range(10):
            args = gen_args()
            self.assertEqual(script.add(*args), sum(args))

    def test_multi(self):
        for _ in range(10):
            args = gen_args()
            self.assertEqual(script.multi(*args), reduce(lambda x, y: x * y, args))


if __name__ == '__main__':
    unittest.main()
