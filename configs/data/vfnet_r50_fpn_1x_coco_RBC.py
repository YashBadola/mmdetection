# The new config inherits a base config to highlight the necessary modification
_base_ = '../vfnet/vfnet_r50_fpn_1x_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    bbox_head=dict(
            num_classes=1))

# Modify dataset related settings
dataset_type = 'COCODataset'
classes = ('RBC',)
runner = dict(type='EpochBasedRunner', max_epochs=10000)
checkpoint_config = dict(interval=250)
data = dict(
    train=dict(
        img_prefix='data/',
        classes=classes,
        ann_file='data/annotation_coco.json'),
    val=dict(
        img_prefix='data/',
        classes=classes,
        ann_file='data/annotation_coco.json'),
    test=dict(
        img_prefix='data/',
        classes=classes,
        ann_file='data/annotation_coco.json'))

# # We can use the pre-trained Mask RCNN model to obtain higher performance
# load_from = 'checkpoints/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco_bbox_mAP-0.408__segm_mAP-0.37_20200504_163245-42aa3d00.pth'