# This problem can be solved using a sliding window approach.
# We can start by initializing two pointers, left and right, to the beginning of the list. 
# We will also initialize a variable, current_sum, to the value of the first element in the list.
# Then, we can then iterate over the list, moving the right pointer forward by one element at a time. 
# At each iteration, we will add the current element to current_sum. If current_sum is greater than or equal to the target t, we can start moving the left pointer forward until current_sum is less than t. If at any point current_sum is equal to t, we have found a valid sublist and can return its indices.
# If we reach the end of the list without finding a valid sublist, we can return [-1, -1].


def solution(l, t):
    left, right = 0, 0
    current_sum = l[0]

    while right < len(l):
        if current_sum == t:
            return [left, right]
        elif current_sum < t:
            right += 1
            if right < len(l):
                current_sum += l[right]
        else:
            current_sum -= l[left]
            left += 1

    return [-1, -1]