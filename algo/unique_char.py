#Given a string, determine if it consists of all unique characters.
#For example, the string 'abcde' has all unique characters and should return True.
#The string 'aabcde' contains duplicate characters and should return False.

def unique_char(str):
    count={}
    for ch in str:
        if ch in count.keys():
            return False
        else:
            count[ch]=1
    return True



string1 = "abcdef"
print(unique_char(string1))
string2 = "abccdef"
print(unique_char(string2))


