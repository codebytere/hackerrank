'''
Given a list of unsorted integers, can you find the pair of elements that have the smallest absolute difference between them? If there are multiple pairs, find them all.

Input Format
The first line of input contains a single integer, N, representing the length of array A.
In the second line, there are N space-separated integers representing the elements of array A.
'''

def closest_numbers():
    arr_len = int(input())
    arr = [int(num) for num in input().split(" ")]
    arr.sort()
    smallest_diff = 1<<31-1
    smallest_pairs = []

    for index in range(len(arr)-1):
        diff = arr[index+1] - arr[index]

        if diff < smallest_diff:
            smallest_diff = diff
            smallest_pairs = [str(arr[index]) + " " +  str(arr[index+1])]
        elif diff == smallest_diff:
            smallest_pairs.append(str(arr[index]) + " " + str(arr[index+1]))

    print(" ".join(smallest_pairs))

closest_numbers()



