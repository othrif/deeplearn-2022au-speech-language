import subprocess

import torch
import transformers
import datasets

is_gpu_available = torch.cuda.is_available()

def display_library_version(library):
    print(f"Using {library.__name__} v{library.__version__}")

def install_requirements():
    """Installs the required packages for the project. Relevant when we are running in Google Colab"""
    cmd = ["python", "-m", "pip", "install", "-r", "requirements.txt"]
    process_install = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if process_install.returncode != 0:
        raise Exception("😭 Failed to install base requirements")
    else:
        print("✅ Base requirements installed!")
    print("⏳ Installing Git LFS ...")
    process_lfs = subprocess.run(["apt", "install", "git-lfs"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if process_lfs.returncode == -1:
        raise Exception("😭 Failed to install Git LFS and soundfile")
    else:
        print("✅ Git LFS installed!")


    print("⏳ Installing base requirements ...")

def setup_notebooks():
    # Check if we have a GPU
    if is_gpu_available:
        print('Nvidia GPU detected!')
        print('__CUDNN VERSION:', torch.backends.cudnn.version())
        print('__Number CUDA Devices:', torch.cuda.device_count())
        for i in range(torch.cuda.device_count()):
            print(f'__CUDA Device {i} Name:', torch.cuda.get_device_name(i))
            print(f'__CUDA Device {i} Total Memory [GB]:', torch.cuda.get_device_properties(0).total_memory / 1e9)
    else:
        print('No GPU was detected! This notebook can be *very* slow without a GPU!')

    # Give visibility on versions of the core libraries
    display_library_version(transformers)
    display_library_version(datasets)
    # Disable all info / warning messages
    transformers.logging.set_verbosity_error()
    datasets.logging.set_verbosity_error()