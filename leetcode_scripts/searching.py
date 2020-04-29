# def bin_search(numbers, num):
#     n = len(numbers)
#     left = 0
#     right = n - 1
#     while left < right:
#         mid = (int)((left + right) / 2)
#         if numbers[mid] == num:
#             return(mid)
#         elif numbers[mid] > num:
#             right = mid - 1
#         elif numbers[mid] < num:
#             left = mid + 1
#
# binlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# num = 9
#
# print(bin_search(binlist, num))


def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    search_space = list(range(1, x))
    left = 0
    right = len(search_space) - 1
    if x == 1:
        return 1
    while left <= right:
        mid = (int)((left + right) / 2)
        if search_space[mid]**2 == x:
            return search_space[mid]
        elif search_space[mid]**2 > x:
            right = mid - 1
        elif search_space[mid]**2 < x:
            left = mid + 1
    return left

print(mySqrt(2))




