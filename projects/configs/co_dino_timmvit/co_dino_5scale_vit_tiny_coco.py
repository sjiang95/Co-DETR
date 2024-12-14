_base_ = ["co_dino_5scale_vit_large_coco.py"]
pretrained = None

model = dict(
    type="CoDETR",
    backbone=dict(
        type="VisionTransformer",
        img_size=1536,
        patch_size=16,
        embed_dim=192,
        depth=12,
        num_heads=3,
        # init_cfg=None
    ),
    neck=dict(
        type="SFP",
        in_channels=[192],
    ),
)
