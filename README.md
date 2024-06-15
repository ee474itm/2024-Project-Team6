# 2024-Project-Team6

## About Instruct-pix2pix

conda env create -f environment.yaml
conda activate ip2p
bash scripts/download_checkpoints.sh

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
