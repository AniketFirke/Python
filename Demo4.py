import math

def is_jolly(a, n):
    # Boolean vector to diffSet set of differences.
    # The vector is initialized as False.
    diff_set = [False] * n
    
    # Traverse all array elements
    for i in range(n - 1):
        # Find absolute difference between current two
        d = abs(a[i] - a[i + 1])
        
        # If difference is out of range or repeated,
        # return False.
        if d == 0 or d > n - 1 or diff_set[d]:
            return False
        
        # Set presence of d in set.
        diff_set[d] = True
    
    return True

# Driver Code
a = [11, 7, 4, 2, 1, 6]
n = len(a)
if is_jolly(a, n):
    print("Yes")
else:
    print("No")

