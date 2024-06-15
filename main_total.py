import os
import shutil
from subprocess import Popen, PIPE
import yaml
from writing_base_yaml import write_base_yaml
from writing_config_yaml import write_config_yaml

def file_exist_or_not():
    directory = './TM2T/motion_option'
    files_in_directory = os.listdir(directory)
    
    text_files = [file for file in files_in_directory if file.endswith(".txt")]
    return text_files
        


def store_motion_option(mot_cond, obj):
    file_name = './TM2T/motion_option/%s.txt' % (mot_cond)

    with open(file_name, 'w+') as file:
        file.write(obj + '\n')
        file.write(mot_cond)

def move_files(source_dir, dest_dir):
    # 원본 디렉토리에서 파일 목록 가져오기
    files = os.listdir(source_dir)

    for file_name in files:
        # 파일의 전체 경로 설정
        source_file = os.path.join(source_dir, file_name)
        dest_file = os.path.join(dest_dir, file_name)

        # 파일 이동
        shutil.move(source_file, dest_file)
        print(f'Moved: {source_file} -> {dest_file}')


def run_command_in_conda_env(env_name, command):
    # 환경 활성화와 명령어 실행
    init_cmd = 'source ~/anaconda3/etc/profile.d/conda.sh'
    activate_cmd = f'conda activate {env_name}'
    deactivate_cmd = 'conda deactivate'
    full_command = f'{init_cmd} && {activate_cmd} && {command} && {deactivate_cmd}'

    process = Popen(full_command, shell=True, executable='/bin/bash')
    process.communicate()


def run_model1():

    print("---1. Remove Background Step---\n")

    # 원본 디렉토리와 대상 디렉토리 설정
    input_directory = os.path.join(os.getcwd(), 'TEAM6/Input')
    temp_directory = os.path.join(os.getcwd(), 'TEAM6/Temp')
    destination_directory1 = os.path.join(os.getcwd(), 'U2Net/test_data/test_images')
    destination_directory2 = os.path.join(os.getcwd(), 'U2Net/test_data/finalResults')

    # 파일 이동 함수 호출1
    move_files(input_directory, destination_directory1)

    # 명령어 실행
    command1 = 'cd U2Net'
    command2 = 'python u2net_test.py'
    command3 = 'python applyMask_Removal.py'
    command4 = 'cd ..'
    
    command_test = f'{command1} && {command2} && {command4}'
    command_mask = f'{command1} && {command3} && {command4}'
    
    run_command_in_conda_env('U2NET', command_test)
    
    # 파일 이동 함수 호출2
    #move_files(destination_directory2, input_directory)

    run_command_in_conda_env('U2NET', command_mask)
    move_files(destination_directory2, temp_directory)
        
    


def run_model2():

    print("---2. Image Variation Step---\n")

    # 경로 설정
    team_folder = 'TEAM6'
    temp_folder = os.path.join(os.getcwd(), 'TEAM6/Temp')
    input_file = os.path.join(os.getcwd(), 'TEAM6/Temp/input.jpg')
    output_file = os.path.join(os.getcwd(), 'TEAM6/Temp/output.jpg')

    # cfg 값 입력받기
    text_cfg = float(input("Text CFG (default: 7.5): ") or 7.5)
    image_cfg = float(input("Image CFG (default: 1.5): ") or 1.5)

    # 편집 조건 입력받기
    edit_condition = input("Edit condition: ")

    # 명령어 실행
    command1 = 'cd pix2pix/instruct-pix2pix'
    command2 = f'CUDA_VISIBLE_DEVICES=2 python edit_cli.py --cfg-text {text_cfg} --cfg-image {image_cfg} --input {input_file} --output {output_file} --edit "{edit_condition}"'
    command3 = 'cd ../..'
    command = f'{command1} && {command2} && {command3}'
    run_command_in_conda_env('conda-env/ip2p', command)

def get_cond():
    print("---3. Generate Emoticon Step---\n")
    print("We can generate 1 emoticon")
    print("and you can choose the kind of emoticon: Emotion or Motion\n")
    print("---Object feature---")
    obj = input("Please express the object (etc. 1 girl, 2 person)\n")
    obj = str(obj)
    print("---Decide Motion or Emotion---")
    print("Do you want to generate motion emoticon?\n")
    print("If your answer is yes, press Y or y.\n")
    print("If your answer is no, press N or n.\n")

    while True:
        
        ck_motion = input()
        
        if ck_motion == "Y" or ck_motion == "y":
            print("---Motion---\n")
            print("We provide 3 motion conditions:\n")
            print(" -Press 1: walk\n")
            print(" -Press 2: waving hands\n")
            print(" -Press 3: playing guitar\n")
            while True:
                mot_type = input("Please type the number (Press between 1, 2, 3) \n")
                if mot_type == "1":
                    mot_cond = "walk"
                    break
                elif mot_type == "2":
                    mot_cond = "waving hands"
                    break
                elif mot_type == "3":
                    mot_cond = " playing guitar"
                    break
                else:
                    print("Impossible key input error! Please try again!\n")
                    print("Valid key input is 1, 2, 3.\n")

            store_motion_option(mot_cond, obj)
            write_config_yaml(obj, mot_cond)
            break

        elif ck_motion == "N" or ck_motion == "n":
            print("---Emotion---\n")
            emot_cond = input("Enter the condition of emotion!\n")
            write_config_yaml(obj, emot_cond)
            break

        else:
            print("Impossible key input error! Please try again!\n")
            print("Valid key input is Y, y, N, n.\n")
            
            
    print("We can change the length of video.\n")
    print("Do you want to change video length?\n")
    print("If your answer is yes, press Y or y.\n")
    print("If your answer is no, press N or n.\n")

    while True:
        ck_frame = input()
        
        if ck_frame == "Y" or ck_frame == "y":
            print("---Frame Number---\n")
            print("Recommend to choose from 10 to 22 (default:16)\n")
            mod_frame = input("Please type the number of frame\n")
            mod_frame = int(mod_frame)

            write_base_yaml(mod_frame)
            break

        elif ck_frame == "N" or ck_frame == "n":
            mod_frame = "16"
            mod_frame = int(mod_frame)

            write_base_yaml(mod_frame)
            break

        else:
            print("Impossible key input error! Please try again!\n")
            print("Valid key input is Y, y, N, n.\n")
    
    


def run_model3():
    # 환경 이름과 명령어 설정
    env_name = "tm2t"
    command1 = 'cd TM2T'
    command2 = 'python evaluate_m2t_transformer.py --name M2T_EL3_DL3_NH8_PS --gpu_id 2 --n_enc_layers 3 --n_dec_layers 3 --proj_share_weight --ext beam_search'
    command3 = 'cd ..'

    command = f'{command1} && {command2} && {command3}'
    
    run_command_in_conda_env(env_name, command)


def run_model4():

    #경로 설정
    config_file = os.path.join(os.getcwd(), 'TEAM6/Result/config.yaml')
    
    # 환경 이름과 명령어 설정
    env_name = "pia"
    command1 = 'cd PIA'
    command2 = f'python inference.py --config={config_file}'
    command3 = 'cd ..'
    
    command = f'{command1} && {command2} && {command3}'

    run_command_in_conda_env(env_name, command)


if __name__ == '__main__':
    run_model1()
    run_model2()
    get_cond()
    text_files = file_exist_or_not()
    if text_files != []:
        run_model3()
    run_model4()