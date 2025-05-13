from checker import *

def tests_col_check() -> None:
    grid = [
        ['X', 'X', 'X', 'X'],
        [], [], [], [], [], []
    ]
    assert col_check(grid, 'X', 0)

    grid = [
        ['X', 'X', 'X', 'O'],
        [], [], [], [], [], []
    ]
    assert not col_check(grid, 'O', 0)

    grid = [
        ['O', 'O', 'O', 'O'],
        [], [], [], [], [], []
    ]
    assert col_check(grid, 'O', 0)


def tests_row_check() -> None:
    grid = [
        ['X'],
        ['X'],
        ['X'],
        ['X'],
        [], [], []
    ]
    assert row_check(grid, 'X', 0)

    grid = [
        ['X'],
        ['X'],
        ['X'],
        ['X'],
        ['X'],
        [], []
    ]
    assert row_check(grid, 'X', 0)

    grid = [
        ['X'],
        ['X'],
        [],
        ['X'],
        ['X'],
        [], []
    ]
    assert not row_check(grid, 'X', 0)

    grid = [
        ['X', 'X'],
        ['O', 'X'],
        ['O', 'X'],
        ['X', 'X'],
        [], [], []
    ]
    assert row_check(grid, 'X', 1)


def tests_diagonal_check() -> None:
    grid = [
        ['X'],
        ['O', 'X'],
        ['O', 'O', 'X'],
        ['O', 'O', 'O', 'X'],
        [], [], []
    ]
    assert diagonal_check(grid, 'X', 3, 3)

    grid = [
        ['O', 'O', 'O', 'X'],
        ['O', 'O', 'X'],
        ['O', 'X'],
        ['X'],
        [], [], []
    ]
    assert diagonal_check(grid, 'X', 0, 3)

    grid = [
        ['X'],
        ['X'],
        ['X'],
        ['O'],
        [], [], []
    ]
    assert not diagonal_check(grid, 'X', 2, 0)

    grid = [
        ['O'],
        ['X'],
        ['X'],
        ['X'],
        [], [], []
    ]
    assert not diagonal_check(grid, 'X', 3, 0)

    grid = [
        ['X'],
        ['X', 'O'],
        ['X', 'X', 'O'],
        ['X', 'X', 'X', 'O'],
        [], [], []
    ]
    assert not diagonal_check(grid, 'O', 2, 2)

    grid = [
        ['X'],
        ['X', 'X'],
        ['O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        [], [], []
    ]
    assert diagonal_check(grid, 'X', 2, 2)

def main() -> None:
    # Example grid for testing
#          row  0    1    2    3    4    5    6
# col = 0     ['X'],
# col = 1     ['X', 'X'],
# col = 2     ['O', 'O', 'X'],
# col = 3     ['X', 'X', 'O', 'X'],
# col = 4,    [],
# col = 5     [],
# col = 6     []


    grid = [['X', '', '', '', '', ''], []]
    assert not check(grid, 'X', 0)

    tests_col_check()
    tests_row_check()
    tests_diagonal_check()
    print("All tests passed.")

if __name__ == '__main__':
    main()
