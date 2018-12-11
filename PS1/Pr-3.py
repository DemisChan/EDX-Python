#Assume s is a string of lower case characters.
#Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = #'azcbobobegghakl', then your program should print
#Longest substring in alphabetical order is: beggh
#In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
#Longest substring in alphabetical order is: abc
#Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest #that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your #head.

x = 'abcdefghijklmnopqrstuvwxyz'


current_string = ''
count=0
longest_string = ''
longest_string2 = ''
for p in range(len(s)-1):

    if x.index(s[p+1])-x.index(s[p]) < 0 and count == 0:
       longest_string = s[count]
       p +=1
    elif x.index(s[p+1])-x.index(s[p]) < 0:
       current_string = ''
            
    elif x.index(s[p+1])-x.index(s[p]) >= 0:
       current_string += s[p]
       count += 1
       if len (longest_string) < len (current_string + s[p+1]):
           longest_string = current_string + s[p+1]
           

print('Longest substring in alphabetical order is:', longest_string)
