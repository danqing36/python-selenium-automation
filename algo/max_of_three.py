#find max number from 3 values

#O(1)

def max_of_three(a, b, c):
    max = a
    if(b>max):
        max = b
    if(c>max):
        max = c
    return max

number1 = int(input('input a number:'))
number2 = int(input('input another number:'))
number3 = int(input('input the third number:'))
result = max_of_three(number1, number2, number3)
print(f'The max number is {result}')