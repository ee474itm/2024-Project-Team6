import yaml

class MyDumper(yaml.SafeDumper):
    pass


def str_presenter(dumper, data):
    if data == 'output_instruct-pix2pix' or data == '/mnt/hard1/ivymm04/TEAM6/Temp' or data == '/mnt/hard1/ivymm04/TEAM6/Result/' or data == '/mnt/hard1/ivymm04/PIA/models/StableDiffusion/' or data == '/mnt/hard1/ivymm04/TEAM6/Result/base.yaml' or data == 'models/DreamBooth_LoRA/rcnzCartoon3d_v20.safetensors':
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style="'")
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)


MyDumper.add_representer(str, str_presenter)


def write_data(file_path, data):
    #data["unet_additional_kwargs"]["motion_module_kwargs"]["attention_block_types"] = ["Temporal_self", "Temporal_self"]
    with open(file_path, 'w') as file:
        yaml.dump(data, file, Dumper=MyDumper, default_flow_style=False, sort_keys=False, indent=2)


def write_config_yaml(main_ch, cond):

    prmt_list = [
        [
            f'{main_ch} {cond}, best quality'
        ]
    ]
    
    yaml_data_config = {
        "base": '/mnt/hard1/ivymm04/TEAM6/Result/base.yaml',
        "prompts": prmt_list,
        "n_prompt": ['wrong white balance, dark, sketches,worst quality,low quality, deformed, distorted, disfigured, bad eyes, wrong lips,weird mouth, bad teeth, mutated hands and fingers, bad anatomy,wrong anatomy, amputation, extra limb, missing limb, floating,limbs, disconnected limbs, mutation, ugly, disgusting, bad_pictures, negative_hand-neg'],
        "validation_data": {
            "input_name": 'output',
            "validation_input_path": '/mnt/hard1/ivymm04/TEAM6/Temp',
            "save_path": '/mnt/hard1/ivymm04/TEAM6/Result/',
        },
        "generate": {
            "use_lora": False,
            "use_db": True,
            "global_seed": 10201403011320481249,
            "lora_path": '',
            "db_path": 'models/DreamBooth_LoRA/rcnzCartoon3d_v20.safetensors',
            "lora_alpha": 0.8
        }
    }

    write_data('/mnt/hard1/ivymm04/TEAM6/Result/config.yaml', yaml_data_config)