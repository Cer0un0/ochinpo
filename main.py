# -*- coding: utf-8 -*-
import random
ochinpo = ['お', 'ち', 'ん', 'ぽ']
s = [random.choice(ochinpo) for i in range(4)]
o = s[0] + s[1] + s[2] + s[3]
i = 0
while(True):
    o += random.choice(ochinpo)
    if o[len(o)-12:] == 'おちんぽ':
        print o
        print 'イグゥゥゥゥ'
        print 'あなたは{}回目でイキました'.format(i+5)
        exit()
    i += 1
