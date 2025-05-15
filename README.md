# 🧠 Face Generation & Pain Estimation Models

## 📌 Overview

This project includes deep learning pipelines for:

- **Synthetic facial image generation** using GANs.
- **Facial expression transformation.**
- **Pain intensity prediction** from facial expressions.

### Models Included:
- StyleGAN2-ADA
- StyleGAN3
- 2CET-GAN
- SimSwap GAN
- Pain Estimation & Prediction Pipelines

---

## ⚙️ General Workflow

### ✅ Step 1: Preprocess the Data

Ensure your dataset is properly cleaned and formatted.

- Follow model-specific preprocessing notebooks or scripts.
- Typically, datasets are expected as image folders or `.zip` archives.

### ✅ Step 2: Use a Model

Instructions for each model are detailed below.

---

## 🎨 Model 1: StyleGAN2-ADA

**Notebook:**  
`Models/Face_Generation_Models/stylegan2-ada-pytorch-main/stylegan2-ada.ipynb`

**Pre-trained Weights:**  
`Output_results/Style2GAN/output/00005-b_e-mirror-paper1024-kimg100-resumeffhq1024/network-snapshot-000100.pkl`

**🖼️ Image Generation:**
```bash
python generate.py \
  --outdir=D:/MS/Dissertation/Output_results/Style2GAN/output/generated/ \
  --trunc=0.7 \
  --seeds=1001-5000 \
  --network="D:/MS/Dissertation/Output_results/Style2GAN/output/00005-b_e-mirror-paper1024-kimg100-resumeffhq1024/network-snapshot-000100.pkl"
```

**🏋️‍♂️ Model Training:**
```bash
source /usr/local/miniconda/bin/activate style-gan2-ada && python train.py \
  --outdir=/content/drive/MyDrive/stylegan2-ada-pytorch-main/output \
  --data=/content/drive/MyDrive/stylegan2-ada-pytorch-main/dataset/b_e.zip \
  --gpus=1 \
  --cfg=paper1024 \
  --mirror=1 \
  --resume=ffhq1024 \
  --snap=10 \
  --kimg=100
```

**📋 Requirements:**  
Environment setup: `stylegan2-ada-pytorch-main/docker_run.sh`

---

## 🎨 Model 2: StyleGAN3

**Notebook:**  
`Models/Face_Generation_Models/stylegan3-main/stylegan3.ipynb`

**Pre-trained Weights:**  
`Output_results/Style3GAN/output/00022-stylegan3-r-DPD_1024-gpus1-batch4-gamma6.6/network-snapshot-000016.pkl`

**🖼️ Image Generation:**
```bash
python gen_images.py \
  --outdir=D:/MS/Dissertation/Output_results/Style3GAN/output/generated_images/ \
  --trunc=0.7 \
  --seeds=1001-5000 \
  --network="D:/MS/Dissertation/Output_results/Style3GAN/output/00022-stylegan3-r-DPD_1024-gpus1-batch4-gamma6.6/network-snapshot-000016.pkl"
```

**🏋️‍♂️ Model Training:**
```bash
python train.py \
  --outdir=/content/drive/MyDrive/stylegan3-main/output \
  --cfg=stylegan3-r \
  --data=/content/drive/MyDrive/stylegan3-main/data/DPD_1024.zip \
  --gpus=1 \
  --batch=4 \
  --gamma=6.6 \
  --mirror=1 \
  --kimg=58 \
  --snap=5 \
  --resume=/content/drive/MyDrive/stylegan3-main/output/00012-stylegan3-r-DPD_1024-gpus1-batch4-gamma6.6/network-snapshot-000040.pkl"
```

**📋 Requirements:**  
`stylegan3-main/environment.yml`

---

## 🎨 Model 3: 2CET-GAN

**Notebook:**  
`Models/Face_Generation_Models/2CET-GAN-main/Cycle-Gan.ipynb`

**Pre-trained Weights:**  
`Output_results/2CET-GAN/models/550000_model_s.ckpt`

**🖼️ Expression Transfer:**
```bash
python main.py --mode eval \
  --eval_dir D:/MS/Dissertation/Output_results/2CET-GAN/eval \
  --eval_model_step 550000 \
  --img_size 128 \
  --code_dim 32 \
  --encoder_grey True \
  --train_dir D:/MS/Dissertation/Output_results/2CET-GAN/train \
  --test_dir D:/MS/Dissertation/Output_results/2CET-GAN/test \
  --batch_size 8 \
  --output_dir D:/MS/Dissertation/Output_results/2CET-GAN/output \
  --models_dir D:/MS/Dissertation/Output_results/2CET-GAN/models
```

**🏋️‍♂️ Model Training:**  
Use the `train(config)` function in the notebook.

**📋 Requirements:**  
`2CET-GAN-main/requirements.txt`

---

## 🎨 Model 4: SimSwap GAN

**Notebook:**  
`Models/Face_Generation_Models/SimSwap-main/sim_swap.ipynb`

Use the notebook to apply facial expression transfer with SimSwap. Configuration and usage are described inside.

---

## 🩺 Pain Estimation & Prediction

**Pain Estimation Script:**  
```bash
Models/Pain_Estimation_Model/get_facs.py
```

Use this to generate pain scores from images.

### Steps for Pain Prediction

1. **Place all images in one folder.**
2. **Rename StarGAN-generated files:**
```bash
Models/Utils/openface-utils/stargan_renamer.py
```
3. **Train-Test Split:**
```bash
Models/Utils/predictive-utils/train_test_splitter.py
```
4. **Separate Images by Score:**
```bash
Models/Utils/predictive-utils/folder_tts.py
```

---

## 🧪 Final Notes

- All paths are relative to project root.
- Use appropriate `conda` or `requirements.txt` to manage environments per model.
- Outputs are saved under `/Output_results/`.

---

© 2025 FaceGen-PainAI Toolkit
