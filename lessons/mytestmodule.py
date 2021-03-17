import numpy as np

def only_evens(list_of_numbers):
    list_of_evens = []
    for each_number in list_of_numbers:
        if each_number % 2 == 0:
            list_of_evens.append(each_number)
        else:
            pass
    return(list_of_evens)

def only_evens_numpy(list_of_numbers):
    list_array = np.array(list_of_numbers)
    check_for_evens = list_array % 2 == 0
    even_numbers_list = list_array[check_for_evens]
    return(even_numbers_list)
