import random

#define a function that will perform the random shuffling of the Password
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)


# create a list to hold the password
passw = []
for codes in range(3):
    # append the ASCII characters to the list passing the range of numbers

    passw.append((chr(random.randint(48, 57))) + chr(random.randint(97, 122))
                 + chr(random.randint(65, 90)) + chr(random.randint(33, 38)))

# call the shuffle function and pass the list to it

print(shuffle(passw))

#below is a different way to do implement code
'''
uppercaseletter1 = chr(random.randint(65,90))
uppercaseletter2 = chr(random.randint(65,90))
lowercaseletter1 = chr(random.randint(97,122))
lowercaseletter2 = chr(random.randint(97,122))
digit1 = chr(random.randint(48,57))
digit2 = chr(random.randint(48,57))
symbol1 = chr(random.randint(33,152))
symbol2 = chr(random.randint(50,140))
password = uppercaseletter1 + uppercaseletter2 + digit1 + digit2 + symbol1 + lowercaseletter2 + lowercaseletter1 + symbol2
password = shuffle(password)
print(password) '''
