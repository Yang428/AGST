# AGST - Attention-based Gating network for Segmentation Tracking

## Publication
Yijin Yang and Xiaodong Gu.
Attention-based Gating Network for Robust Segmentation Tracking.
TCSVT, 2024.

# Abstract
Visual object tracking is a challenging task that aims to accurately estimate the scale and position of a designated target. Recently, segmentation networks have proven effective in visual tracking, producing outstanding results for target scale estimation. However, segmentation-based trackers still lack robustness due to the presence of similar distractors. To mitigate this issue, we propose an Attention-based Gating Network (AGNet) that produces gating weights to diminish the impact of feature maps linked to similar distractors. Subsequently, we incorporate the AGNet into the segmentation-based tracking paradigm to achieve accurate and robust tracking. Specifically, the AGNet utilizes three cascading Multi-Head Cross-Attention (MHCA) modules to generate gating weights that govern the generation of feature maps in the baseline tracker. The proficiency of the MHCA in modeling global semantic information effectively suppresses feature maps associated with similar distractors. Additionally, we introduce a distractor-aware training strategy that leverages distractor masks to train our model. To alleviate the issue of partial occlusion, we introduce a box refinement module to enhance the accuracy of the predicted target box. Comprehensive experiments conducted on 11 challenging tracking benchmarks show that our approach significantly surpasses the baseline tracker across all metrics and achieves excellent results on multiple tracking benchmarks.

## Running Environments
* Pytorch 1.1.0, Python 3.6.12, Cuda 9.0, torchvision 0.3.0, cudatoolkit 9.0, Matlab R2016b.
* Ubuntu 16.04, NVIDIA GeForce GTX 1080Ti.

