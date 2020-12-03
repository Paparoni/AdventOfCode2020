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

## PART TWO

def valid(s):
    def isAlph(a):
        return a.isalpha()
    letter = list(filter(isAlph, list(s.split(':')[0].replace(" ", ""))))[0] # get the letter we're counting
    password = s.split(':')[1].replace(" ", "") # get just the password
    valid_index_a = readNum(s)[0] 
    valid_index_b = readNum(s)[1]
    indexes = [i for i, char in enumerate(password) if char == letter] # find each occurence of the letter in the password
    valid_indexes = [n for n in indexes if n + 1 == valid_index_a or n + 1 == valid_index_b] # find each occurrence of a valid index
    
    # No need to do complex xor syntax if we have a list of valid indexes :3
    if len(valid_indexes) == 1:
        return True
    else:
        return False

solution = list(filter(valid, passwords))
print(len(solution))
