#!/usr/bin/env python3

# Author: Andres Wong
# Author_id: agwong-lam
# 2024/05/23

import sys

timer = len(sys.argv)
if timer != 2:
    timer = 3
else:
    timer = int(sys.argv[1])
while timer != 0:
    print(timer)
    timer = timer - 1
print('blast off!')

