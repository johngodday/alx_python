def best_score(a_dictionary):

    ls_score = [score for name, score in a_dictionary.items()]
    best_key = ''

    for name, score in a_dictionary.items():
        if score == max(ls_score):
            best_key += name
    return best_key            
