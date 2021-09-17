#!/usr/bin/python3
import sys

def main():
    next_biggest_number(sys.argv[1])


def next_biggest_number(num):
    nums = [n for n in str(num)] # O(n)

    num_digits = len(nums)

    for i in range(num_digits-1, 0, -1): # O(n)
        if nums[i-1] < nums[i]:
            # print(f"nums[{i-1}]={nums[i-1]} < nums[{i}]={nums[i]}") # decrease

            # next largest element
            next = i
            for j in range(i, num_digits):
                if nums[j] > nums[i-1] and nums[j] <= nums[next]:
                    next = j
            
            # swap
            temp = nums[i-1]
            nums[i-1] = nums[next]
            nums[next] = temp

            nums[i:num_digits] = nums[i:num_digits][::-1] # reverse remainder
            # print(int(''.join(nums)))
            return int(''.join(nums))
    return -1

if __name__ == "__main__":
    main()

"""
nbn(83800) == 88003
     ^^    find decrease, next largest element, swap O(n)
    88300
      ^^^  reversed remainder O(n)
    88003

nbn(83410) == 83810
     ^^    find decrease, next largest element, swap O(n)
    84310  
      ^^^  reversed remainder O(n)
    84013

nbn(49396) == 49639
      ^ ^  find decrease, next largest element, swap O(n)
    49693
       ^^
    49939  reversed remainder O(n)

nbn(98421005431) == 98421010345
          ^   ^  find decrease, next largest element, swap O(n)
    98421015430
           ^^^^  reversed remainder O(n)
    98421010345
"""
