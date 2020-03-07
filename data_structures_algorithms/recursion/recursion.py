# https://see.stanford.edu/materials/icspacs106b/Lecture08.pdf


def isPalindrome(s: str):
    if len(s) <= 1:
        return True
    return s[0] == s[len(s)-1] and isPalindrome(s[1:len(s)-1])

data =   "go hang a salami im a lasagna hog"
# data =  "was it a car or a cat i saw"
data = data.replace(" ", "")
print("Is palindrome: ", isPalindrome(data))
