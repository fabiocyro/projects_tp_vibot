# Performing face detection using OpenCV and Deep Learning

## Overview

<p>
  Face detection is a very beginner-friendly project for those who are starting their paths with Computer Vision.<p>
<p>
  There are many algorithms and many approaches to help perform it, but with different level of difficulties and usually directly proportional to its accuracy.
  This method here utilizes Deep Learning in order to produces more stable and accurate results while not being too much computational demanding, and also having the great advantage of being included in OpenCV, thanks to Aleksandr Rybnikov, the primary contributor for the module.
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

Obs: there are other imports on the code such as imutils, time and argparse. They are optional and used as personal preference. Just make sure that if you are using OpenCV only, to modify the code for starting the camera and to perform some pre-processing 

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




