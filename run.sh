#!/bin/bash
# python run.py --encoder vitb --img-path /w/339/kecenyao/Depth-Anything-V2/metric_depth/dataset/splits/vkitti2-mb/test_infer.txt --outdir /w/339/kecenyao/Depth-Anything-V2/metric_depth/dataset/splits/vkitti2-mb/test_depthanythingv2 --pred-only
# python run.py --encoder vitb --img-path /w/339/kecenyao/Depth-Anything-V2/metric_depth/dataset/samples/raw --outdir /w/339/kecenyao/Depth-Anything-V2/metric_depth/dataset/samples/dav2 --pred-only --grayscale


cd metric_depth
# bash dist_train.sh
python run.py \
  --encoder vitb \
  --load-from /w/339/kecenyao/Depth-Anything-V2/checkpoints/depth_anything_v2_mb-last.pth \
  --max-depth 80 \
  --img-path /w/339/kecenyao/Depth-Anything-V2/metric_depth/dataset/samples/raw --outdir /w/339/kecenyao/Depth-Anything-V2/metric_depth/dataset/samples/ours-last --pred-only --grayscale