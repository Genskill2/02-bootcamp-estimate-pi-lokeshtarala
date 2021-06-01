# import random
# import math
# print(random.random())
# for a in range(1,5+1):
#     print(a)
# origin = [0,0]
# point = [3,4]
# print(math.dist(point,origin))

import math
from typing import Sequence
import unittest
import random

def monte_carlo(noOfDarts):
    distance = float()
    circleChance =  0.0
    origin = [0.0,0.0]
    point = [0.0,0.0]
    for m in range(1,noOfDarts + 1):
        point[0] = random.random()
        point[1] = random.random()
        distance = math.dist(point,origin)
        if distance < 1.0:
            circleChance += 1.0  
    print(circleChance)
    return circleChance/(noOfDarts - circleChance )    
print(monte_carlo(15000))