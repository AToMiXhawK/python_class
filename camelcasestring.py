""Shubham wrote a sequence of words. The words are written using the rules given below:

The sequence is concatenation of one or more words consisting of English letters.
All letters in the first word are lowercase.
For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.
You need to find the number of words in the string.""

t=int(input())
for x in range(t):
    s=input()
    c=1
    for i in range(1,len(s)):
        if s[i].isupper():
            c=c+1
    print(c)
