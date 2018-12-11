#Assume s is a string of lower case characters.
#Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print
#Number of times bob occurs is: 2

count=0
for p in range(len(s)):
    if p+1==len(s) or p+2==len(s):
        break
    elif s[p] == 'b' and s[p+1]=='o' and s[p+2]=='b':
        count+=1
print('Number of times bob occurs is:'+ str(count))
