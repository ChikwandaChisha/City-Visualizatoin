# Author : Chikwanda Chisha
# Date: 11/05/2022
# Purpose : LAB3

def compares_func(a, b):
    if type(a) is str:
        return a.lower() <= b.lower()
    elif type(a) is int or type(a) is float:
        return a <= b


def partition(the_list, p, r, compare_func):
    j = p
    i = p - 1
    pivot = the_list[r]
    for j in range(p, r):
        if compare_func(the_list[j], pivot):
            i += 1
            the_list[i], the_list[j] = the_list[j], the_list[i]

        if j == r - 1:
            the_list[r], the_list[i + 1] = the_list[i + 1], the_list[r]  # swapping the values
            return i + 1


def quicksort(the_list, p, r, compare_func):
    if r - p < 1:  # base case
        return
    q = int(partition(the_list, p, r, compare_func))
    quicksort(the_list, q + 1, r, compare_func)
    quicksort(the_list, p, q - 1, compare_func)


def sort(the_list, compare_func):
    r = len(the_list) - 1
    p = 0  # sets the value of p when placed here
    quicksort(the_list, p, r, compare_func)


# names = ["John", "Lizzy", "Amazon", "Singapore", "Alave"]
# sort(names, compares_func)
# print(names)
