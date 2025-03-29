def is_jolly_jumper(sequence):
    n = len(sequence)
    
    if n == 1:
        return True
    
    absolute_diff_set = set()
    
    for i in range(1, n):
        absolute_diff = abs(sequence[i] - sequence[i - 1])
        absolute_diff_set.add(absolute_diff)
    
    for i in range(1, n):
        if i not in absolute_diff_set:
            return False
    
    return True

sequence1 = [1, 4, 2, 3]
sequence2 = [1, 4, 2, -1, 6]
sequence3 = [11, 7, 4, 2, 1, 6]
sequence4 = [1, 3, 6, 7, 9]

print("Is sequence1 a Jolly Jumper?", is_jolly_jumper(sequence1))
print("Is sequence2 a Jolly Jumper?", is_jolly_jumper(sequence2))
print("Is sequence3 a Jolly Jumper?", is_jolly_jumper(sequence3))
print("Is sequence4 a Jolly Jumper?", is_jolly_jumper(sequence4))
