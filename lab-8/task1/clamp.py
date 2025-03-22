
def clamp(var,lower_bound,upper_bound): # math function that is often used in game engines to limit upper/lower bounds of integer or float variable. i implmemented it to limit rotation
    return max(lower_bound,min(var,upper_bound))