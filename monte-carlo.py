
import random

"""
This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate 
π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""

  
INTERVAL= 1000

def monte_carlo():
    circle_points= 0
    square_points= 0
    pi = None

    for i in range(INTERVAL ** 2): # O(INTERVAL ** 2) = O(1)
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        origin_dist = x**2 + y**2

        if origin_dist <= 1:
            circle_points += 1
    
        square_points += 1
    
        pi = 4* circle_points/ square_points

    return '{0:.4g}'. format(pi)

print(monte_carlo())

"""
Time complexity:
    if INTERVAL is constant => O(1)
    else O(n**2)
Space complexity = O(1)
"""