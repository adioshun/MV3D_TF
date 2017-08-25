#!/bin/bash

./train_net.py --device gpu --device_id 0 --weights /workspace/MV3D_TF/data/pretrain_model/VGG_imagenet.npy --iters 50001 --cfg /workspace/MV3D_TF/experiments/cfgs/faster_rcnn_end2end.yml --network MV3D_train

