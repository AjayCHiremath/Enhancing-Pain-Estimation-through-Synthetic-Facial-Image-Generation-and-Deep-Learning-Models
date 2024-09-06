import os, re
from glob import glob
from pathlib import Path
import argparse

def sorted_dict(filenames):
    """
    Sorts the filenames based on the numeric part extracted from each filename.
    
    Args:
    filenames (list of str): List of filenames to be sorted.

    Returns:
    list of str: List of sorted filenames.
    """
    # Initialize a list to hold the sorted results
    sorted_filenames = [None] * len(filenames)
    
    # Create a list of tuples with (index, filename)
    indexed_files = []
    for filename in filenames:
        # Extract the numeric part from the filename
        numeric_part = ''.join([char for char in filename if char.isdigit()])
        index = int(numeric_part) - 1
        # Append a tuple of (index, filename) to the list
        indexed_files.append((index, filename))

    # Sort the list of tuples by the extracted index
    indexed_files.sort()

    # Populate the sorted_filenames list with sorted filenames
    for new_index, (index, filename) in enumerate(indexed_files):
        sorted_filenames[new_index] = filename
    return sorted_filenames

def rename_files(old_file_directory):
    """
    Renames files in the given directory by adding an index.

    Args:
    old_file_directory (str): Path to the directory containing the files to be renamed.
    """
    # Get all filenames in the directory recursively
    old_filenames = glob(os.path.join(old_file_directory, '**', '*.*'), recursive=True)
    
    # Dictionary to hold subjects and their associated filenames
    subjects = {}
    
    # Populate the subjects dictionary with filenames grouped by subject identifier
    for filename in old_filenames:
        subject_identifier = filename.split('/')[-1].split("\\")[-1].split("_")[-1].split(".")[0]
        subject_key = subject_identifier[:2]
        if subject_key not in subjects:
            subjects[subject_key] = [subject_identifier]
        else:
            subjects[subject_key].append(subject_identifier)
    
    # Sort and rename files for each subject
    for key, filenames in subjects.items():
        subjects[key] = sorted_dict(filenames)

    # Variable to keep track of the index to add to the filenames
    index_offset = 0

    # Rename files by adding an index
    for subject_key, renamed_filenames in subjects.items():
        for i, renamed_filename in enumerate(renamed_filenames):
            # Extract numeric part from the original filename
            sub_filename = renamed_filename.split('_')[0]
            match = re.search(r'\d+\.?\d*', sub_filename)
            index = int(match.group()) + index_offset - 1
            subjects[subject_key][i] = f"id{index}_{renamed_filename.split('_')[-1]}"
            
            file_path = old_file_directory + "\\DPD_1_" + renamed_filename + ".jpg"

            # Determine the target path
            trgt = Path(f"{old_file_directory}\\id{index}_class1.jpg")

            # Rename the file if it exists
            if os.path.isfile(file_path):
                Path(file_path).replace(trgt)
            else:
                print(file_path, "doesn't exist.")

            print(f"subjects[{subject_key}][{i}] changed from {renamed_filename} to {trgt.name}")
            
        index_offset = index + 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rename files based on specific rules.")
    parser.add_argument('-oldfile', type=str, required=True, help="Path to the old file directory")

    args = parser.parse_args()

    rename_files(args.oldfile)