## Installation
The instructions have been tested on an Ubuntu 16.04 system. In case of issues, we refer to these two links [1](https://github.com/alanlukezic/d3s) and [2](https://github.com/visionml/pytracking) for details.

#### Clone the GIT repository
```
git clone https://github.com/Yang428/AGST.git.
```

#### Install dependent libraries
Run the installation script 'install.sh' to install all dependencies. We refer to [this link](https://github.com/visionml/pytracking/blob/master/INSTALL.md) for step-by-step instructions.
```
bash install.sh conda_install_path pytracking
```

#### Or step by step install
```
conda create -n pytracking python=3.6
conda activate pytracking
conda install -y pytorch=1.1.0 torchvision=0.3.0 cudatoolkit=9.0 -c pytorch
conda install -y matplotlib=2.2.2
conda install -y pandas
pip install opencv-python
pip install tensorboardX
conda install -y cython
pip install pycocotools
pip install jpeg4py 
sudo apt-get install libturbojpeg
```

#### Or copy my environment directly.

You can download the packed conda environment from the [Baidu cloud link](https://pan.baidu.com/s/1gMQOB2Zs1UPj6n8qzJc4Lg?pwd=qjl2), the extraction code is 'qjl2'.

#### Download the pre-trained networks
You can download the models from the [Baidu cloud link](https://pan.baidu.com/s/1BarJfydZaiEbyI-usK2OkQ?pwd=thn4), the extraction code is 'thn4'. Then put the model files 'SegmNet.pth.tar' and 'IoUnet.pth.tar' to the subfolder 'pytracking/networks'.

## Testing the tracker
There are the [raw resullts](https://github.com/Yang428/AGST/tree/master/resultsOnBenchmarks) on eight datasets. 
1) Download the testing datasets OTB-100, LaSOT, Got-10k, TrackingNet, VOT2016, VOT2018, VOT2019 and VOT2020 from the following Baidu cloud links.
* [Got-10k](https://pan.baidu.com/s/1t_PvpIicHc0U9yR4upf-cA), the extraction code is '78hq'.
* [TrackingNet](https://pan.baidu.com/s/1BKtc4ndh_QrMiXF4fBB2sQ), the extraction code is '5pj8'.
* [VOT2016](https://pan.baidu.com/s/1iU88Aqq9mvv9V4ZwY4gUuw), the extraction code is '8f6w'.
* [VOT2018](https://pan.baidu.com/s/1ztAfNwahpDBDssnEYONDuw), the extraction code is 'jsgt'.
* [VOT2020](https://pan.baidu.com/s/16PFiEdnYQDIGh4ZDxeNB_w), the extraction code is 'kdag'.
* [OTB100](https://pan.baidu.com/s/1TC6BF9erhDCENGYElfS3sw), the extraction code is '9x8q'.
* [UAV123](https://pan.baidu.com/share/init?surl=OAUG8IrdqTRpGbK4Nv-bhA), the extraction code is 'vp4r'.
* [LaSOT](https://pan.baidu.com/s/1KBlrWGOFH9Fe85pCWN5ZkA&shfl=sharepset#list/path=%2F).
* [NFS](https://pan.baidu.com/share/init?surl=72r0r4y6UhAxzjc359yt6A), the extraction code is 'gc7u'.
* [TCL128](https://pan.baidu.com/share/init?surl=P4i63SrHhxMPShv7mWYZqg), the extraction code is '1h83'.
* Or you can download almost all tracking datasets from this web [link](https://blog.csdn.net/laizi_laizi/article/details/105447947#VisDrone_77).

2) Change the following paths to you own paths.
```
Network path: pytracking/parameters/agst/agst.py  params.segm_net_path.
Results path: pytracking/evaluation/local.py  settings.network_path, settings.results_path, dataset_path.
```
3) Run the AGST tracker on Got10k, TrackingNet, OTB100, UAV123, LaSOT, NFS and TCL128 datasets.
```
cd pytracking
python run_experiment.py myexperiments got10k
python run_experiment.py myexperiments trackingnet
python run_experiment.py myexperiments otb
python run_experiment.py myexperiments uav
python run_experiment.py myexperiments lasot
python run_experiment.py myexperiments nfs
python run_experiment.py myexperiments tpl
```

## Evaluation on VOT16 and VOT18 using Matlab R2016b
We provide a [VOT Matlab toolkit](https://github.com/votchallenge/toolkit-legacy) integration for the AGST tracker. There is the [tracker_AGST.m](https://github.com/Yang428/AGST/tree/master/pytracking/utils) Matlab file in the 'pytracking/utils', which can be connected with the toolkit. It uses the 'pytracking/vot_wrapper.py' script to integrate the tracker to the toolkit.

## Evaluation on VOT2020 and VOT2021 using Python Toolkit
We provide a [VOT Python toolkit](https://github.com/votchallenge/toolkit) integration for the AGST tracker. There is the [trackers.ini](https://github.com/Yang428/AGST/tree/master/pytracking/utils) setting file in the 'pytracking/utils', which can be connected with the toolkit. It uses the 'pytracking/vot20_wrapper.py' script to integrate the tracker to the toolkit.
```
cd pytracking/workspace_vot2020
pip install git+https://github.com/votchallenge/vot-toolkit-python
vot initialize <vot2020> --workspace ./workspace_vot2020/
vot evaluate AGST
vot analysis --workspace ./workspace_vot2020/AGST
```

## Training the networks
The AGST network is trained on the YouTube VOS, GOT-10K and TrackingNet datasets. Download the VOS training dataset (2018 version) and copy the files vos-list-train.txt and vos-list-val.txt from ltr/data_specs to the training directory of the VOS dataset. Download the bounding boxes from [this link](http://data.vicos.si/alanl/d3s/rectangles.zip) and copy them to the corresponding training sequence directories.
1) Download the YouTube VOS dataset from [this link](https://youtube-vos.org/challenge/2018/).
2) Download the GOT-10K dataset from [this link](https://blog.csdn.net/laizi_laizi/article/details/105447947#VisDrone_77).
3) Download the TrackingNet dataset from [this link](https://blog.csdn.net/laizi_laizi/article/details/105447947#VisDrone_77).
4) Download the pre-generated masks of GOT-10K and TrackingNet from [this link](https://drive.google.com/file/d/17YcdQOoA4DubK-krClJfxNtw9ooCyWHv/view). We refer to [this link](https://github.com/visionml/pytracking/blob/master/ltr/README.md#RTS) for more instructions.

5) Change the following paths to you own paths.
```
Workspace: ltr/admin/local.py  workspace_dir.
Dataset: ltr/admin/local.py  vos_dir.
```
3) Taining the AGST network
```
cd ltr
python run_training.py segm segm_default
then enable the distractor-aware loss in the 'AGST\ltr\train_settings\segm\segm_default.py'
run additional 5 epochs
```

## Acknowledgement
We would like to thank the author Martin Danelljan of [pytracking](https://github.com/visionml/pytracking) and the author Alan Lukežič of [D3S](https://github.com/alanlukezic/d3s).

## <b>BibTex citation:</b></br>
@ARTICLE{Yijin2024,<br>
title = {Attention-based Gating Network for Robust Segmentation Tracking},<br>
author = {Yijin, Yang. and Xiaodong, Gu.},<br>
journal = {TCSVT},<br>
volume  = {},<br>
pages = {},<br>
year    = {2024},<br>
doi = {10.1109/TCSVT.2024.3460400}<br>
}
