def write_pascal_triangle_to_file(n, filename):
    # initialize the first row with 1
    row = [1]

    # open the file for writing
    with open(filename, "w", encoding='utf-8') as file:
        # write the first n rows of the Pascal Triangle to the file
        for i in range(n):
            # write the current row to the file
            file.write(" ".join(str(x) for x in row))
            file.writelines("\n")

            # generate the next row
            next_row = [1]
            for j in range(1, len(row)):
                next_row.append(row[j - 1] + row[j])
            next_row.append(1)

            # update the current row
            row = next_row


def write_test_number_to_file(n, filename):
    # open the file for writing
    with open(filename, "w") as file:
        file.write(str(n))


def main():
    for n in range(16):
        filename = f"ExpectedFiles\\test{n}.out"
        write_pascal_triangle_to_file(n, filename)

        # filename = f"InputFiles\\test{n}.in"
        # write_test_number_to_file(n, filename)

        print(f"Wrote Pascal Triangle of {n} rows to {filename}")


if __name__ == "__main__":
    main()
