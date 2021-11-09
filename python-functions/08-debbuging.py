def subtract(*nums):
    target_num = 1000

    for num in nums:
        target_num -= num

    return target_num


print(subtract(1, 2, 3, 4, 5))
