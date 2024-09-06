import os
import argparse

def rename_folders_in_directory(directory_path, replace_from, replace_to):
    # Traverse all folders and subfolders in the directory
    for root, dirs, _ in os.walk(directory_path, topdown=False):
        for folder_name in dirs:
            # Create the full path to the current folder
            old_folder_path = os.path.join(root, folder_name)
            
            # Replace specified string in the folder name
            new_folder_name = folder_name.replace(replace_from, replace_to)
            new_folder_path = os.path.join(root, new_folder_name)
            
            # Rename the folder
            if old_folder_path != new_folder_path:
                os.rename(old_folder_path, new_folder_path)
                print(f'Renamed folder: {old_folder_path} -> {new_folder_path}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rename folders in a directory by replacing a specified string with another string.")
    parser.add_argument('-dir', type=str, required=True, help="Path to the directory containing the folders to rename")
    parser.add_argument('-replace_from', type=str, required=True, help="String to be replaced in the folder names")
    parser.add_argument('-replace_to', type=str, required=True, help="String to replace with in the folder names")

    args = parser.parse_args()

    # rename_folders_in_directory("D:/MS/Dissertation/Output_results/", "&", "and")
