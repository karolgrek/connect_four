Grid = list[list[str]]

WIN_LENGTH = 4

def check(grid, player, column):
    index_added = len(grid[column]) - 1
    return (
        col_check(grid, player, column) or
        row_check(grid, player, index_added) or
        diagonal_check(grid, player, column, index_added)
    )

def col_check(grid, player, column):
    columnfour = 0
    for value in grid[column]:
        if value == player:
            columnfour += 1
            if columnfour == WIN_LENGTH:
                return True
        else:
            columnfour = 0
    return False

def row_check(grid, player, index_added):
    rowfour = 0
    for col in grid:
        if len(col) > index_added and col[index_added] == player:
            rowfour += 1
            if rowfour == WIN_LENGTH:
                return True
        else:
            rowfour = 0
    return False

def diagonal_check(grid, player, column, index_added):
    return (
        diagonal_down_check(grid, player, column, index_added) or
        diagonal_up_check(grid, player, column, index_added)
    )

def diagonal_down_check(grid, player, column, index_added):
    fourdiag = 0
    for i in range(-WIN_LENGTH + 1, WIN_LENGTH):
        col_index = column + i
        row_index = index_added + i
        if 0 <= col_index < len(grid) and 0 <= row_index < len(grid[col_index]):
            if grid[col_index][row_index] == player:
                fourdiag += 1
                if fourdiag == WIN_LENGTH:
                    return True
            else:
                fourdiag = 0
        else:
            fourdiag = 0
    return False

def diagonal_up_check(grid, player, column, index_added):
    fourdiag = 0
    for i in range(-WIN_LENGTH + 1, WIN_LENGTH):
        col_index = column + i
        row_index = index_added - i
        if 0 <= col_index < len(grid) and 0 <= row_index < len(grid[col_index]):
            if grid[col_index][row_index] == player:
                fourdiag += 1
                if fourdiag == WIN_LENGTH:
                    return True
            else:
                fourdiag = 0
        else:
            fourdiag = 0
    return False