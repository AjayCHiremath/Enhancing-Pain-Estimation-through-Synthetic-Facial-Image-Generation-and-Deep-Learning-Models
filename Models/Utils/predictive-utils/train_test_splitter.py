import os
import glob
import shutil
import argparse
from sklearn.model_selection import train_test_split

def get_all_files(directory):
    """Retrieve all image files from the directory, considering both jpg and png formats."""
    return (glob.glob(os.path.join(directory, '**', '*.jpg'), recursive=True) + 
            glob.glob(os.path.join(directory, '**', '*.png'), recursive=True))

def create_train_test_split(all_files):
    """Split the files into train and test datasets."""
    y_rand = [0 for _ in range(len(all_files))]
    return train_test_split(all_files, y_rand, test_size=0.1)

def copy_files_to_directory(file_list, new_dir_name):
    """Copy files to a new directory, placing them directly under the new directory."""
    for old_file in file_list:
        filename = os.path.basename(old_file)
        new_file = os.path.join(new_dir_name, filename)
        os.makedirs(new_dir_name, exist_ok=True)
        shutil.copy(old_file, new_file)

def train_test_splitter(directory):
    all_files = get_all_files(directory)
    all_files = [files.replace("\\", "/") for files in all_files]

    X_train, X_test, _, _ = create_train_test_split(all_files)

    base_dir = "/".join(directory.split("/")[:-1]).replace('Pre-pred','')

    # Define paths for "Train" and "Test" directories
    train_dir_name = os.path.join(base_dir, "Predictive_Images_Real_Only", "Train")
    test_dir_name = os.path.join(base_dir, "Predictive_Images_Real_Only", "Test")

    # Copy files to Train directory
    copy_files_to_directory(X_train, train_dir_name)

    # Copy files to Test directory
    copy_files_to_directory(X_test, test_dir_name)

if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description="Replace folders in a directory by replacing a specified string with another string.")
    # parser.add_argument('-dir', type=str, required=True, help="Path to the directory containing the folders to replace")
    # args = parser.parse_args()
    # train_test_splitter(args.dir)
    # print("Saved all files under", args.dir)

    train_test_splitter("C:/Users/psxah20/Desktop/Dissertation/Pre-pred/")
    print("Saved all files under C:/Users/psxah20/Desktop/Dissertation/Predictive_Images_Real_Only")