# We need to search for answer in the range 1010101010 - 1389026623
# But we know that our answer must end in 30 or 70. So we can reduce the search space to 10101010 - 13890266 and append 30, 70

for num in (a + b for a in (30, 70) for b in xrange(1389026600, 1010101000, -100)):
    if str(num * num)[::2] == '1234567890':
        break

print(num)