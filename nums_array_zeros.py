"""
Your grade will be judged on:
Solve the following question and create test cases with unittest.
    Ability to solve the question (speed of your solution will not affect your grade,
    but efficiency is king)
    Correctly creating your Test file
    Choosing The correct Test Cases to ensure your solution is valid.

Given an array nums, write a function to move all zeroes to the end of it 
while maintaining the relative order of
the non-zero elements.
array1 = [0, 1, 0, 3, 12]
Output:
[1, 3, 12, 0, 0]

array2 = [1, 7, 0, 0, 8, 0, 10, 12, 0, 4]
Output:
[1, 7, 8, 10, 12, 4, 0, 0, 0, 0]
"""
array1 = [0, 1, 0, 3, 12]
array2 = [1, 7, 0, 0, 8, 0, 10, 12, 0, 4]

# This did not pass any tests:
# def move_zeros(alist):
#     for n in alist:
        # n = 0
        # alist.append(alist.pop(alist.index(0))) #original
        # alist.pop(alist.append(n)) #int issue
        # alist.append(alist.pop(0)) #did not remove 0 from front
#     return alist 

def move_zeros(alist):
    for n in alist:
        no_zlist = [n for n in alist if n !=0]
        zlist = [n for n in alist if n == 0]        
    c_list = no_zlist + zlist
    return c_list

# def move_zeros(alist):
#     zlist = []
#     for n in alist:
#         while n in alist:
#             if n != 0:
#                 continue
#             if n == 0:
#                 zlist.append(n) 
#                 alist.remove(n)     
#     return alist.append(zlist)

# Marcus' Method: doesn't work in terminal
# def move_zeros(alist):
#     length_list = len(alist)
#     n = 0
#     for i in range(length_list):
#         alist[n] = alist[i]
#         n += 1 if alist[i] else 0
#     alist[n:] - [0] * (length_list -n)
#     return alist
      
print(move_zeros([0,0,1,2,3,4]))
print(move_zeros([0, 1, 0, 3, 12]))
print(move_zeros([1, 7, 0, 0, 8, 0, 10, 12, 0, 4]))  
