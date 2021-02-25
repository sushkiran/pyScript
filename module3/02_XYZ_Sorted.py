
'''
Q2. Data of XYZ company is stored in sorted list. Write a program for searching
specific data from that list.
Hint: Use if/elif to deal with conditions.
'''


def q2_xyz_sorted():
    data = ['a1', 'a2', 'a3', 'a4', 'a5']
    to_search = 'a4'
    if to_search in data:
        print('found', to_search)
    else:
        print(to_search, 'cannot be found')


if __name__ == '__main__':
    q2_xyz_sorted()