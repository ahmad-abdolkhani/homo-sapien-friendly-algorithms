def selection_sort(list):
    return result_of_outer_loop(list)


def result_of_outer_loop(list):
    for nextSmallestIndex in range(len(list)):
        inner_loop(list, nextSmallestIndex)
    return list


def inner_loop(list, nextSmallestIndex):
    minIndex = nextSmallestIndex
    for i in range(nextSmallestIndex, (len(list))):
        if (list[i] < list[minIndex]):
            minIndex = i
    update_list(list, nextSmallestIndex, minIndex)


def update_list(list, current, minIndex):
    list[current], list[minIndex] = list[minIndex], list[current]
