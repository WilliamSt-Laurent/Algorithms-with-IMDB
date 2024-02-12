# write your code here
import re
import time


def swap(array, first_index, second_index):
    first_item = array[first_index]
    array[first_index] = array[second_index]
    array[second_index] = first_item


def bubble_sort(array):
    array_length = len(array)

    swapped = True

    while swapped is True:
        swapped = False
        for n in range(0, array_length - 1):
            if array[n][1] > array[n + 1][1]:
                swap(array, n, n + 1)
                swapped = True

    return array


def merge_sort(array, left, right):
    if left < right:
        center = int((left + right) / 2)
        merge_sort(array, left, center)
        merge_sort(array, center + 1, right)
        merge(array, left, center, right)


def merge(array, left, mid, right):
    len1 = mid - left + 1
    len2 = right - mid

    left_array = [0] * len1
    right_array = [0] * len2

    for e in range(len1):
        left_array[e] = array[left + e]
    for j in range(len2):
        right_array[j] = array[mid + 1 + j]

    i = 0
    j = 0
    k = left

    while i < len1 and j < len2:
        if left_array[i][1] <= right_array[j][1]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1
        k += 1

    while i < len1:
        array[k] = left_array[i]
        i += 1
        k += 1
    
    while j < len2:
        array[k] = right_array[j]
        j += 1
        k += 1


movie_dict = []

with open("movies.csv", newline='', encoding="UTF-8") as file:
    for line in file:
        line_stripped = line.strip("\r\n")
        movie_no_quote = re.sub('"', '', line_stripped)
        movie_entry = movie_no_quote.rsplit(",", 1)
        movie_entry[1] = float(movie_entry[1])
        movie_dict.append(movie_entry)


start_time = time.time()

length = len(movie_dict)
merge_sort(movie_dict, 0, length - 1)

end_time = time.time()


# for movie in movie_dict:
#     print(movie[0], movie[1], sep=" - ")


# binary search logic below

continue_search = True

while continue_search:
    low = 0
    high = len(movie_dict) - 1

    while True:
        middle = int((low + high) / 2)
        middle_element = movie_dict[middle]

        if middle_element[1] == 6.0:
            print(middle_element[0], middle_element[1], sep=' - ')
            movie_dict.pop(middle)
            break
        elif float(middle_element[1]) < 6.0:
            low = middle + 1
        else:
            high = middle - 1

        if low == high:
            continue_search = False


# print("The operation took: {} seconds".format(end_time - start_time))
