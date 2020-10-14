if __name__ == "__main__":

    array = [80, 60, 70, 2, 3, 3, 20, 50]

    first_largest = 0
    second_largest = 0

    first_smallest = array[0]   # b/c largest will be checked on first
    second_smallest = array[0]
    
    for i in array:
        # print("current: %s" % i)
        # print("second_largest: %s" % second_largest)
        # print("second_smallest: %s" % second_smallest)

        if i > first_largest:
            print("a")
            second_largest = first_largest
            first_largest = i
        elif i > second_largest and i < first_largest:
            print("b")
            second_largest = i
        elif i < first_smallest:
            print("c")
            second_largest = first_smallest
            first_smallest = i
        elif i < second_smallest and i > first_smallest:
            print("d")
            second_smallest = i

    print("second_largest: %s" % second_largest)
    print("second_smallest: %s" % second_smallest)
