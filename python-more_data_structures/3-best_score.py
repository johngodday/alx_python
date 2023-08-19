def best_score(a_dictionary):

    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    ls_score = [score for name, score in a_dictionary.items()]
    best_key = ''
    for name, score in a_dictionary.items():
        if score == max(ls_score):
            best_key += name

    return best_key            