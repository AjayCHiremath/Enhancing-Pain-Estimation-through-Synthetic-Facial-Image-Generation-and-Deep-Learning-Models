import os
import re
from glob import glob
from pathlib import Path
import argparse

def sorted_dict(filenames, old_names):
    """
    Sorts the filenames based on the numeric part extracted from each filename and appends 
    the pain score to each filename.
    
    Args:
    filenames (list of str): List of filenames to be sorted.
    old_names (list of str): List of old filenames containing pain scores.

    Returns:
    list of str: List of sorted and renamed filenames.
    """
    store_pain = {}

    for old_name in old_names:
        name = "".join(old_name.split('/')[-1].split("\\")[-1].split("_")[-1].split(".")[0])
        key = old_name.split('/')[-1].split("\\")[-1].split("_")[-2]
        if key not in store_pain:
            store_pain[key] = [name]
        else:
            store_pain[key].append(name)

    # Initialize a list to hold the sorted results
    sorted_filenames = [None] * len(filenames)
    counter = {}

    # Create a list of tuples with (index, filename, pain_score)
    indexed_files = []
    for filename in filenames:
        # Extract the numeric part from the filename
        numeric_part = ''.join([char for char in filename if char.isdigit()])
        index = int(numeric_part) - 1
        # Append a tuple of (index, filename, pain_score) to the list
        indexed_files.append((index, filename, store_pain[filename]))
        counter[filename] = 0

    # Sort the list of tuples by the extracted index
    indexed_files.sort()

    # Populate the sorted_filenames list with sorted filenames
    for new_index, (index, filename, painscore) in enumerate(indexed_files):
        # Construct the new filename with the pain score suffix
        new_filename = f"{filename}_{painscore[counter[filename]]}.jpg"
        sorted_filenames[new_index] = new_filename
        counter[filename] += 1
    
    return sorted_filenames

def rename_files(old_file_directory):
    """
    Renames files in the given directory by adding an index and suffix derived from pain scores.
    
    Args:
    old_file_directory (str): Path to the directory containing the files to be renamed.
    """
    # Get all filenames in the directory recursively
    old_filenames = glob(os.path.join(old_file_directory, '**', '*.*'), recursive=True)
    
    # Dictionary to hold subjects and their associated filenames
    subjects = {}
    
    # Populate the subjects dictionary with filenames grouped by subject identifier
    for filename in old_filenames:
        subject_identifier = filename.split('/')[-1].split('.')[0].split("_")[-2]
        subject_key = subject_identifier[:2]
        if subject_key not in subjects:
            subjects[subject_key] = [subject_identifier]
        else:
            subjects[subject_key].append(subject_identifier)
    
    # Sort and rename files for each subject
    for key, filenames in subjects.items():
        subjects[key] = sorted_dict(filenames, old_filenames)

    # Variable to keep track of the index to add to the filenames
    index_offset = 0

    # Rename files by adding an index and suffix
    for subject_key, renamed_filenames in subjects.items():
        for i, renamed_filename in enumerate(renamed_filenames):
            # Extract numeric part from the original filename
            sub_filename = renamed_filename.split('_')[0]
            match = re.search(r'\d+\.?\d*', sub_filename)
            index = int(match.group()) + index_offset - 1
            subjects[subject_key][i] = f"id{index}_{renamed_filename.split('_')[-1]}"
            
            file_path = old_file_directory + "\\DPD_1_" + renamed_filename

            # Determine the target path based on the pain score suffix
            pain_score_suffix = renamed_filename.split('_')[-1]
            if 'p1' in pain_score_suffix:
                trgt = Path(f"{old_file_directory}\\id{index}_class2.jpg")
            elif 'p2' in pain_score_suffix:
                trgt = Path(f"{old_file_directory}\\id{index}_class3.jpg")
            elif 'p3' in pain_score_suffix:
                trgt = Path(f"{old_file_directory}\\id{index}_class4.jpg")
            elif 'p4' in pain_score_suffix:
                trgt = Path(f"{old_file_directory}\\id{index}_class5.jpg")
            elif 'p5' in pain_score_suffix:
                trgt = Path(f"{old_file_directory}\\id{index}_class6.jpg")
            elif 'p6' in pain_score_suffix:
                trgt = Path(f"{old_file_directory}\\id{index}_class7.jpg")

            # Rename the file if it exists
            if os.path.isfile(file_path):
                Path(file_path).replace(trgt)
            else:
                print(file_path, "doesn't exist.")

            print(f"subjects[{subject_key}][{i}] changed from {renamed_filename} to {trgt.name}")
            
        index_offset = index + 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some files.")
    parser.add_argument('-oldfile', type=str, required=True, help="Path to the old file directory")

    args = parser.parse_args()
    rename_files(args.oldfile)