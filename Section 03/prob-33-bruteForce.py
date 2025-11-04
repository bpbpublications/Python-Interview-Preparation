def trap(height):
    n = len(height)
    water_trapped = 0
 
    for i in range(n):
        left_max = max(height[:i+1])  # Maximum height to the left of the current bar
        right_max = max(height[i:])   # Maximum height to the right of the current bar
        water_trapped += min(left_max, right_max) - height[i]
 
    return water_trapped
