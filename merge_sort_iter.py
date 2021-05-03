import random
import time

def new_list(length):
    random_list = []
    for i in range(length):
        random_list.append(random.randint(0, 100))
    return random_list


def merge_sort(list_A, list_B):
    i = 0
    j = 0
    k = 0
    n = len(list_A) - 1
    m = len(list_B) - 1
    sorted_list = [0]*(n + m + 2)
    while i <= n and j <= m:
        if list_A[i] <= list_B[j]:
            sorted_list[k] = list_A[i]
            i += 1
        else:
            sorted_list[k] = list_B[j]
            j += 1
        k += 1
    while i <= n:
        sorted_list[k] = list_A[i]
        k += 1
        i += 1
    while j <= m:
        sorted_list[k] = list_B[j]
        k += 1
        j += 1
    return sorted_list


test_list_1 = new_list(random.randint(5, 10))
test_list_2 = new_list(random.randint(5, 10))
test_list_1.sort()
test_list_2.sort()
print("Listy: ")
print(test_list_1)
print(test_list_2)
print()
start = time.perf_counter_ns()
test_list = merge_sort(test_list_1, test_list_2)
stop = time.perf_counter_ns()
print(test_list)
print()
print("Sortowanie zajęło:", str(stop - start), "nanosekund")
