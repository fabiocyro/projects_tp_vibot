# Pose estimation for images with OpenCV and Deep Learning

# USAGE
# python pose_image.py -i sample.png -p deploy.prototxt.txt -m pose_iter_440000.caffemodel

# importing necessary packages
import numpy as np
import cv2
import argparse

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser(description = "Run your pose estimation algorithm for image")
ap.add_argument("-i", "--image", required=True, help="Path to the input image"),
ap.add_argument("-p", "--prototxt", required=True, help = "Path to the Caffe 'deploy' prototxt file"),
ap.add_argument("-m", "--model", required=True, help = "Path to the Caffe model"),
ap.add_argument("-t", "--threshold", type=float, default=0.1)
args = vars(ap.parse_args())

# initializing parameters for COCO dataset
nPoints = 18
POSE_PAIRS = [ [1,0],[1,2],[1,5],[2,3],[3,4],[5,6],[6,7],[1,8],[8,9],[9,10],[1,11],[11,12],[12,13],[0,14],[0,15],[14,16],[15,17]]


# load our serialized model from disk
print("[INFO] Loading model...")
net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])

# read the image
frame = cv2.imread(args["image"])

# specify the input image dimensions
frameHeight = frame.shape[0]
frameWidth = frame.shape[1]

# prepare and set the frame to be fed into the network
inputBlob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (frameWidth, frameHeight), (0, 0, 0), swapRB=False, crop=False)
net.setInput(inputBlob)

# make the predictions
output = net.forward()

# parsing the keypoints
H = output.shape[2]
W = output.shape[3]
points = []

for i in range(nPoints):
	# confidence map of the corresponding body part
	probMap = output[0, i, :, :]
	
	# find global maxima of the probMap
	minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)
	
	# scaling the point to fit the original image
	x = (frameWidth * point[0]) / W 
	y = (frameHeight * point[1]) / H
	
	if prob > args["threshold"]:
		cv2.circle(frame, (int(x), int(y)), 4, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)
		#cv2.putText(frame, "{}".format(i), (int(x)+10, int(y)+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, lineType=cv2.LINE_AA) uncomment to see the numbers
		
		# add the point to the list if prob > threshold
		points.append((int(x),int(y)))
	else:
		points.append(None)
		
# drawing the skeleton
for pair in POSE_PAIRS:
    partA = pair[0]
    partB = pair[1]

    if points[partA] and points[partB]:
        cv2.line(frame, points[partA], points[partB], (0, 255, 255), 1)
        cv2.circle(frame, points[partA], 4, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)
		
cv2.imshow("Output", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()