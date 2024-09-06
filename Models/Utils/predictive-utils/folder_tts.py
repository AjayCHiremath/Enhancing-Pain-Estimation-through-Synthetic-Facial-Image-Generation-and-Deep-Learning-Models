import os
import shutil
import glob

def move_files_based_on_pain_value(directory):
    # Get all .jpg and .png files in the directory and its subdirectories
    all_files = glob.glob(os.path.join(directory, '**', '*.jpg'), recursive=True) + \
                glob.glob(os.path.join(directory, '**', '*.png'), recursive=True)
    
    # Loop through all the files
    for file in all_files:
        # Normalize the file path to handle different OS path separators
        file = file.replace('\\', '/')
        
        # Extract the pain level from the filename
        try:
            pain_level = file.split('/')[-1].split('.')[0].split('_')[-1]
            # Ensure pain_level is a digit
            if not pain_level.isdigit():
                print(f"Skipping {file} - pain level is not a digit.")
                continue
        except IndexError:
            print(f"Skipping {file} - unable to extract pain level.")
            continue

        # Create the target directory if it doesn't exist
        target_dir = os.path.join(directory, f'pain_{pain_level}')
        os.makedirs(target_dir, exist_ok=True)
        
        # Move the file to the target directory
        dest_file = os.path.join(target_dir, os.path.basename(file))
        shutil.move(file, dest_file)
        print(f"Moved {file} to {target_dir}")

if __name__ == "__main__":
    move_files_based_on_pain_value("C:/Users/psxah20/Desktop/Dissertation/Predictive_Images_Real_Only/Train")
    move_files_based_on_pain_value("C:/Users/psxah20/Desktop/Dissertation/Predictive_Images_Real_Only/Test")
    print("Moved all files based on pain levels to corresponding folders.")
