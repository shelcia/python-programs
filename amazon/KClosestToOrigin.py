

def kClosest(points, k):

    # arr = []

    # for x, y in points:

    #     dist = (x**2) + (y**2)
    #     arr.append([dist, x, y])

    # arr.sort(key=lambda x: x[0])

    # res = []

    # for dist, x, y in arr:
    #     res.append([x, y])

    # return res[:k]

    return sorted(points, key=lambda x: x[0]**2 + x[1]**2)[:k]


print(kClosest([[3, 3], [5, -1], [-2, 4]], 2))
