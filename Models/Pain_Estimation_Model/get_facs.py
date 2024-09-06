import os
import subprocess
import pandas as pd
from glob import glob
from concurrent.futures import ThreadPoolExecutor, as_completed

def get_files(directory, file_type):
    """Utility function to get all files with a specific extension in a directory."""
    return glob(os.path.join(directory, '**', f'*.{file_type}'), recursive=True)

def process_image(face_image, landmarkds_op, FACE_DETECTION_OPENFACS):
    """
    Processes a single image by setting up the output directories and running face detection.
    
    Parameters:
    - face_image (str): Path to the input image file.
    - landmarkds_op (str): Path to save the output of landmark detection.
    - FACE_DETECTION_OPENFACS (str): Path to the face detection executable.
    """

    # Construct and standardize the output directory path for landmarks
    output_dir_landmarks = '.'.join(landmarkds_op.replace('\\', '/').split('.')[:-1])

    # Prepare the command to run the face detection tool with specified options
    command = [
        FACE_DETECTION_OPENFACS,
        '-f', face_image.replace("\\", "/"),
        '-out_dir', output_dir_landmarks.replace("\\", "/"),
        '-vis-track', output_dir_landmarks.replace("\\", "/"),
        '-vis-hog', output_dir_landmarks.replace("\\", "/"),
        '-vis-aus', output_dir_landmarks.replace("\\", "/"),
    ]

    # Execute the command and handle any errors
    try:
        print(command)
        # Ensure the output directory for the landmarks exists
        os.makedirs(name=output_dir_landmarks, exist_ok=True)
        subprocess.run(command, check=True, capture_output=True, text=True)
        print(f"Successfully processed {face_image}")
    except subprocess.CalledProcessError as e:
        print(f"Error processing {face_image}: {e}")
        print(e.stderr)
    except FileNotFoundError as e:
        print(f"Executable not found: {FACE_DETECTION_OPENFACS}")
        print(e)

def process_images_in_parallel(image_paths, replace_from, replace_to, FACE_DETECTION_OPENFACS, workers=128):
    """
    Processes multiple images in parallel using ThreadPoolExecutor.
    
    Parameters:
    - image_paths (list): List of image file paths to process.
    - replace_from (str): String to be replaced in the output path.
    - replace_to (str): String to replace with in the output path.
    - FACE_DETECTION_OPENFACS (str): Path to the face detection executable.
    - workers (int): Number of parallel workers (default is 200).
    """
    # Use ThreadPoolExecutor to process images concurrently
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = []
        for face_image in image_paths:
            # Construct the output path by replacing part of the image path
            output_path = face_image.replace('\\', '/').replace(replace_from, replace_to)

            # Submit the image processing task to the executor
            futures.append(executor.submit(process_image, face_image, output_path, FACE_DETECTION_OPENFACS))
        
        # Wait for all submitted tasks to complete
        for future in as_completed(futures):
            future.result()  # Retrieve result to catch exceptions if any

def merge_csvs_and_generate_excel(csv_directory, excel_save_path):
    """
    Merges multiple CSV files from the specified directory into a single DataFrame, 
    and saves the result as an Excel file.
    
    Parameters:
    - csv_directory (str): Path to the directory containing the CSV files to merge.
    - excel_save_path (str): Path to save the generated Excel file.
    """
    def process_file(file):
        """Reads a single CSV file and returns it as a DataFrame."""
        df = pd.read_csv(file)
        df.columns = [column.strip() for column in df.columns]
        index_v = df.index
        df['PSPI_Score'] = (df.loc[index_v[0], 'AU04_c'] + max(df.loc[index_v[0], 'AU06_c'], df.loc[index_v[0], 'AU07_c']) +
                            max(df.loc[index_v[0], 'AU09_c'], df.loc[index_v[0], 'AU10_c']) + df.loc[index_v[0], 'AU45_c'])
        df['subjects_name'] = os.path.splitext(os.path.basename(file))[0]
        return df

    # Get all CSV files in the directory
    csv_files = get_files(csv_directory, "csv")

    # List to collect DataFrames
    df_list = []

    for file in csv_files:
        result = process_file(file)
        if result is not None:
            df_list.append(result)

    if df_list:
        # Merge all DataFrames into one
        combined_df = pd.concat(df_list, ignore_index=True)
        combined_df.set_index('subjects_name', inplace=True)
        
        # Save to Excel
        combined_df.to_excel(excel_save_path, index=True)
        print(f"Excel file saved to: {excel_save_path}")
    else:
        print("No valid CSV files found.")

if __name__ == "__main__":
    path = 'C:/Users/psxah20/Desktop/Dissertation/Stargan-3'
    # Let's process for DPD Dataset
    process_images_in_parallel(
        (get_files(path, 'png') 
         + get_files(path, 'jpg')),  # List of all image file paths in the DPD dataset
        path,  # Part of the path to be replaced in the output paths
        'C:/Users/psxah20/Desktop/Dissertation/openfacs-stargan3/',  # Replacement path where the output will be saved
        'P:/Dissertation/Models/Face_Detection_Model/OpenFace_2.2.0_win_x64/FeatureExtraction.exe',  # Path to the face detection executable
        workers=64  # Number of parallel workers to use for processing
    )

    # Now merge the CSV files and generate an Excel file
    merge_csvs_and_generate_excel(
        "C:/Users/psxah20/Desktop/Dissertation/openfacs-stargan3/",  # Directory containing the CSV files
        "C:/Users/psxah20/Desktop/Dissertation/openfacs-stargan3/pspi_predicted.xlsx"  # Path to save the Excel file
    )