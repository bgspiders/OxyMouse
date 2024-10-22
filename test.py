#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
@Project ：OxyMouse 
@File    ：a.py
@IDE     ：PyCharm
@INFO     ：
@Author  ：BGSPIDER
@Date    ：22/10/2024 下午2:16
'''
from oxymouse.oxymouse import OxyMouse
mouse = OxyMouse(algorithm="perlin")
movements = mouse.generate_coordinates(from_x=400, from_y=500, to_x=1000, to_y=1200)
print(movements)