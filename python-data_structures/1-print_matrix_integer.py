def print_matrix_integer(matrix=[[]]):
    for x in matrix:
          for y in range(len(x)):
            print('{:d}'.format(x[y]), end = "")
            if y < len(x) - 1:
                print(" ", end = "")
    print()


