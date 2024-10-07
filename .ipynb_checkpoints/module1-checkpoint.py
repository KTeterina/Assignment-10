#module 1: find 2 smallest numbers in a list
def find_two_smallest(numbers):
    """This function finds 2 smallest values in a list"""
    smallest1 = min(numbers)
    smallest2 = float('inf')
    for n in numbers:
        if n < smallest2 and n != smallest1:
            smallest2 = n
    return smallest1, smallest2