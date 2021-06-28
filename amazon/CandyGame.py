
def candy(ratings):
    candies = [1] * len(ratings)

    for i in range(1, len(ratings)):
        if(ratings[i-1] < ratings[i]):
            candies[i] = candies[i-1] + 1
    print('first iter', candies)

    for i in range(len(ratings)-1, 0, -1):
        if(ratings[i-1] > ratings[i]):
            candies[i-1] = candies[i] + 1
    print('second iter', candies)

    return sum(candies)


print(candy([1, 3, 2, 2, 1]))  # 7
print(candy([1, 0, 2]))  # 5
print(candy([1, 2, 2]))  # 4
