def get_matrix(n, m, value):
    matrix = []
    for q in range(n):
        my_list = []
        matrix.append(my_list)
        for col in range(m):
            my_list.append(value)
    return matrix

print(get_matrix(2, 2, 10))
