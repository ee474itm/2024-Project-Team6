# 2024-Project-Team6

## About U2NET

System Requirements: 


## About Instruct-pix2pix

### Set up a conda environment, and download a pretrained model:
```
conda env create -f environment.yaml -p ../../conda-env/ip2p
conda activate ../../conda-env/ip2p
bash scripts/download_checkpoints.sh
```
### Tips for changing image
1. If image changes too much

    Increasing the image CFG weight
   
    Decreasing the text CFG weight
   
3. If image doesn't change a lot
   
    Decreasing the image CFG weight
   
    Increasing the text CFG weight

## About TM2T

### Python Virtual Environment

Anaconda is recommended for this virtual environment.

```
conda create -f environment.yaml
conda activate tm2t
```

If you cannot successfully create the environment, here is a list of required libraries:
```
Python = 3.7.9   # Other version may also work but is not tested.
PyTorch = 1.6.0 (conda install pytorch==1.6.0 torchvision==0.7.0 -c pytorch)  #Other version may also work but are not tested.
scipy
numpy
tensorflow       # For use of tensorboard only
spacy
tqdm
ffmpeg = 4.3.1   # Other version may also work but are not tested.
matplotlib = 3.3.1
nlpeval (https://github.com/Maluuba/nlg-eval)     # For evaluation of motion-to-text only
bertscore (https://github.com/Tiiiger/bert_score) # For evaluation of motion-to-text only
```

### Download Dataset

Before Inference, please download TM2T model's pre-trianed model and dataset. It is necessary for inference.
Use the following commands.

In this model, we can use HumanML3D or KIT-ML dataset. However, in this project, KIT-ML dataset is used.
You can go to this link [Dataset Link] (https://drive.google.com/drive/folders/1MnixfyGfujSP-4t8w_2QvjtTVpEKr97t) for KIT-ML dataset.

If you want to use HumanML3D dataset, go to this link [HumanML3D Link] (https://github.com/EricGuo5513/HumanML3D?tab=readme-ov-file).

### Data Structure
```
<DATA-DIR>
./animations.rar        //Animations of all motion clips in mp4 format.
./new_joint_vecs.rar    //Extracted rotation invariant feature and rotation features vectors from 3d motion positions.
./new_joints.rar        //3d motion positions.
./texts.rar             //Descriptions of motion data.
./Mean.npy              //Mean for all data in new_joint_vecs
./Std.npy               //Standard deviation for all data in new_joint_vecs
./all.txt               //List of names of all data
./train.txt             //List of names of training data
./test.txt              //List of names of testing data
./train_val.txt         //List of names of training and validation data
./val.txt               //List of names of validation data
./all.txt               //List of names of all data
```

The file named in "MXXXXXX.*" (e.g., 'M000000.npy') is mirrored from file with correspinding name "XXXXXX.*" (e.g., '000000.npy'). Text files and motion files follow the same naming protocols, meaning texts in "./texts/XXXXXX.txt"(e.g., '000000.txt') exactly describe the human motions in "./new_joints(or new_joint_vecs)/XXXXXX.npy" (e.g., '000000.npy'). By passing npy values through model, we can get the predicted text about motion.


### Download Pre-trained Model
Create a checkpoint folder to place pre-traine models:
```
mkdir ./checkpoints
```

You can go to this link and download [Pre-trained Model] (https://drive.google.com/file/d/1xEoMy1aBRe0fxYeSzeLwzjHr9Ia6d6Gf/view).

```
./checkpoints/t2m/
./checkpoints/t2m/Comp_v6_KLD005/                   # A dumb folder containing information for evaluation dataloading
./checkpoints/t2m/VQVAEV3_CB1024_CMT_H1024_NRES3/  # Motion discretizer
./checkpoints/t2m/M2T_EL3_DL3_NH8_PS/              # Motion (token)-to-Text translation model
./checkpoints/t2m/T2M_Seq2Seq_NML1_Ear_SME0_N/     # Text-to-Motion (token) generation model
./checkpoints/t2m/text_mot_match/                  # Motion & Text feature extractors for evaluation
```

After downloading, place under the checkpoints directory.



## About PIA

Before Inference, please download PIA model's ckpt and StableDiffusion model. It is necessary to inference our model.
Use the following commands.

### Download checkpoints
<li>Download the Stable Diffusion v1-5</li>

```
conda install git-lfs
git lfs install
git clone https://huggingface.co/runwayml/stable-diffusion-v1-5 models/StableDiffusion/
```

<li>Download PIA</li>

```
git clone https://huggingface.co/Leoxing/PIA models/PIA/
```

<li>Download Personalized Models</li>

```
bash download_bashscripts/2-RcnzCartoon.sh
```


You can also download *pia.ckpt* manually through link on [Google Drive](https://drive.google.com/file/d/1RL3Fp0Q6pMD8PbGPULYUnvjqyRQXGHwN/view?usp=drive_link)
or [HuggingFace](https://huggingface.co/Leoxing/PIA).

Put checkpoints as follows:
```
└── models
    ├── DreamBooth_LoRA
    │   ├── ...
    ├── PIA
    │   ├── pia.ckpt
    └── StableDiffusion
        ├── vae
        ├── unet
        └── ...
```

## Inference
First, put the input image to the directory TEAM6/Input.

Second, run the following code:
```
python main_total.py
```
### User-Inputs
There are some user-inputs in our code.

<li>cfg values: </li>
<li>Edit condition: </li>
<li>Object feature: You should express the objects of your input image such as 1 girl, 2 person, 1 boy, etc.</li>
<li>Choose whether to create a motion emoticon or an emotion emoticon: If you want to create motion emoticon, press Y or y. If not, press N or n.</li>
<li>Motion: Press between 1(walk), 2(waving hands), 3(playing guitar). </li>
<li>Emotion: Enter the desired emotion you want to generate.</li>
<li>Change video length: You can modify the video length by modulate the number of video frames. Default video frame number is 16. If you want, press N or n and enter the number of frames. We recommend to enter between 10 and 22.</li>
