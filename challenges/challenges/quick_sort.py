def quick_sort(input_list, left, right):

    if left < right:
        p = partition(input_list, left, right)
        quick_sort(input_list, left, p - 1)
        quick_sort(input_list, p + 1, right)

    return input_list

def partition(input_list, left, right):

    pivot = input_list[right]
    i = left - 1

    for j in range(left, right):
        if input_list[j] <= pivot:
            i = i + 1
            (input_list[i], input_list[j]) = (input_list[j], input_list[i])

    (input_list[i + 1], input_list[right]) = (input_list[right], input_list[i + 1])

    return i + 1

if __name__ == "__main__":
    print (quick_sort([8,4,23,42,16,15], 0, len([8,4,23,42,16,15])-1))