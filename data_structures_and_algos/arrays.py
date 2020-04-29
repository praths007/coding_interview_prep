import itertools
import functools

'''
############################################################
print("product of sub arrays using iter tools")
def prod_of_sub_arrays():
    arr = [10, 3, 7]

    merged_list = []
    # making combinations
    for i in range(1, len(arr)):
        merged_list.append(list(itertools.combinations(arr, i)))

    # flattening list of combinations with products of each tuple
    flat_list = []
    for item in merged_list:
        for items in item:
            prod = functools.reduce(lambda x,y :x*y, items)
            flat_list.append(prod)

    # overall product of flattened list
    print(functools.reduce(lambda x,y :x*y, flat_list + [10, 3, 7]))
    print(flat_list + [functools.reduce(lambda x,y:x*y, [10, 3, 7])])
prod_of_sub_arrays()
'''

############################################################
print("product of sub arrays using iter tools")
arr = [10, 3, 7, 9, 1]
i = 0
j = len(arr) - 1
while i<j:
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    i +=1
    j -=1

print(arr)


# sorting (bubble sort)
for i in range(0, len(arr)-1):
    for j in range(i, len(arr)-1):
        if arr[j] > arr[j+1]:
            tmp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = tmp
print(arr)


# sorting log(n)

# for i in range(1, (len(arr)-1):
#     tmp1 = arr[i]
#     arr[i] = arr[j]
#     arr[j] = tmp
#     i += 2
#     j -= 2




