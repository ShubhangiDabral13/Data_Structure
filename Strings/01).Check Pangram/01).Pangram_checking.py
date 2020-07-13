def check_pangram(s):

    c = []
    for i in range(26):
        c.append(False)


    for i in s.lower():

        if not i == " ":

            c[ord(i) - ord("a")] == True


    for i in c:
        if c == False:
            return False

        return True


sentence = ("The quick brown fox jumps over the little lazy dog")

if (check_pangram(sentence)):
    print (sentence)
    print ("is a pangram")
else:
    print (sentence)
    print ("is not a pangram")
