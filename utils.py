import torch
import transformers
import datasets

is_gpu_available = torch.cuda.is_available()

def display_library_version(library):
    print(f"Using {library.__name__} v{library.__version__}")


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