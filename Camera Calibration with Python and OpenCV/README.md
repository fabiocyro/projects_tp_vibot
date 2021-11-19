# Camera Calibration with Python and OpenCV

## Overview

<p>
  Camera calibration is an essential step to be comfortable with, specially if you are using for Vision purposes. This is extremely important because if you really want to have meaningful data we need to have a well calibrated camera. The reason why this became so necessary is due to the fact that with the huge amount of cameras around with the most different types of qualities, most of them, specially the cheapest ones don't reproduce exactly the images. Figure 1 shows the types of distortion that they have and figure 2 shows a real example: 
</p>

![fig1](https://user-images.githubusercontent.com/37183299/142648035-aa4bde62-c597-4dcf-b50c-8ce8f5caf943.jpeg) <br>
*Figure 1: Camera distortion types. [Source](https://aliyasineser.medium.com/opencv-camera-calibration-e9a48bdd1844)* <br>

![fig2](https://user-images.githubusercontent.com/37183299/142648166-dd217d99-6ee0-427b-93f8-2b272730402a.jpg) <br>
*Figure 2: Example of uncalibrated camera. [Source](https://docs.opencv.org/3.4/dc/dbb/tutorial_py_calibration.html)*

<p>
  As it can be seen from Figure 2, the drew lines don't follow exactly the lines from the chessboard, which for more precise applications can be a huge interference, that is why it is so necessary to perform the calibration.
</p>

## Requirements


* Python (version 3.6)
* OpenCV (version 4.4.0)
* Chessboard image. For this example was used a 9x6 chessboard with a square size of 2.5 centimeters. Figure 3 shows the chessboard image used. Feel free to use any other one, just make sure to change the respective values while calling the function.



![chessboard](https://user-images.githubusercontent.com/37183299/142653771-7e7ffd7e-e8e6-4b43-8917-97a3538790dd.png)
*Figure 3: Chessboard for calibration.*




Obs: there are other imports in the code such as argparse. This is optional and used as personal preference in order to create a code to be able to modify its parameters while being called on the command line.
Just make sure to change the code accordingly if no intention to use it. 

## Setup!


<p>
  In order to be ready to calibrate the camera, and consequently, run the code, it is necessary to prepare at least 10 photos with the chessboard (according to OpenCV's documentation) at different positions, angles, and distances, but it is not a problem to take a little bit more than that. Also, fix the chessboard on a flat surface, for avoiding the paper to twist and consequently providing bad results. For this example, 20 pictures were taken. The pictures below show some of the examples of the dataset:
</p>


![image1](https://user-images.githubusercontent.com/37183299/142650315-a9779080-aaa5-424b-8b03-67cb53666f47.jpg)
![image4](https://user-images.githubusercontent.com/37183299/142650332-2926841e-f3d2-4738-9492-cfd7a4cf60a5.jpg)
*Figure 4, 5: Samples from the dataset.*

<p>
  After creating your own dataset, rename each image for image1, image2 etc, for not running into any troubles. After that, just run the code and check the results. Pay attention to the RMS (root mean squared) at the end. This is a metric that shows how accurate was your calibration and its value needs to be between 0 and 1, the lower the better.
</p>


## Usage
On your terminal type: <br>


```
python camera_calibration.py --image_dir YOUR_DIRECTORY_WITH_THE_DATASET 
                             --image_format YOUR_IMAGES_FORMAT 
                             --prefix image 
                             --square_size 2.5
                             --width 9 
                             --height 6 
                             --save_file NAME_OF_YOUR_CALIBRATION_FILE.yml
```
