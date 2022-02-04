def autocomplete(string_set, str_input):
    output_string_set = []

    for str in string_set:
        if str[0:len(str_input)] == str_input:
            output_string_set.append(str)

    return output_string_set


print(autocomplete(["dog", "deer", "deal"], "de"))