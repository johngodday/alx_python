def square_matrix_simple(matrix=[]):
    emp_ls = []
    for x in matrix:
        rs = [i ** 2 for i in x]
        emp_ls.append(rs)
    return emp_ls