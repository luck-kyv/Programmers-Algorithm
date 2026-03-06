# Two sum
# hash table 사용 - in O(1)
# def two_sum(nums, target):
#     # dict 선언
#     num_dict = {n: True for n in nums}

#     # 반복문 내 
#     # target - nums 가 있는지 확인(같은 숫자 x)
#     for n in nums:
#         needed_num = target - n
#         if needed_num != n and needed_num in num_dict:
#             return True
#     return False

# print(two_sum([4, 1, 9, 7, 5, 3, 16], 14))
# print(two_sum([2, 1, 5, 7], 4))

# Longest Consecutive Sequence 

def longestConsecutive(nums):
    # dict 선언
    longest = 0
    num_dict = {n:True for n in nums}

    # 반복문
    for n in nums:
        # 이전 숫자가 없다면
        if n-1 not in num_dict:
            cnt = 1
            target = n+1
            # cnt ++, target 이 있는동안 cnt ++ target ++
            while target in num_dict:
                cnt += 1
                target += 1
            # 끝나면 max update
            longest = max(cnt, longest)
    return longest

print(longestConsecutive([100, 4, 200, 1, 3, 2]))
print(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
