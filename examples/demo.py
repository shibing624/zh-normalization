# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description:
"""
import sys

sys.path.append('..')
from zh_normalization import TextNormalizer
if __name__ == '__main__':
    m = TextNormalizer()
    text = "电影中梁朝伟扮演的陈永仁的编号27149!啊——但是《原神》是由,米哈\游100％自主，研发的一款全.新开放世界.冒险游戏.呣呣呣～就是…大人的鼹鼠党吧？"
    sents = m.normalize(text)
    new_text = ''.join(sents)
    print(text)
    print(sents)
    print(new_text)
    # output: 电影中梁朝伟扮演的陈永仁的编号二七幺四九!啊但是原神是由,米哈游百分之一百自主，研发的一款全.新开放世界.冒险游戏.呣呣呣至就是大人的鼹鼠党吧？
