#Given a string. Split it into two equal parts. Swap these parts and return the result.
#If the string has odd characters, the first part should be one character greater than the second part.
#Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.

def split_in_half(str):
    if len(str)%2 == 0:
        part1 = str[0:int(len(str)/2)]
        part2 = str[int(len(str)/2):len(str)]
    else:
        part1 = str[0:int((len(str)+1)/2)]
        part2 = str[int((len(str)+1)/2):len(str)]
    return part2 + part1

test_string1 = "bbbccc"
print(split_in_half(test_string1))
test_string2 = "abbbccc"
print(split_in_half(test_string2))