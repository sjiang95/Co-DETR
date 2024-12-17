_base_ = ["co_dino_5scale_vit_large_coco.py"]
pretrained = None

model = dict(
    type="CoDETR",
    backbone=dict(
        type="VisionTransformer",
        img_size=1536,
        patch_size=16,
        embed_dim=1280,
        depth=32,
        num_heads=16,
        # init_cfg=None
    ),
    neck=dict(
        type="SFP",
        in_channels=[1280],
    ),
)

data = dict(
    samples_per_gpu=1, # use 16 gpus for batchsize=16
    workers_per_gpu=1,
)
