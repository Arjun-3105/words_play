'''find palindromes from the list of words given in a text file'''
import sys
def load(file):
    '''load the dict file as a list'''
    try:
        with open('D:\Coding\Python_Projects\chapter 2\words.txt','r') as f:
            loaded_text = f.read().strip().split('\n')
            loaded_text = [x.lower() for x in loaded_text]
            return loaded_text
    except IOError as e:
        print ("Error opening the file ")
    sys.exit(1)
def ispal(s):
    ''''check ifa given word is palindrome or no'''
    s_reversed = s[::-1]
    if(s == s_reversed):
        return True
    return False
palindromes = []
words_list = load("words.txt")
for x in words_list:
    if ispal(x):
        palindromes.append(x)

print(palindromes)