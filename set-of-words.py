"""

This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces), 
return the original sentence in a list. If there is more than one possible 
reconstruction, return any of them. If there is no possible reconstruction, 
then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the 
string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string 
"bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 
'and', 'beyond'].

"""

def set_of_words(str, word_set):
    word = ""
    word_list = []

    for char in str: # O(n)
        word += char
        if word in word_set: # O(1)
            word_list.append(word)
            word = ""

    return word_list # space -> O(n)

assert set_of_words("thequickbrownfox", {'quick', 'brown', 'the', 'fox'}) == ['the', 'quick', 'brown', 'fox']
assert set_of_words("bedbathandbeyond", {'bed', 'bath', 'bedbath', 'and', 'beyond'}) == ['bed', 'bath', 'and', 'beyond']

"""
n = number of char in the input string

Time complexity: O(n) = O(n)
Space complexity: O(n) = O(n) -> word_list
"""