#!/bin/bash

executable="$1"
input_folder="$2"
output_folder="$3"
actual_output_folder="$4"

# set a flag to print differences if desired
print_diff=false
if [[ "$5" == "--diff" ]]; then
  print_diff=true
fi

for input_file in "$input_folder"/*
do
    # get the base filename of the input file
    base=$(basename "$input_file")

    # construct the expected output filename
    expected_output_file="$output_folder/${base%.*}.out"

    # construct the actual output filename
    actual_output_file="$actual_output_folder/${base%.*}.out"

    # run the executable with the input file and capture its output to the actual output file
    "$executable" < "$input_file" > "$actual_output_file"

    # compare the actual output to the expected output
    if diff -w -q "$actual_output_file" "$expected_output_file" > /dev/null
    then
        echo "PASSED: $base"
    else
        echo "FAILED: $base"
        echo "Expected Output File: $expected_output_file"
        if [ "$print_diff" = true ]; then
          echo "Difference:"
          diff --strip-trailing-cr "$actual_output_file" "$expected_output_file"
        fi
    fi
done
