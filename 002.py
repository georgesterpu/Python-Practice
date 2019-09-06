def sortNums(nums):
    # Fill this in.
    counts = {1: 0, 2: 0, 3: 0}
    for val in nums:
        counts[val] += 1
    return [1] * counts[1] + [2] * counts[2] + [3] * counts[3]

print(sortNums([3, 3, 2, 1, 1 , 1, 1, 3, 2, 1, 3 ,3, 3 , 2]))
# [1, 1, 2, 2, 3, 3, 3]