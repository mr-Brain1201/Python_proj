class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        for row in self.matrix:
            for x in row:
                print(f"{x:<8}", end="")
            print()
        return ''

    def __add__(self, other):
        while True:
            try:
                for i in range(len(self.matrix)):
                    for j in range(len(self.matrix[0])):
                        self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
            except IndexError:
                print('Либо удалите последнюю матрицу, либо заполните отсутствующие значения нулями!')
            return Matrix(self.matrix)


mx_1 = Matrix([[4, 67, 8], [45, 23, 8], [5, 6, 5]])
mx_2 = Matrix([[2, 5, 45], [4, 7, 45], [23, 65, 76]])
mx_3 = Matrix([[43, 4, 6], [23, 6, 2], [56, 34, 6]])
print(mx_1)
print(mx_1 + mx_2 + mx_3)
