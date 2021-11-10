# Pose estimation (Keypoint Detection) using OpenCV and Deep Learning

## Overview

<p>
  Pose estimation is a very known and research topic within the field of Computer Vision where we detect both position and orientation of a an object. <p>
<p>
  We have many examples that can be 
</p>
<p>
  OpenCV’s deep learning face detector is based on the Single Shot Detector (SSD) framework with a ResNet base network, and for this algorithm, we will use a pre-trained Caffe model and its weights to achieve our detection with great accuracy in real-time imaging.
</p>

## Requirements

* Python (version 3.6 was used here)
* The **.prototxt** file that defines the model architecture
* The **.caffemodel** with the weights
* OpenCV (version 4.4.0 for this example)
* NumPy

Obs: there are other imports in the code such as imutils, time and argparse. They are optional and used as personal preference. Just make sure that if you are using OpenCV only, to modify the code for starting the camera and to perform some pre-processing 

Just place everything into the same folder and you are good to go!

## Comments
<p>
  This model performs well even with not the best light conditions and with simple cameras, like an in-built webcame for example (check the result below). So, to conclude, this   project can help the user to better understand how to align deep learning and OpenCV to achieve some interesting results with accuracy.
</p>

![Result](https://user-images.githubusercontent.com/37183299/136977725-d42b881f-e446-4805-b3a6-e6d2afc8f4d2.jpg)

## Usage
On your terminal type: <br>
```
python detect_faces_video.py -p deploy.prototxt.txt -m res10_300x300_ssd_iter_140000.caffemodel
```




Link for the model: 

https://drive.google.com/file/d/1dCw5g8z_DscRa8E4JO9VCQXYeQEwx0lz/view?usp=sharing
