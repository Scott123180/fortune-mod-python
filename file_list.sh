#!/bin/bash

# Directory path to read files from
directory="./datfiles"

# Check if the directory exists
if [ ! -d "$directory" ]; then
  echo "Directory does not exist."
  exit 1
fi

# Change to the specified directory
cd "$directory" || exit 1

# Array to store file names
files=()

# Read all file names in the directory
while IFS= read -r -d $'\0' file; do
  # Add file name to the array
  files+=("$file")
done < <(find . -type f -print0)

# Concatenate file names into a comma-separated list
comma_separated_list=$(IFS=,; echo "${files[*]}")

# Print the comma-separated list
echo "$comma_separated_list"

