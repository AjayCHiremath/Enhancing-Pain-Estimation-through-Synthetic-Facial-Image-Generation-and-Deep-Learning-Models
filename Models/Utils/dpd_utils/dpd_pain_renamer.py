import os, glob, shutil
import pandas as pd

def dpd_files_replace(directory):
    csv_file = "C:/Users/psxah20/Desktop/Dissertation/Final_cropped_pictures/DelawarePainDatabase_StimulusCharacterization_forOSF.csv"
    facs_dpd = pd.read_csv(filepath_or_buffer=csv_file)
    
    # Extracting the 'OpenFace_PainIndex' as a Series
    pain_scores = facs_dpd.set_index('Target')['OpenFace_PainIndex']

    # Collecting all the .JPG and .PNG files
    dpd_files = (glob.glob(os.path.join(directory, '**', '*.JPG'), recursive=True) + 
                 glob.glob(os.path.join(directory, '**', '*.PNG'), recursive=True))
    
    for file_path in dpd_files:
        file_path = file_path.replace("\\", "/")
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        if 'pain' not in file_name:
            if file_name in pain_scores.index:
                # Extract and clean the pain score
                pain_score = str(pain_scores.loc[file_name])
                
                # Ensure the pain_score is properly formatted and does not include unexpected text or newlines
                pain_score = pain_score.strip().split()[0]  # Taking only the first part, assuming it is the numeric score

                # Construct the new file name
                new_file_name = f"{file_name}_pain_{pain_score}"
                
                # Construct the new file path
                new_file_path = os.path.join(os.path.dirname(file_path), f"{new_file_name}.jpg")
                new_file_path = new_file_path.replace('Final_cropped_pictures/Cropped_Faces/Expression_Images', 'Pre-pred/DPD_FACES')

                # Create the directory if it does not exist
                os.makedirs(os.path.dirname(new_file_path), exist_ok=True)
                
                # Use shutil.copy to copy the file (it will overwrite if the file already exists)
                shutil.copy(file_path, new_file_path)
                print(f"Moved: {file_name} to {new_file_name}")
            else:
                print(f"Unable to process {file_path}")

if __name__ == "__main__":
    directory = "C:/Users/psxah20/Desktop/Dissertation/Final_cropped_pictures/Cropped_Faces"
    dpd_files_replace(directory)
