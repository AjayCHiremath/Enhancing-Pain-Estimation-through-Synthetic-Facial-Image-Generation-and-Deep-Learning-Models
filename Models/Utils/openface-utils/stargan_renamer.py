import os
import glob
import pandas as pd

def rename_files(directory, excel_dir):
    # Get all jpg and png files in the directory
    files = (glob.glob(os.path.join(directory, '**', '*.jpg'), recursive=True) + 
             glob.glob(os.path.join(directory, '**', '*.png'), recursive=True))
    
    # Sort files to ensure consistent numbering
    files.sort()
    # excel_sheet = pd.read_excel(io=excel_dir, sheet_name='Sheet1', index_col='subjects_name')

    # Loop over files and rename them
    for i, file_path in enumerate(files):
        file_path = file_path.replace("\\", "/")
        file_name = file_path.split('/')[-1].split('.')[0]
        file_name = file_name.replace(file_name, f'stargan2_id_{i}_')
        # if file_name in excel_sheet.index:

        # Generate new filename as stargan_2_facs_01.png, stargan_2_facs_02.png, etc.
        # new_file_name = f"face_{i+1}_{excel_sheet.loc[file_name, 'PSPI_Score']}.png"

        new_file_name = f"{file_name}.png"
        
        # Construct new file path
        new_file_path = os.path.join(os.path.dirname(file_path), new_file_name)
        
        # Rename the file (this also deletes the old file)
        os.rename(file_path, new_file_path)
        print(f"Renamed {file_path} to {new_file_path}")

if __name__ == "__main__":
    directory = "C:/Users/psxah20/Desktop/Dissertation/Stargan-2/"
    excel_dir = "C:/Users/psxah20/Desktop/Dissertation/openfacs-stargan2/pspi_predicted.xlsx"

    # Rename files in the directory
    rename_files(directory, excel_dir)
