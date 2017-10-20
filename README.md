# brain-tumor-segmentation-resources

# Plan
1 2D CNN
每张mri图有24层，每层抓出来拼成一张大图，跑cnn

2 3D CNN 
2D CNN 忽略了层与层的关系
用3D CNN 做，设计3D CNN
推向科技 横平面 加 纵平面

3 RNN
CNN 作为 RNN的embedding
只有一个RNN

Feature rich -> 1 output
sample size is 200
easy to overfitting

use brats as pre trained model -> transfer learning

# TODO
data pre processing, reference:

this uses brats 2013 data, tested and able to correctly process all image data

https://github.com/cvdlab/nn-segmentation-for-lar

tested, doesn't run has bugs, still trying to make this work

https://github.com/naldeborgh7575/brain_segmentation

process our data:

--- convert all chinese character file names to english

--- skull strip

tried this: https://github.com/GUR9000/Deep_MRI_brain_extraction

I don't think this works well with our data, the t2 result is very dark

works well with data from here: https://www.nitrc.org/frs/?group_id=48

I have uploaded results in the predictions folder

Oct 1

Tried Nipype with FSL.BET (Brain Extraction Tool), result uploaded to t2_skull_stripped.nii.gz

works well upon initial inspection

--- downsize x and y dimensions (brats 2013 x,y is 160,216, brats 2015 is 240, 240, ours is 640,640)

--- make more layers, z dimension (brats 2013 had 176 layers, 2015 had 155 layers, ours only 24)

--- then feed all data to the pre-processing pipeline similar to github examples.

Oct16

Tried: https://github.com/Kamnitsask/deepmedic

pre-processed shanghai data to 256 x 256 jpegs

Oct20
https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html
https://stanford.edu/~shervine/blog/keras-how-to-generate-data-on-the-fly.html

# MRI basics
https://www.youtube.com/watch?v=CKbemQBAzUE

# Tutorials
https://blog.dataversioncontrol.com/best-practices-of-orchestrating-python-and-r-code-in-ml-projects-f28f3a879484

# Neuroscience software
http://neuro.debian.net/

https://miykael.github.io/nipype-beginner-s-guide/installation.html

https://miykael.github.io/nipype_tutorial/

# BRATS data
https://www.smir.ch/

# Promising
https://github.com/nilearn/nilearn

https://github.com/Kamnitsask/deepmedic

https://github.com/zsdonghao/u-net-brain-tumor

https://github.com/ellisdg/3DUnetCNN

# Segmentation
https://github.com/fabianbormann/Tensorflow-DeconvNet-Segmentation

https://github.com/naldeborgh7575/brain_segmentation

https://github.com/e271141/BRATS

https://github.com/kaspermarstal/BrainNet

https://github.com/jocicmarko/ultrasound-nerve-segmentation

https://github.com/pietz/brats-segmentation

https://github.com/GUR9000/Deep_MRI_brain_extraction


# Resources
https://github.com/desimone/segmentation-models

https://github.com/madlymissyou/deep-learning-for-neuroimage

https://github.com/jindongwang/transferlearning

https://github.com/dformoso/machine-learning-mindmap

https://github.com/mnielsen/neural-networks-and-deep-learning
