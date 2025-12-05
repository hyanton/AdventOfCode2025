import itertools
from os import remove


def paper_roll_at_place(matrix, row, col):
    return 1 if matrix[row][col] == '@' else 0

def accessible_paper_roll(matrix: list[list[str]], row: int, col: int) -> bool:
    adjacent_paper_rolls = 0

    changes = [-1, 0, 1]
    for i,j in itertools.product(changes, changes):
        adjacent_paper_rolls += paper_roll_at_place(matrix, row + i, col + j)

    return True if adjacent_paper_rolls < 5 else False

def main():
    with open('data.txt') as f:
        matrix = []
        for line in f.readlines():
            line = list(line.replace('\n', ''))
            line.insert(0, '.')
            line.append('.')
            matrix.append(list(line))

        matrix.insert(0, ['.'] * len(matrix[0]))
        matrix.append(['.'] * len(matrix[0]))

        accessible_paper_roll_total = 0
        removed_paper_rolls = 1
        total_row = len(matrix)
        total_col = len(matrix[0])

        while removed_paper_rolls > 0:
            removed_paper_rolls = 0
            for row in range(1, total_row - 1):
                for col in range(1, total_col - 1):
                    if not paper_roll_at_place(matrix, row, col):
                        continue
                    if accessible_paper_roll(matrix, row, col):
                        matrix[row][col] = '.'
                        removed_paper_rolls += 1

            accessible_paper_roll_total += removed_paper_rolls

        print(f'Solution: {accessible_paper_roll_total}')

if __name__ == '__main__':
    main()