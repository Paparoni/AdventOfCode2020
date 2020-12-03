import re
# Remove the line breaks from the end of each line and separate each line into its own array element
def breaks(s):
    return re.sub(r"(?<=[a-z])\r?\n","", s)

passwords = list(map(breaks, open('data.txt').readlines()))

# Function that only reads the numbers in a string and returns the numbers as integers in a list
def readNum(s):
    def isDig(n):
        return int(re.sub("[^0-9]", "", n))
    ss = s.split(':')[0].split('-')    
    return list(map(isDig, ss))

# Function that tests if the string is a valid password

def valid(s):
    def isAlph(a):
        return a.isalpha()
    letter = list(filter(isAlph, list(s.split(':')[0].replace(" ", ""))))[0] # get the letter we're counting
    low = readNum(s)[0]
    high = readNum(s)[1]
    password = s.split(':')[1].replace(" ", "") # get just the password
    numOf = password.count(letter)
    return numOf >= low and numOf <= high

# Now we just count how many valid passwords we have
solution = list(filter(valid, passwords))
print(len(solution))
