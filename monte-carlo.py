
import random
  
INTERVAL= 1000

def monte_carlo():
    circle_points= 0
    square_points= 0
    pi = None

    for i in range(INTERVAL ** 2):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        origin_dist = x**2 + y**2

        if origin_dist <= 1:
            circle_points += 1
    
        square_points += 1
    
        pi = 4* circle_points/ square_points

    return '{0:.4g}'. format(pi)

print(monte_carlo())