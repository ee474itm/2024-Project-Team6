# 2024-Project-Team6

Before Inference, Please download PIA model's ckpt and StableDiffusion model. It is necessary to inference our model.
Use the following commands.


# About PIA
## Setup

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
