from random import sample

def print_field(field):
    n = len(field)
    for i in range(n):
        print(*field[i])

def generate_field(n, m, count_mines):
    field = [[0 for i in range(m+2)] for j in range(n+2)]
    cells = []
    for i in range(n):
        for j in range(m):
            cells.append((i+1, j+1))
    bombs = sample(cells, k=count_mines)
    print(len(bombs))
    print(bombs)
    for bomb in bombs:
        field[bomb[0]][bomb[1]] = '*'
    return field

def fill_field(field):
    n = len(field)
    m = len(field[0])
    rows = [-1, 0 , 1]
    cols = [-1, 0 , 1]
    for i in range(1, n-1):
        for j in range(1, m-1):
            if field[i][j] != '*':
                for r in rows:
                    for c in cols:
                        if field[i+r][j+c] == '*':
                            field[i][j] += 1
    return field

def check_cell(i, j, field):
    if field[i][j] == '*':
        return '*'





field = generate_field(8, 8, 15)
field = fill_field(field)
print_field(field)