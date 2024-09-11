
README for Face Generation and Pain Estimation Models

Overview
This project provides various models for generating synthetic facial images and enhancing pain estimation using deep learning. It includes multiple models like StyleGAN2-ADA, StyleGAN3, 2CET-GAN, SimSwap GAN, and pain estimation models. Each model has its own requirements and setup instructions. You can follow the detailed steps for preprocessing data, generating images, and training models for your use case.

General Steps for Using the Models
Step 1: Preprocess the Data
Data preprocessing is the first step before using any of the models. Each model may require different data formats or preprocessing steps. Follow the steps in the Pre-processing file to ensure your data is ready for training or image generation.

Step 2: Model-Specific Instructions
Each model has specific instructions for image generation and training, detailed below.

---

Model 1: StyleGAN2-ADA

Path:
Notebook:
\Models\Face_Generation_Models\stylegan2-ada-pytorch-main\stylegan2-ada.ipynb
Pre-trained Weights:
Output_results\Style2GAN\output\00005-b_e-mirror-paper1024-kimg100-resumeffhq1024\network-snapshot-000100.pkl

Image Generation:
To generate images using the pre-trained StyleGAN2-ADA model, use the following command:
!python generate.py --outdir=D:/MS/Dissertation/Output_results/Style2GAN/output/generated/ --trunc=0.7 --seeds=1001-5000 --network="D:/MS/Dissertation/Output_results/Style2GAN/output/00005-b_e-mirror-paper1024-kimg100-resumeffhq1024/network-snapshot-000100.pkl"

Training the Model:
To train StyleGAN2-ADA, use this command (make sure to change the dataset path):
!source /usr/local/miniconda/bin/activate style-gan2-ada && python train.py \
    --outdir=/content/drive/MyDrive/stylegan2-ada-pytorch-main/output \
    --data=/content/drive/MyDrive/stylegan2-ada-pytorch-main/dataset/b_e.zip \
    --gpus=1 \
    --cfg=paper1024 \
    --mirror=1 \
    --resume=ffhq1024 \
    --snap=10 \
    --kimg=100

Requirements:
The detailed environment requirements for this model can be found in the following script:
D:\MS\Enhancing Pain Estimation through Synthetic Facial Image Generation and Deep Learning Models\Models\Face_Generation_Models\stylegan2-ada-pytorch-main\docker_run.sh

---

Model 2: StyleGAN3

Path:
Notebook:
\Models\Face_Generation_Models\stylegan3-main\stylegan3.ipynb
Pre-trained Weights:
Output_results\Style3GAN\output\00022-stylegan3-r-DPD_1024-gpus1-batch4-gamma6.6\network-snapshot-000016.pkl

Image Generation:
To generate images using StyleGAN3, use the following command:
!python gen_images.py --outdir=D:/MS/Dissertation/Output_results/Style3GAN/output/generated_images/ --trunc=0.7 --seeds=1001-5000 --network=D:/MS/Dissertation/Output_results/Style3GAN/output/00022-stylegan3-r-DPD_1024-gpus1-batch4-gamma6.6/network-snapshot-000016.pkl

Training the Model:
To train StyleGAN3, use this command:
!python train.py --outdir /content/drive/MyDrive/stylegan3-main/output/ \
                 --cfg=stylegan3-r \
                 --data /content/drive/MyDrive/stylegan3-main/data/DPD_1024.zip \
                 --gpus=1 \
                 --batch=4 \
                 --gamma=6.6 \
                 --mirror=1 \
                 --kimg=58 \
                 --snap=5 \
                 --resume=/content/drive/MyDrive/stylegan3-main/output/00012-stylegan3-r-DPD_1024-gpus1-batch4-gamma6.6/network-snapshot-000040.pkl

Requirements:
The detailed environment requirements for StyleGAN3 can be found in the following file:
Models\Face_Generation_Models\stylegan3-main\environment.yml

---

Model 3: 2CET-GAN

Path:
Notebook:
D:\MS\Enhancing Pain Estimation through Synthetic Facial Image Generation and Deep Learning Models\Models\Face_Generation_Models\2CET-GAN-main\Cycle-Gan.ipynb
Pre-trained Weights:
Output_results\2CET-GAN\models\550000_model_s.ckpt

Image Generation:
To transfer expressions using 2CET-GAN, use the following command:
python main.py --mode eval --eval_dir D:/MS/Dissertation/Output_results/2CET-GAN/eval --eval_model_step 550000 --img_size 128 --code_dim 32 --encoder_grey True --train_dir D:/MS/Dissertation/Output_results/2CET-GAN/train --test_dir D:/MS/Dissertation/Output_results/2CET-GAN/test --batch_size 8 --output_dir D:/MS/Dissertation/Output_results/2CET-GAN/output --models_dir D:/MS/Dissertation/Output_results/2CET-GAN/models

Training the Model:
To train 2CET-GAN, use the function train(config) in the .ipynb file.

Requirements:
The detailed environment requirements for 2CET-GAN can be found in:
Models\Face_Generation_Models\2CET-GAN-main\requirements.txt

---

Model 4: SimSwap GAN

Path:
Notebook:
Models\Face_Generation_Models\SimSwap-main\sim_swap.ipynb

Use the notebook to transfer expressions using SimSwap. The detailed explanation is available in the notebook itself.

---

Pain Estimation Models

To generate a pain score from faces, use the following script:
Models\Pain_Estimation_Model\get_facs.py

Refer to the code for more details on how to generate pain scores from facial images.

---

Pain Prediction Models

Steps for Creating a Train-Test Split for Pain Prediction:
1.Place All Data in One Folder
Ensure that all your data is consolidated into one folder before proceeding with the train-test split.

2.Rename Files Generated by StarGAN
Before running the train-test split script, you need to rename the files generated by StarGAN. Use the following script for renaming:

Models\Utils\openface-utils\stargan_renamer.py
This script will help standardize the file names, making it easier to manage and process the files.

3.Create a Train-Test Split
After renaming the files, use the following script to create a train-test split:
Models\Utils\predictive-utils\train_test_splitter.py
This script will divide your dataset into training and testing subsets, ensuring a proper distribution of data for pain prediction.

4.Separate Images Based on Pain Scores
Once the train-test split is done, separate the images based on their corresponding pain scores. You can use the following script for this purpose:

Models\Utils\predictive-utils\folder_tts.py
This step will help group images by pain scores, making it easier for model training and evaluation.