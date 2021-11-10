# Pose estimation (Keypoint Detection) using OpenCV and Deep Learning

## Overview

<p>
  Pose estimation is a very known and research topic within the field of Computer Vision where we detect both position and orientation of a an object. It has also a vast number of applications such as:
</p>

* Human Tracking
* Gaming features
* Video surveillance
* Advanced Driver Assistance Systems (ADAS)
* etc.

<p>
  All of these examples use one of the many different methods. As an example we can say that Video Surveillance can use face pose estimation (facial landmark detection) to detect people's faces, or even the whole body, with a different method of course. We have also other examples like head pose estimation, which uses the facial landmark in order to obtain the 3D orientation of the human head with respect to the camera and also human pose estimation, which focus on detecting and localizing the major parts/joints of the body, and, after achieving this point, perform some action on it. And it is this last example what we will work with but we will stick to the detection only for a sort of introductory work and to make easier the reading/learning process. The typical output after the detection is shown below:<br>

![Figure 1: Typical output of a human pose estimation algorithm. Source: free images on internet](https://user-images.githubusercontent.com/37183299/141136853-e2dbbfb5-d9e6-4eb7-ae62-ceab8aa579d9.jpg)<br>
 *Figure 1: Typical output of a human pose estimation algorithm. Source: free images on internet*
</p>

## Datasets

<p>
  In order to perform the detection is necessary to have a dataset trained on. And throughout the years, AI enthusiasts decided that pretty much every problem is just a dataset away of being conquered. Because of that, very interesting datasets were released during the pasts years such as:
  
  1. [COCO Keypoints Challenge](http://cocodataset.org/#keypoints-2018)
  2. [MPII Human Pose Dataset](http://human-pose.mpi-inf.mpg.de/)
  3. [VGG Pose Dataset](http://www.robots.ox.ac.uk/~vgg/data/pose_evaluation/)

  And for this work, the COCO dataset will be used by purely preference, feel free to try with the others.
</p>

## Multi-person Pose Estimation Model

<p>
  
  For this tutorial, the model used is based on a paper titled [Multi-Person Pose Estimation](https://arxiv.org/pdf/1611.08050.pdf), by the Perceptual Computing Lab at Carnegie Mellon University.
  
</p>

![Figure 2: Multi-person Pose Estimation model architecture](https://user-images.githubusercontent.com/37183299/141149372-527e13e2-1879-4ab9-be2b-5c66af9b0c21.jpg)
*Figure 2: Multi-person Pose Estimation model architecture*


<p>
 
  For this task it is trained a very deep neural network. The model takes as input a color image of size w × h and produces, as output, the 2D locations of keypoints for each person in the image. The detection takes place in three stages:

- **Stage 0**: The first 10 layers of the VGGNet are used to create feature maps for the input image.
- **Stage 1**: A 2-branch multi-stage CNN is used where the first branch predicts a set of 2D confidence maps (S) of body part locations ( e.g. elbow, knee etc.). Given below are confidence maps and Affinity maps for the keypoint – Left Shoulder.
  
![Figure 3](https://learnopencv.com/wp-content/uploads/2018/05/confidence-left-shoulder.jpg)<br>
*Figure 3 : Showing confidence maps for Left Shoulder*
  
The second branch predicts a set of 2D vector fields (L) of part affinities, which encode the degree of association between parts. In the figure below part affinity between the Neck and Left shoulder is shown.

![Figure 4](https://learnopencv.com/wp-content/uploads/2018/05/heatmap-left-shoulder.jpg)<br>
*Figure 4 : Showing Part Affinity maps for Neck – Left Shoulder pair for the given image*
  
- **Stage 2**: The confidence and affinity maps are parsed by greedy inference to produce the 2D keypoints for all people in the image. 
  
</p>

## Requirements

* Python (version 3.6 was used here)
* The **.prototxt** file that defines the model architecture
* The **.caffemodel** with the weights, you can download it from here: [Caffe Model](https://drive.google.com/file/d/1dCw5g8z_DscRa8E4JO9VCQXYeQEwx0lz/view?usp=sharing)
* OpenCV (version 4.4.0 for this example)
* NumPy

Obs: there are other imports in the code such as imutils, time and argparse. They are optional and used as personal preference. Just make sure that if you are using OpenCV only, to modify the code for starting the camera and to perform some pre-processing 

Just place everything into the same folder and you are good to go!

## Comments and important observations
<p>
  This model performs well even with not the best light conditions and with simple cameras, like an in-built webcame for example (check the result below). So, to conclude, this   project can help the user to better understand how to align deep learning and OpenCV to achieve some interesting results with accuracy.
</p>


## Usage
On your terminal type: <br>
```
python detect_faces_video.py -p deploy.prototxt.txt -m res10_300x300_ssd_iter_140000.caffemodel
```
