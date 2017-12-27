# EDX-Python
# MITx: 6.00.1x Introduction to Computer Science and Programming Using Python
s='jhjbdhdhfsiiuegayvcdsmnbvsa'
numVowels=0
for char in s:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
print('numVowels is: ' + str(numVowels))
