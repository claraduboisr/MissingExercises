##### Determine the maximum out of 4 given numbers

x = float (input ("Give me the first number: "))
y = float (input ("Give me the second number: "))
z = float (input ("Give me the third number: "))
w = float (input ("Give me the fourth number: "))


print("The highest value number is", max(x, y, z, w))

##### Determine the average of 4 random numbers

import random # Create random number
y = 0
for abc in range (4): # Repeat this code for times
    z = random.randint (1, 100) # From 1 to 100
    y = y + z # Each time you sum z the previous result (y)
print (y/4)

##### Determine the average of n random numbers

n = 100

import random
def myaverage (n):
    y = 0
    for abc in range(n):
        z = random.randint (1,100)
        y = y + z # y +=z
print(y/n)
myaverage (5000) # you can choose the range

### Given 3 number, determine what kind of triangle you can form with them

x = float (input ("Give me the first number: "))
y = float (input ("Give me the second number: "))
z = float (input ("Give me the third number: "))

def check_triangle (x,y,z):
    if x>=y and x>=z:
        maximum = x
        small1 = y
        small2 = z
    elif y>=x and y>=z:
        maximum = y
        small1 = z
        small2 = x
    else:
        maximum = z
        small1 = x
        small2 = y

check_triangle (x,y,z)
if x==y and x==z:
    print ("equilateral")
elif x==y or y==z or x==z:
    print ("isosceles")
else:
    print ("scalene")


### Print the N-th “Fibonacci” number (function inside function)

def fibonacci (n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
print (fibonacci(7))

##### Determine if all characters in a string are doubled: ggbbyy99aappWW

word = input("What is the word you are thinking of?")
if word[::2] == word[1::2]:
    print("All the letters are doubled")
else:
    print("Not all the letters are doubled")

##### Determine the longest word in a text file

punctuation = ",.;:!?"

fd = open ("trex.txt", "r")

longest = ""
size = 0


for line in fd:
    # line = line.decode()
    for c in punctuation:
        line = line.replace(c, "")
    words = line.split()
    for word in words:
        if len(word) > size:
            size = len (word)
            longest = word
print ("longest word is: ", longest)
fd.close()

##### Sorting a list

a = [5,8,3,2,9,7]

stop = False
while not stop:
    stop = True
    for i in range (len(a)-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            stop = False
print (a)

##### Encode a string. Take a random “seed” number between 1 and 10.
##### Add that number to each letter and determine the encoded letter.
##### If seed = 3, ana -> dqd

import random
seed = random.randint(1, 10)
alphabet = "abcdefghijklmnopqrstuvwxyz"
text = input("What is the text to encode?")
text = text.lower()
encoded = ""
for c in text:
    pos = alphabet.find(c)
    if pos == -1:
        encoded = encoded + c
        continue
    new_pos = (pos + seed) % 26  # circular addition to account for going over the end of the alphabet
    encoded = encoded + alphabet[new_pos]
print("The encoded text is:", encoded)


