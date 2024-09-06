import os, glob, shutil, argparse

def get_files(directory):
    return glob.glob(os.path.join(directory, '**', '*.jpg'), recursive=True)

def move_file(files, destination_dir):
    for file in files:
        file = file.replace("\\",'/')
        file_path = file.split("/")
        filename = file_path[-1]
        # print(filename)
        gender = file_path[-2].split("_")[1]
        # print(gender)
        if "Expression_Images" == file_path[-3]:
            prompt_level = filename.split(".")[0].split('_')[-1]
            if 'p1' in prompt_level:
                os.makedirs(name=destination_dir + 'Expression_Folder/' +"p1/" + gender, exist_ok=True)
                new_dir = destination_dir + 'Expression_Folder/' +"p1/" + gender
                destination_path = (new_dir + "/" + filename)
            elif 'p2' in prompt_level:
                os.makedirs(name=destination_dir + 'Expression_Folder/' +"p2/" + gender, exist_ok=True)
                new_dir = destination_dir + 'Expression_Folder/' +"p2/" + gender
                destination_path = (new_dir + "/" + filename)
            elif 'p3' in prompt_level:
                os.makedirs(name=destination_dir + 'Expression_Folder/' +"p3/" + gender, exist_ok=True)
                new_dir = destination_dir + 'Expression_Folder/' +"p3/" + gender
                destination_path = (new_dir + "/" + filename)
            elif 'p4' in prompt_level:
                os.makedirs(name=destination_dir + 'Expression_Folder/' +"p4/" + gender, exist_ok=True)
                new_dir = destination_dir + 'Expression_Folder/' +"p4/" + gender
                destination_path = (new_dir + "/" + filename)
            elif 'p5' in prompt_level:
                os.makedirs(name=destination_dir + 'Expression_Folder/' +"p5/" + gender, exist_ok=True)
                new_dir = destination_dir + 'Expression_Folder/' +"p5/" + gender
                destination_path = (new_dir + "/" + filename)
            elif 'p6' in prompt_level:
                os.makedirs(name=destination_dir + 'Expression_Folder/' +"p6/" + gender, exist_ok=True)
                new_dir = destination_dir + 'Expression_Folder/' +"p6/" + gender
                destination_path = (new_dir + "/" + filename)
            else:
                os.makedirs(name=destination_dir + 'Expression_Folder/' +"unidentified", exist_ok=True)
                new_dir = destination_dir + 'Expression_Folder/' +"unidentified"
                destination_path = (new_dir + "/" + filename)
        elif "Neutral_Images" == file_path[-3]:
            os.makedirs(name=destination_dir + 'Neutral_Folder/' +gender, exist_ok=True)
            new_dir = destination_dir + 'Neutral_Folder/' +gender
            destination_path = (new_dir + "/" + filename)
        shutil.copy(file, destination_path)
        print(f'Copied {file} to {destination_path}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rename folders in a directory by replacing a specified string with another string.")
    parser.add_argument('-dir', type=str, required=True, help="Path to the directory containing the folders to rename")
    parser.add_argument('-destination_dir', type=str, default=" ", required=True, help="String to be replaced in the folder names")

    args = parser.parse_args()

    all_files = get_files(args.dir)
    move_file(all_files, args.destination_dir)
    # all_files = get_files("D:/MS/Dissertation/Output_results/Faces_Cropped_SimSwap/")
    # move_file(all_files, "D:/MS/Dissertation/Output_results/Faces_Cropped_SimSwap/")