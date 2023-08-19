def square_matrix_simple(matrix=[]):
    emp_ls = []
    for x in ls:
        rs = [i ** 2 for i in x]
        emp_ls.append(rs)
    return emp_ls

ls = [[2,3,4], [5,6,8]]
    
print(square_matrix_simple(ls))