import os, glob, shutil, argparse
import pandas as pd

def unbc_files_replace(directory):
    xlsx_file = "C:/Users/psxah20/Desktop/Dissertation/UNBC_OPENFACS/UNBC_Previous_Study.xlsx"
    facs_unbc = pd.read_excel(io=xlsx_file, sheet_name=1, index_col='Target')
    pain_scores = facs_unbc['PSPI_Score']
    pain_scores.index = [idx.split("_")[0] for idx in facs_unbc.index]
    pain_scores.columns = ["PSPI_Score"]

    unbc_files = (glob.glob(os.path.join(directory, '**', '*.jpg'), recursive=True) + 
                 glob.glob(os.path.join(directory, '**', '*.png'), recursive=True))
    
    for files in unbc_files:
        files = files.replace("\\","/")
        file_name = files.split("/")[-1].split(".")[0]
        if file_name in pain_scores.index:
            if pain_scores.loc[file_name] != 0:
                new_file_name = file_name + "_pain" + str(pain_scores.loc[file_name])
                new_file_path = files.replace(file_name, new_file_name).replace("UNBC-McMaster/Images","UNBC_Pain_score")

                destination_folder = "/".join(new_file_path.split("/")[:-1])

                os.makedirs(name=destination_folder, exist_ok=True)
                shutil.copy(files, new_file_path)
                # print("Saved:",new_file_name,"in",destination_folder)
        else:
            print("Unable to process",files)

if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description="replace folders in a directory by replacing a specified string with another string.")
    # parser.add_argument('-dir', type=str, required=True, help="Path to the directory containing the folders to replace")

    # args = parser.parse_args()

    # all_files = unbc_files_replace(args.dir)
    all_files = unbc_files_replace("C:/Users/psxah20/Desktop/Dissertation/UNBC-McMaster/Images")