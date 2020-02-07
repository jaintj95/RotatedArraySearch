def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    start_idx = 0
    end_idx = len(input_list) - 1

    result = mod_binary_search(input_list, number, start_idx, end_idx) 

    return result


def mod_binary_search(input_list, number, start_idx, end_idx):

    # if start_idx has crossed the end_idx while recursing, return -1
    if start_idx > end_idx:
        return -1

    mid_idx = (end_idx+start_idx) // 2

    if input_list[mid_idx] == number:
        return mid_idx

    # check if right-half array is sorted
    if input_list[mid_idx] <= input_list[end_idx]:
        
        # if number lies in this range, use binary search to find it
        if input_list[mid_idx] <= number <= input_list[end_idx]:
            return mod_binary_search(input_list, number, mid_idx+1, end_idx)

        else:
            return mod_binary_search(input_list, number, start_idx, mid_idx-1)
     

    # if right-half is not sorted, left-half is definitely sorted
    else:
        # if number lies in range of values in left-half, use binary search
        if input_list[start_idx] <= number <= input_list[mid_idx]:
            return mod_binary_search(input_list, number, start_idx, mid_idx-1)

        else:
            return mod_binary_search(input_list, number, mid_idx+1, end_idx)
            

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])