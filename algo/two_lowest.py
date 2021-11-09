#When given a list of elements, find the two lowest elements. They can be equal to each other or different
#o(n)
def two_lowest(input):
    result = []
    result.append(min(input))
    input.remove(min(input))
    result.append(min(input))
    return result

list1=[190,89,3,4,2,2]
print(two_lowest(list1))
list2=[3,6,10,9,8]
print(two_lowest(list2))

