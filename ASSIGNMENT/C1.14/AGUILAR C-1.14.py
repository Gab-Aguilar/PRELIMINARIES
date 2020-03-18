def odd_product(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                product = nums[i] * nums[j]
                if product & 1:
                    return True
                    return False


list = [3,3,24,32,36,75]
print(list, odd_product(list));

