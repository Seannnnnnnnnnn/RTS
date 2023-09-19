def highestPowerof2(x):
    # check for the set bits
    x |= x >> 1
    x |= x >> 2
    x |= x >> 4
    x |= x >> 8
    x |= x >> 16
     
    # Then we remove all but the top bit by xor'ing the
    # string of 1's with that string of 1's shifted one to
    # the left, and we end up with just the one top bit
    # followed by 0's.
    return x ^ (x >> 1)
 

p2 = set()
for i in range(10000):
    if highestPowerof2(i) not in p2: print(i, highestPowerof2(i))
    p2.add(highestPowerof2(i))
    