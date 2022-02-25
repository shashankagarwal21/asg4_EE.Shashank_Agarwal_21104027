# a recursive function to make anagrams of enter string
def anagrams(string):
    # if string empty return empty list to avoid infinite loop
    if string == "":
        return [string]
    else:
        ans = []
        for i in anagrams(string[1:]):
            for pos in range(len(i)+1):
                ans.append(i[:pos]+string[0]+i[pos:])
        return ans


# take word as input
input_word = input("Enter the word that George spoke ")

# call function with entered word and print its returned value
print("Possible anagrams that can be made form ", input_word, " are : ", (anagrams(input_word)))
