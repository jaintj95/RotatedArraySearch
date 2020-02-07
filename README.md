# Rotated Array Search

## Problem Statement

You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

Example:
Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

## Solution

Initially, I implemented a 2 pass algorithm, where the algorithm first searches for the pivot element in the list and then uses this pivot index to run binary search.

However, while searching for a more efficient way to do this, I landed on the following stackoverflow post which I used as reference for implementing a revised algorithm - https://stackoverflow.com/questions/4773807/searching-in-a-sorted-and-rotated-array

Basically, we run a single pass binary search which is modified to suit our needs.

At any given point, atleast one half of the array (either left or right) is correctly sorted.

Example arrays from my notes:

[4, 5, 7, 8, 10, 0, 1, 2] (Left half is sorted)

[8, 10, 0, 1, 2, 4, 5, 7] (Right half is sorted)

[10, 0, 1, 2, 4, 5, 7, 8] (Again right half is still sorted)

Let's use the last example array to see how the algorithm works step-by-step.

Suppose we are searching for the number 0 in the array [10, 0, 1, 2, 4, 5, 7, 8]

1) First calculate the middle index (4) and check if number is present there. (Not present)

2) Then check if right half of the array is sorted by comparing values of mid item and last item. (It is sorted in this case)
2.1) Now, check if the number we are searching for lies in the range of items in right-half of array. If it does, then we recursively perform binary search on the new smaller region [5, 7, 8]
2.2) Otherwise we perform binary search of the left half region [10, 0, 1]  
  
3) If left half of the array is sorted, we follow similar steps and recursively search for the item.

Time Complexity: O(log n) because we are using a slightly modified binary search algorithm.

Space Complexity: Since, this is a recursive algorithm, it uses stack space that needs to be taken into account for space complexity. The algorithm only uses some additional variables and does not create copy of the main array. In my calculation the space complexity would be O(log n) because if input size is n we make a maximum of log n sub calls to find the element.