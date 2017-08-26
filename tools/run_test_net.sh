#!/bin/bash

./train_net.py --device gpu --device_id 0 --weights /workspace/MV3D_TF/output/faster_rcnn_end2end/train/VGGnet_fast_rcnn_iter_3.ckpt.meta --imdb kitti_test --cfg /workspace/MV3D_TF/experiments/cfgs/faster_rcnn_end2end.yml --network MV3D_test
