grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

#6 rows, 8 collumns

def print_stuff(stuff):
    image = ''
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            image+= stuff[j][i]
        image += '\n'
    print(image)

print_stuff(grid)




    

