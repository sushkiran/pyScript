'''
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡Y-1.
Example: Suppose the following inputs are given to the program: 3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
'''


def q9_2d_array():

    total_rows = int(input('How many rows: '))
    total_cols = int(input('How many cols: '))

    outer_array = []
    for row_num in range(0, total_rows):

        inner_array = []
        for col_num in range(0, total_cols):
            inner_array.append(row_num * col_num)

        outer_array.append(inner_array)

    print(outer_array)


if __name__ == '__main__':
    q9_2d_array()
