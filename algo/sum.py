#Compute the sum of digits in all numbers from 1 to n

#O(n)

def sum_of_numbers(n):
    sum = 0
    for i in range (1,n+1):
        sum +=i
    return sum

number = int(input('Input a number:'))
result = sum_of_numbers(number)
print(f'sum of digits from 1 to {number} is:{result}')
