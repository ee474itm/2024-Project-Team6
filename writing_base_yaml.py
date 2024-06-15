import yaml

class MyDumper(yaml.SafeDumper):
    pass


def sequence_presenter(dumper, data):
    return dumper.represent_sequence('tag:yaml.org,2002:seq', data, flow_style=True)


MyDumper.add_representer(list, sequence_presenter)


def str_presenter(dumper, data):
    if data == "linear" or data == "Temporal_self" or data == "/mnt/hard1/ivymm04/PIA/models/PIA/pia.ckpt" or data == "/mnt/hard1/ivymm04/PIA/models/StableDiffusion/":
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='"')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)


MyDumper.add_representer(str, str_presenter)


def write_data(file_path, data):
    data["unet_additional_kwargs"]["motion_module_kwargs"]["attention_block_types"] = ["Temporal_self", "Temporal_self"]
    with open(file_path, 'w') as file:
        yaml.dump(data, file, Dumper=MyDumper, default_flow_style=False, sort_keys=False, indent=2)


def write_base_yaml(frame_num):
    yaml_data_base = {
        "generate": {"model_path": "/mnt/hard1/ivymm04/PIA/models/PIA/pia.ckpt",
                     "use_image": True,
                     "use_video": False,
                     "sample_width": 512,
                     "sample_height": 512,
                     "video_length": frame_num},

        "validation_data": {"mask_sim_range": [0, 1],
                            "cond_frame": 0,
                            "num_inference_steps": 25,
                            "img_mask": ''},

        "noise_scheduler_kwargs": {"num_train_timesteps": 1000,
                                   "beta_start": 0.00085,
                                   "beta_end": 0.012,
                                   "beta_schedule": "linear",
                                   "steps_offset": 1,
                                   "clip_sample": False},

        "pretrained_model_path": "/mnt/hard1/ivymm04/PIA/models/StableDiffusion/",

        "unet_additional_kwargs": {"use_motion_module": True,
                                   "motion_module_resolutions": [1, 2, 4, 8],
                                   "unet_use_cross_frame_attention": False,
                                   "unet_use_temporal_attention": False,
                                   "motion_module_type": "Vanilla",
                                   "motion_module_kwargs": {
                                       "num_attention_heads": 8,
                                       "num_transformer_block": 1,
                                       "attention_block_types": ["Temporal_Self", "Temporal_Self"],
                                       "temporal_position_encoding": True,
                                       "temporal_position_encoding_max_len": 32,
                                       "temporal_attention_dim_div": 1,
                                       "zero_initialize": True}}
    }

    write_data('/mnt/hard1/ivymm04/TEAM6/Result/base.yaml', yaml_data_base)