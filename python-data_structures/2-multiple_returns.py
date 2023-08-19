def multiple_returns(sentence):
    len_of_string = len(sentence)
    first_char = sentence[0]
    print("Length: {:d} - First character: {}".format(len_of_string, first_char))
    return len_of_string, first_char


print(multiple_returns('I am John By Name'))
