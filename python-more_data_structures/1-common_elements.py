def common_elements(set_1, set_2):
    return set(set_1.intersection(set_2))

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }

print(common_elements(set_1, set_2))