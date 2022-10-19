# Notebooks - Speech and Language Processing - DeepLearn 2022au

This repository contains some accompanying material to the course I am teaching on **Speech and Language Processing in Modern Applications** at [DeepLearn 2022](https://irdta.eu/deeplearn/2022au/) at Lulea University of Technology in Sweden. You can find the course description [here](https://irdta.eu/deeplearn/2022au/blog/speakers/othmane-rifki/)


In this repo, you will be able to:
1. Setup your environment
1. Run your first transformer
1. Fine-tune your transformer


### 1. Setup environment

You can run the notebooks in this repo either in your machine or in a cloud platform with a GPU. I recommend [Google Colab](https://colab.research.google.com/) as most work with large NLP models require a GPU to run in a reasonable amount of time and these cloud services come pre-installed with CUDA.

#### Running on Google Colab



|  Notebook | Colab  |
|---|---|
|  First | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/othrif/deeplearn-2022au-speech-language/blob/main/01_text_classifier.ipynb)  |
|   |   |
|   |   |


#### Running locally

To run the notebooks on your own machine, first clone the repository and navigate to it:
``` bash
$ git clone https://github.com/nlp-with-transformers/notebooks.git
$ cd notebooks
```

One of the best package and dependency managers in python is `conda`. Install `Miniconda` with:

``` bash
# Mac (Intel based)
$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
$ bash Miniconda3-latest-MacOSX-x86_64.sh

# Linux
$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
$ bash Miniconda3-latest-Linux-x86_64.sh
```

Create the environment with:
``` bash
# CPU-based
$ conda env create -f environment-cpu.yml

# GPU-based
$ conda env create -f environment-gpu.yml
```
You should see that your environment is active in your shell. For ex. `(deeplearn-cpu) othmane@My-MacBook-Pro ~ %`

Once you've installed the dependencies, you can activate the conda environment and spin up the notebooks as follows:
``` bash
# CPU-based
$ conda activate deeplearn-cpu

# GPU-based
$ conda activate deeplearn-gpu
```

Launch `jupyterhub`:
``` bash
$ jupyter lab
```
