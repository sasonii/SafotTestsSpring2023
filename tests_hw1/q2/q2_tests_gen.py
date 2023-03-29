import random
import string
import os


def generate_strings(n):
    """
    Generates two random strings of length n consisting of lowercase letters.
    """
    s1 = "".join(random.choices(string.ascii_lowercase, k=n))
    s2 = "".join(random.choices(string.ascii_lowercase, k=n))
    return s1, s2


def print_histogram(s):
    """
    Prints a histogram of the characters in the string s.
    """
    # Create a dictionary to count the occurrences of each character
    count = {}
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    # Print the histogram
    for char in sorted(count.keys()):
        print(char, count[char])


def write_test_number_to_file(n, filename):
    # open the file for writing
    with open(filename, "w") as file:
        file.write(str(n))


def main():
    print(os.getcwd())
    for n in range(101):
        filename_out = fr"ExpectedFiles\test{n}.out"
        filename_in = fr"InputFiles\test{n}.in"
        s1, s2 = generate_strings(n)
        common = set(s1).intersection(set(s2))
        with open(filename_in, "w") as f:
            f.write(s1)
            f.write("\n")
            f.write(s2)

        with open(filename_out, "w") as f:
            # Print whether there are common characters
            if len(common) == 0:
                f.write("TRUE\n")
            else:
                f.write("FALSE\n")

            """
            Prints a histogram of the characters in the string s.
            """
            # Create a dictionary to count the occurrences of each character
            count = {}
            for char in s1 + s2:
                if char in count:
                    count[char] += 1
                else:
                    count[char] = 1

            # Print the histogram
            for char in sorted(count.keys()):
                f.write(char + " " + str(count[char]) + "\n")

        # filename = f"InputFiles\\test{n}.in"
        # write_test_number_to_file(n, filename)

        print(f"Wrote Pascal Triangle of {n} rows to {filename_out}")


if __name__ == "__main__":
    main()
