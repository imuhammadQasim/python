# def candy(ratings):
#     n = len(ratings)
#     candies = [1] * n
#     print(candies)
#     # Left to right
#     for i in range(1, n):
#         if ratings[i] > ratings[i-1]:
#             candies[i] = candies[i-1] + 1
#             print(candies)
    
#     for i in range(n-2 , -1 , -1):
#         if ratings[i] > ratings[i+1]:
#             candies[i] = max(candies[i], candies[i+1] + 1)
#             print(candies)

# rating = [1, 0, 2]
# candy(rating)

# nums = [1,2,4,5,6]

# n = len(nums) + 1
# expected = n * (n + 1) // 2
# print(expected)
# actual = sum(nums)
# missing = expected - actual
# for i in range(n):
#     temp =0
#     if nums[i] < missing and nums[i+1] > missing:
#         nums.insert(i+1, missing)
#         break

# print(nums)

# arr = [1,2,3,4,5,6,7]
# k = 3
# n = len(arr)

# k = k% len(arr)

# arr = arr[-k:]+ arr[:-k]

# print(arr)



# arr = [1,2,0,0,3,4,0,5,6,7]

# count = 0
# result = []
# for i in range(len(arr)):
#     if arr[i] ==0:
#         count+=1
#     else:
#         result.append(arr[i])
# while (count > 0):
#     result.append(0)
#     count -=1

# print(result)



# arr = [1,2,0,0,3,4,0,5,6,7]

# zero_count = 0
# result = []
# inserted_zero = 0
# for i in range(len(arr)):
#     if arr[i] == 0:
#         zero_count +=1

# print(zero_count)

# for num in arr:
#     if num !=0:
#         result.append(num)
    
#         if inserted_zero < zero_count:
#             result.append(0)
#             inserted_zero +=1
#         else:
#             break
# print(result)



# arr = [3,7,2,8,5,10,1]
# count_even = 0
# count_odd = 0
# for num in arr:
#     if num % 2 ==0:
#         count_even +=1
#     else:
#         count_odd +=1

# print("count_odd", count_odd)
# print("count_event", count_even)



# arr = [1,0,2,0,3,4,0]
# count = 0
# for num in arr:
#     if num ==0:
#         count +=1


# arr = [1,0,2,3,0,4]

# i = 0 

# while(i < len(arr)):
#     if arr[i] ==0:
#         arr.insert(i+1 , 0)
#         i+=2
#     else:
#         i+=1
# print(arr)



# arr = [1,2,4,5]
# sum = 0
# n = len(arr) +1

# expected = n * (n+1)//2
# print(expected)

# for num in arr:
#     sum +=num
# print(sum) 

# missing = expected - sum
# print(missing)


# arr = [1,1,2,2,3,3,4]


# arr = [2,11,15,7]
# target = 9

# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if arr[i] + arr[j] == target:
#             print (i, j)
#     else:
#         "Not Found"



# arr = [4,5,1,2,0,4,5,1,2,0]

# for x in arr:
#     count = 0
#     for y in arr:
#         if x == y:
#             count +=1
    
#     if count ==1:
#         print(x)
#         break


# arr = [1,2,3,4,5,6,7,8]

# def binarySearch(arr, target):
#     h = len(arr)-1
#     l = 0
#     for i in range(len(arr)):
#         mid = (l+h)//2
#         if(target == arr[mid]):
#             return mid
#         if(target > arr[mid]):
#             l= mid+1
#         else:
#             h= mid-1
#     return " Not found"


# # print(binarySearch(arr, 7))


# left = [1,3,5,7]
# right = [2,4,6,8]

# def mergeSort(arr1, arr2):
#     i = 0 
#     j = 0 
#     result = []

#     while(i < len(arr1) and j < len(arr2)):
#         if arr1[i] < arr2[j]:
#             result.append(arr1[i])
#             i+=1
#         else:
#             result.append(arr2[j])
#             j+=1
    
#     while(i < len(arr1)):
#         result.append(arr1[i])
#         i +=1
#     while(j < len(arr2)):
#         result.append(arr2[j])
#         j +=1

#     return binarySearch(result, 7)


# print(mergeSort(left, right))


# arr = [1,3,5,7,0]

# result = []
# i =0
# j = len(arr)-1

# while i <=j:
#     result.append(arr[i])
#     i+=1

#     if i<=j:
#         result.append(arr[j])
#         j-=1


# print(result)




# i = 0
# j = len(s)-1
# is_palindrome= True  
# print(s[i])
# while i<=j:
#     if s[i] != s[j]:
#         is_palindrome = False
    
#     i+=1
#     j-=1

# if is_palindrome:
#     print("The string is palindorme")
# else:
#     print("The string is not palindorme")


s = "reviver"

mid = len(s)//2
l = mid -1
h = mid +1
is_palindrom = True

while l >=0 and h<len(s):
    if s[l] != s[h]:
        is_palindrom = False
    l-=1
    h+=1

if is_palindrom:
    print("The string is palindorme")
else:
    print("The string is not palindorme")
