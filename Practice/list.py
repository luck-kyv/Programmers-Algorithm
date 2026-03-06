# Two Sum
# Dictionary
# def two_sum(nums, target):
#     # dict 변환
#     num_dict = {n: True for n in nums}
#     # num 반복문
#     # target - n 이 있는지 확인 , 같은 원소 x
#     for n in num_dict:
#         needed_num = target - n
#         if needed_num != n and needed_num in num_dict:
#             return True
#     return False 

# Sort + Two Pointer
# def two_sum(nums, target):
#     nums.sort()
#     left, right = 0, len(nums) - 1
#     while left < right:
#         if nums[left] + nums[right] == target:
#             return True
#         elif nums[left] + nums[right] > target:
#             right -= 1
#         else:
#             left += 1
#     return False


# print(two_sum([4, 1, 9, 7, 5, 3, 16], 14))
# print(two_sum([2, 1, 5, 7], 4))

# Design Browser History
# class LinkNode(object):
#     def __init__(self, val, prev=None, next=None):
#         self.val = val
#         self.prev = prev
#         self.next = next

# class BrowserHistory(object):
#     def __init__(self, homepage):
#         self.current = LinkNode(val=homepage)
        
#     def visit(self, url):
#         # new node - 현 페이지의 next와 연결, current 이동
#         self.current.next = LinkNode(val=url, prev=self.current)
#         self.current = self.current.next
#         return None

#     def back(self, steps):
#         # step만큼 prev쪽으로 이동, prev이 none이 아닐때까지 
#         while self.current.prev and steps != 0:
#             self.current = self.current.prev
#             steps -= 1
#         return self.current.val
        
#     def forward(self, steps):
#         # step만큼 next쪽으로 이동, next가 none이 아닐때까지 
#         while self.current.next and steps != 0:
#             self.current = self.current.next
#             steps -= 1
#         return self.current.val


# browserHistory = BrowserHistory("leetcode.com")
# print(browserHistory.visit("google.com"))
# print(browserHistory.visit("facebook.com"))
# print(browserHistory.visit("youtube.com"))
# print(browserHistory.back(1))
# print(browserHistory.back(1))
# print(browserHistory.forward(1))
# print(browserHistory.visit("linkedin.com"))
# print(browserHistory.forward(2))
# print(browserHistory.back(2))
# print(browserHistory.back(7))


# Two Sum
# def two_sum(nums, target):
#     nums_dict = {n:True for n in nums}

#     for n in nums:
#         needed_n = target - n
#         if (needed_n in nums_dict) & (needed_n != n):
#             return True
#     return False

# def two_sum(nums, target):
#     n = len(nums)
#     for i in range(n):
#         for j in range(i+1, n):
#             if nums[i] + nums[j] == target:
#                 return True
#     return False

# def two_sum(nums, target):
#     nums.sort()
#     l, r = 0, len(nums) - 1
#     while l < r:
#         if nums[l] + nums[r] == target:
#             return True
#         elif nums[l] + nums[r] < target:
#             l += 1
#         else:
#             r -= 1
#     return False

# print(two_sum([4, 1, 9, 7, 5, 3, 16], 14))
# print(two_sum([2, 1, 5, 7], 4))

# BrowserHistory
class ListNode(object):
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory(object):
    def __init__(self, homepage):
        self.head = self.current = ListNode(val=homepage)
    
    def visit(self, url):
        self.current.next = ListNode(val=url, prev=self.current)
        self.current = self.current.next

    def back(self, steps):
        while steps > 0 and self.current.prev != None:
            steps -= 1
            self.current = self.current.prev
        return self.current.val
    
    def forward(self, steps):
        while steps > 0 and self.current.next != None:
            steps -= 1
            self.current = self.current.next
        return self.current.val
    
browserHistory = BrowserHistory("leetcode.com")
print(browserHistory.visit("google.com"))
print(browserHistory.visit("facebook.com"))
print(browserHistory.visit("youtube.com"))
print(browserHistory.back(1))
print(browserHistory.back(1))
print(browserHistory.forward(1))
print(browserHistory.visit("linkedin.com"))
print(browserHistory.forward(2))
print(browserHistory.back(2))
print(browserHistory.back(7))