##### Write a function that takes the name of a text file as a parameter. Print out the 3-letter words that start with “b”

def namefunction ( parameter_file ):
    fd = open (parameter_file)
    for line in fd:
        words = line.split() # I have all the words
        for word in words:
            if word [0] == "b" and len(word)==3:
                print (word)

##### Write a recursive function (function that calls itself) that computes a to the power b (a and b are parameters given to the function)

## (1)
def recursive (a,b):
    if b==0:
        return 1
    return a*recursive(a, b-1)
## (2)
def recursive (a,b):
    result = 1
    for i in range(b):
        result = result * a
    return result

##### Write a function that takes an integer as a parameter and returns a list of all the divisors of that number:	Ex: 47 -> [1,4,7], 28 -> [1,2,4,7,14,28]
def divisor (n):
    numbers = [] # create a list
    for x in range(1,n+1): # in order to include n
        if n%x == 0:
            numbers.append(x) # add to the end of the list "numbers"
    return numbers

##### Write a function that forces the user to enter a multiple of 6 number. Use try, except to catch invalid inputs. Return that number
def function():
    try:

        if(int(input("tell me a number")) % 6 == 0):
            print("thanks")
            return True
        else:
            print("try a different number")
            return False
    except:
        print("That is not a number")
        return False

while True:

    if function() == True:
        break
    else:
        continue