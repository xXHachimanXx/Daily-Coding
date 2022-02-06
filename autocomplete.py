"""
This problem was asked by Twitter.

Implement an autocomplete system. That is, given 
a query string s and a set of all possible query 
strings, return all strings in the set that have 
s as a prefix.

For example, given the query string de and the set 
of strings [dog, deer, deal], return [deer, deal].
"""

def autocomplete(string_set, str_input):
    output_string_set = []

    for str in string_set: # O(n)
        if str[0:len(str_input)] == str_input:
            output_string_set.append(str)

    return output_string_set


print(autocomplete(["dog", "deer", "deal"], "de"))

"""
Time complexity = O(n)
Space complexity = O(n) -> just one array with n words
"""