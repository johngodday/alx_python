def multiple_returns(sentence):
    len_of_string = len(sentence)
    if len(sentence) == 0:
        first_char = None
    else:
        first_char = sentence[0]
    return len_of_string, first_char