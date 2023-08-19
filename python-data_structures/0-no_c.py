def no_c(my_string):
    emp_string = ''
    for var in my_string:
        if var == 'c' or var == 'C':
            continue
        else:
            emp_string += var
    return emp_string

