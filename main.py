def majorityElement(list):
    answer = None
    for item in list:
        if answer == None or item > answer:
            answer = item

    return answer

#Example 1:
#Input: 
nums = [3,2,3]
print(majorityElement(nums))
#Output: 3

#Example 2:
#Input: 
nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))
#Output: 2
 