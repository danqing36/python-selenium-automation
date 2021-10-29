#Count odd and even digits of the whole number

#O(n)

def count_odd_and_even(number):
    temp = str(number)
    count_odd =0;
    count_even = 0;
    for ch in temp:
       num = int(ch)
       if(num%2==0):
           count_even +=1
       else:
           count_odd +=1
    return [count_even, count_odd]

def odd_digits(number):
    odd_list = []
    for ch in str(number):
        if (int(ch)%2 !=0):
            odd_list.append(int(ch))
    return odd_list

def even_digits(number):
    even_list = []
    for ch in str(number):
        if (int(ch)%2 ==0):
            even_list.append(int(ch))
    return even_list

n = int(input('Enter a number:'))
result = count_odd_and_even(n)
result_odd_digits = odd_digits(n)
result_even_digits = even_digits(n)
print(f'count of odd digits is {result[1]}')
print(result_odd_digits)
print(f'count of even digits is {result[0]}')
print(result_even_digits)