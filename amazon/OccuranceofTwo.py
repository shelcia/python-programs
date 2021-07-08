# Number of occurrences of 2 as a digit in numbers from 0 to n


# Count the number of 2s as digit in all numbers from 0 to n.

# Examples :

# Input : 22
# Output : 6
# Explanation: Total 2s that appear as digit
#              from 0 to 22 are (2, 12, 20,
#              21, 22);

# Input : 100
# Output : 20
# Explanation: total 2's comes between 0 to 100
# are (2, 12, 20, 21, 22..29, 32, 42, 52, 62, 72,
# 82, 92);

def OccuranceOfTwos(n):

    num = 0
    twoCount = 0

    while num <= n:
        twoCount += list(str(num)).count('2')
        num += 1

    return twoCount


print(OccuranceOfTwos(22))  # 6
print(OccuranceOfTwos(100))  # 20
