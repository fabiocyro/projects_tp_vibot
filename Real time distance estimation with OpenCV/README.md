# Real time distance estimation with OpenCV and Python

## Overview

<p>
  This works has as objective of using OpenCV and Python to perform object detection, in order to detect the distance between the camera and the object, which for this case will be our face.
  
</p>


<p>
  This is a simple project that uses interesting techinques that are a must for anyone who is starting in this world of Computer Vision and artificial intelligence.
  The algorithm used for this project will use Haar Cascades, and for the distance calculation we will use simple relations that involves the camera's focal length and some known measures.
</p>

## Haar Cascades


<p>
  Haar Cascade is a machine learning-based approach where a lot of positive and negative images are used to train the classifier. The algorithm was first introduced by Viola and James
  publication named Rapid Object Detection using a Boosted Cascade of Simple Features, and they are the most popular OpenCV's object detection technique. 
</p>

You can access the publication [here](https://www.cs.cmu.edu/~efros/courses/LBMV07/Papers/viola-cvpr-01.pdf)

<p>
  For those familiar with object detection, it is known already there are many more algorithms that are also more accurate than Haar cascades, such as HOG + Linear SVM, SSDs, Faster R-CNN, YOLO etc, 
  but it is impossible to deny their relevance still today, and they are still used for some applications, for example, for devices that are resource-constrained and can't afford or support a heavier detector and also, not forget to mention,
  that it is very hard to beat their speed. Other great advantage is that Haar Cascades are part of OpenCV, so no need to any extra coding, just call the detector and you are good to go.

The downside to Haar cascades is that they tend to be prone to false-positive detections, require parameter tuning when being applied for inference/detection, and just, in general, are not as accurate as the more “modern” algorithms we have today.
</p>

<p>
  In order to understand what the algorithm does under the hood it is necessary to understand what is a sliding window. As it can be seem on figure 1, a window pass through all the window
  and only the pixels inside the current window will be considered. At each stop along the sliding window path, the window must pass a series of tests where each subsequent test is more computationally expensive than the previous one. 
  If any one test fails, the window is automatically discarded. This was a concept proposed by the authors in order to reduce the computational costs and it was called <em>cascades</em> or <em>stages</em>.
</p>

![Figure 1: Sliding Window](https://user-images.githubusercontent.com/37183299/142020605-84ccce21-3852-4f12-87a2-a9ea95bfbb40.gif)


*Figure 1: Sliding window example. [Source](https://www.pyimagesearch.com/2021/04/12/opencv-haar-cascades/)*


<p>
  At each stop of the sliding window, it is calculated five feature windows and their goal are to match pixels the pixel on the image with the best rectangle. Figure 2 shows the rectangular features, while the figure 3 shows
  an example of how does the matching happens. To explain in more simple way: Suppose that on a sliding window we will try to detect the eyebrow of a person, well, the best rectangular feature to use would be the horizonal one, since the hair on the eyebrow 
  represents the darker part, while the skin presents the brighter part.
</p>

![Figure 2: Rectangular features](https://user-images.githubusercontent.com/37183299/142021625-e64237b3-8a76-49d6-b198-8ad621d323f6.png)

*Figure 2: Rectangular Features.*

![Figure 3: Example of use of the rectangular features](https://user-images.githubusercontent.com/37183299/142022711-adb8fd31-999f-4f10-9eca-6ebba3602061.png)

*Figure 3: Example of use of the rectangular features*

## Focal Length and Distance Finder

<p>
  The face detection is the first part of the algorithm, now that it is possible to detect a face, what can be done to measure the distance with respect to the camera?
  That is where the focal length comes in. 
</p>

<p>
  The focal length of the lens is the **distance between the lens and the image sensor when the subject is in focus**. It can be measured by quite several ways and for this work
  we will use the following relation:
</p>

## Requirements

* Python (version 3.6 was used here)
* OpenCV (version 4.4.0 for this example)
* Pre-trained face cascades file

Obs: there are other imports in the code such as argparse. This is optional and used as personal preference in order to create a code to be able to modify its parameters within the command line.
Just make sure to change the code accordingly. 

Just place everything into the same folder and you are good to go!


## Usage
On your terminal type: <br>

For the image script:

```
python real_time_distance.py -c haarcascade_frontalface_default.xml
```
