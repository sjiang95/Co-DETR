
## Prerequisie

create conda env

```shell
conda create -n codetr
```

pytorch 1.11

```shell
conda install pytorch==1.11.0 torchvision==0.12.0 torchaudio==0.11.0 cudatoolkit=11.3 -c pytorch
```

or, if you prefer pip

```shell
pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113
```

mmcv 1.5.3

```shell
pip install mmcv-full==1.5.3 -f https://download.openmmlab.com/mmcv/dist/cu113/torch1.11.0/index.html
```

install mmdetection from this repo. `cd` to this repo, and run

```shell
pip install -v -e .
```