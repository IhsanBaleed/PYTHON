import array

def array_test_1():

    array1 = [21,52,73]
    print(array1)

    # i is used here to indicate an int
    my_array = array.array('i', [11, 22, 33, 44, 55])
    print(my_array)

    # iterating per item
    for item in array1:
        print (item)

    # range(start, stop, step), the stop is mandatory, and it excludes stop
    for i in range(len(my_array)):
        print (my_array[i])

    for i in range(2, len(my_array)):
        print (my_array[i])

    for i in range(2, len(my_array), 2):
        print (my_array[i])

def switch_test():
    data = 7
    match data:
        case 1:
            print("Got 1")
        case 2:
            print("Got 2")
        case 7:
            print("Got 7")
        case _: # this would be the default case
            print("Default")
