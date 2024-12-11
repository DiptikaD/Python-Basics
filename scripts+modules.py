import math
print(math.sqrt(9))
#you can import modules (python's version of packages) and call upon their functions/methods. Could also instead:
from math import e, pi
print(pi + e)
# this is best for multiple uses, but isnt really neccessary

# can also rename functions if there happens to be imports sharing the same function names.

from math import sqrt
from cmath import sqrt as csqrt
#cmath is complex math. if i had not overriden the name, the sqrt function from math would have been taken over by the cmath sqrt, therefore the math function would have been ignored. 
#can do the same to the whole module also!
import random as ra
print(ra.randint(0,9)+1)