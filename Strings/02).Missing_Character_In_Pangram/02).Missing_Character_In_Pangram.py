def check_pangram(s):

    c = []
    for i in range(26):
        c.append(False)


    for i in s.lower():

        if i != " ":
            c[ord(i) - ord("a")] = True

    for i in range(len(c)):
        if c[i] == False:
            print(chr(i + ord("a")))



sentence = ("The quick brown fox the little lazy dog")

check_pangram(sentence)
