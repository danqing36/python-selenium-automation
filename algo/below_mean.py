#When given a list, the program should return a list of all the elements below the original list's arithmetical mean.
#o(n)
def below_mean(input):
    result = []
    mean = sum(input)/len(input)
    for a in input:
        if a<mean:
            result.append(a)
    return result

list1=[1,3,5,6,4,10,2,3]
print(below_mean(list1))
