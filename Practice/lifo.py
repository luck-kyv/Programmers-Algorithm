# Valid Parentheses
# def isValid(s):
#     # stack - 여는괄호면 닫는괄호 넣기, 닫는괄호면 top이랑 비교해서 같은지 확인
#     # 남는게 없다면 True
#     stack = []
#     for c in s:
#         if c == '(':
#             stack.append(')')
#         elif c == '{':
#             stack.append('}')
#         elif c == '[':
#             stack.append(']')
#         elif not stack or stack.pop() != c:
#             return False
#     return not stack

# print(isValid(")("))
# print(isValid("([]}"))
# print(isValid("{()[]}"))

# Daily Temperatures
# def dailyTemperatures(temperatures):
#     # enumerate - idx(날짜), temp(온도) 반복문 안
#     # 낮은 온도 들어오면 append
#     # 높은 온도 들어오면 pop, idx 계산 후 answer에 넣기
#     answer = [0 for _ in range(len(temperatures))]
#     stack = []
#     for cur_day, cur_temp in enumerate(temperatures):
#         while stack and stack[-1][1] < cur_temp:
#             prev_day, _ = stack.pop()
#             answer[prev_day] = cur_day - prev_day
#         stack.append((cur_day, cur_temp))
#     return answer

# print(dailyTemperatures([73,74,75,71,69,72,76,73]))
# print(dailyTemperatures([30, 40, 50, 60]))         
# print(dailyTemperatures([30, 60, 90]))    