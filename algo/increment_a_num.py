#Write a program that takes as input an array of digits encoding a nonnegative decimal
#integer D and updates the array to represent the integer D + 1.
#For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].
#O(n)
def increment_one(input):
    s=""
    for i in input:
        s += str(i)
    num = int(s)
    newnum = num+1
    result = []
    for i in str(newnum):
        result.append(int(i))
    return result

input1=[1,2,9]
print(increment_one(input1))
input2=[9,9]
print(increment_one(input2))
