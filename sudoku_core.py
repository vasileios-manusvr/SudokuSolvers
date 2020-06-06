###
### Propagation function to be used in the recursive sudoku solver
###
def propagate(sudoku_possible_values,k):
    # Find all the numbers that cannot be used per row
    used_row = []
    for i in range(k**2):
        row = []
        for j in range(k**2):
            possibilities = sudoku_possible_values[i][j];
            if len(possibilities) == 1:
                row.append(possibilities[0])

        used_row.append(row)

    # Find all the numbers that cannot be used per col
    used_col = []
    for i in range(k ** 2):
        col = []
        for j in range(k ** 2):
            possibilities = sudoku_possible_values[j][i];
            if len(possibilities) == 1:
                col.append(possibilities[0])

        used_col.append(col)

    # Find all the numbers that cannot be used per square
    used_square = []
    for i1 in range(k):
        for j1 in range(k):
            square = []
            for i2 in range(k):
                for j2 in range(k):
                    i = i1 * k + i2
                    j = j1 * k + j2
                    possibilities = sudoku_possible_values[i][j]
                    if len(possibilities) == 1:
                        square.append(possibilities[0])

            used_square.append(square)

    # Remove all the numbers that cannot be used from the possibilities because exist in row, col and box.
    # Adding a number in the prohibited if a cell has left one value possible.
    # Repeat this refinement until we cannot remove any more values from the possibilities.
    change = True
    while change:
        change = False
        for i in range(k ** 2):
            for j in range(k ** 2):
                to_be_removed = []
                # Remove numbers that cannot be used because they exist in the same row
                if(len(sudoku_possible_values[i][j])) > 1:
                    for possibility in sudoku_possible_values[i][j]:
                        if possibility in used_row[i]:
                            to_be_removed.append(possibility)

                        if possibility in used_col[j]:
                            to_be_removed.append(possibility)

                        if possibility in used_square[(i // k) * k + j // k]:
                            to_be_removed.append(possibility)

                    sudoku_possible_values[i][j] = [x for x in sudoku_possible_values[i][j] if x not in to_be_removed]

                    if(len(sudoku_possible_values[i][j])) == 1:
                        change = True
                        certain_value = sudoku_possible_values[i][j][0]
                        used_row[i].append(certain_value)
                        used_col[j].append(certain_value)
                        used_square[(i // k) * k + j // k].append(certain_value)

    print(sudoku_possible_values)
    print(len(sudoku_possible_values))
    print(len(sudoku_possible_values[0]))
    print(len(sudoku_possible_values[0][0]))
    input()
    return sudoku_possible_values;

###
### Solver that uses SAT encoding
###
def solve_sudoku_SAT(sudoku,k):
    return None;

###
### Solver that uses CSP encoding
###
def solve_sudoku_CSP(sudoku,k):
    return None;

###
### Solver that uses ASP encoding
###
def solve_sudoku_ASP(sudoku,k):
    return None;

###
### Solver that uses ILP encoding
###
def solve_sudoku_ILP(sudoku,k):
    return None;