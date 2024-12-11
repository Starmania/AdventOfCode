import os

os.chdir(os.path.dirname(__file__))

is_safe = 0

with open('input', 'r', encoding="utf8") as f:
    for line in f.readlines():
        nums = tuple(map(int, line.split()))
        if nums[0] > nums[1]:
            for i in range(len(nums)-1):  # Level should decrease
                # print(nums[i] - nums[i+1])
                if not 0 < nums[i] - nums[i+1] < 4:
                    break
            else:
                is_safe += 1
        else:
            for i in range(len(nums)-1):  # Level increase
                # print(nums[i] - nums[i+1])
                if not -4 < nums[i] - nums[i+1] < 0:
                    break
            else:
                is_safe += 1

print(is_safe)
