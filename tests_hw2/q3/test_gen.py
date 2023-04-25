
def is_alive(matrix):
    # Count the number of live neighbors for the center cell
    live_neighbors = sum(
        [matrix[i][j] for i in range(3) for j in range(3) if (i, j) != (1, 1)]
    )

    # Check the rules of Conway's Game of Life
    if matrix[1][1]:  # Center cell is alive
        if live_neighbors < 2 or live_neighbors > 3:
            return False  # Center cell dies
        else:
            return True  # Center cell survives
    else:  # Center cell is dead
        if live_neighbors == 3:
            return True  # Center cell is born
        else:
            return False  # Center cell remains dead


# Generate all possible 3x3 matrices with boolean values
possibilities = [
    [(a, b, c), (d, e, f), (g, h, i)]
    for a in [True, False]
    for b in [True, False]
    for c in [True, False]
    for d in [True, False]
    for e in [True, False]
    for f in [True, False]
    for g in [True, False]
    for h in [True, False]
    for i in [True, False]
]
def in_gen():
    f=open("test_q3.in", 'w')
    # Iterate through all matrices and call the is_alive function
    for i, matrix in enumerate(possibilities):
        result = is_alive(matrix)
        f.write(f"val test_{i+1} = if {result} = is_alive {matrix[0]} {matrix[1]} {matrix[2]} then \"Passed\" else \"Failed\";\n".replace("False", "empty").replace(
                "True", "alive"
            ).replace("[", "").replace("]", ""))
    f.close()

def exp_gen():   
    f=open("test_q3.expected", 'w')
    begining = """Standard ML of New Jersey (64-bit) v110.99.2 [built: Sun Mar 20 20:10:23 2022]
[opening hw2_q3.sml]
datatype cell = alive | empty
val is_alive = fn :
  cell * cell * cell -> cell * cell * cell -> cell * cell * cell -> cell
- """
    f.write(begining)
    # Iterate through all matrices and call the is_alive function
    for i, matrix in enumerate(possibilities):
        result = is_alive(matrix)
        f.write(f"val test_{i+1} = \"Passed\" : string\n")
    f.write("- \n")
    f.close()


in_gen()
exp_gen()