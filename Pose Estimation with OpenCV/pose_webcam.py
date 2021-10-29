######################## ATTENTION #######################################################
# To run this you will need GPU (and risk it to not run decently)

# USAGE
# python pose_video.py -p deploy.prototxt.txt -m pose_iter_440000.caffemodel

# import the necessary packages
from imutils.video import VideoStream
import numpy as np
import argparse
import imutils
import time
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser(description = "Run your pose estimation algorithm for webcam")
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

# initialize the video stream and allow the camera sensor to warm up
print("[INFO] Starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)

# loop over the frames from the video stream
while True:
	# grab the frame from the threaded video stream and resize it
	# to have a maximum width of 400 pixels
	frame = vs.read()
	frame = imutils.resize(frame, width=400)
	
	# specify the input image dimensions
	frameHeight = frame.shape[0]
	frameWidth = frame.shape[1]
 
	# grab the frame dimensions and convert it to a blob
	(h, w) = frame.shape[:2]
	blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0,
		(300, 300), (104.0, 177.0, 123.0))
 
	# pass the blob through the network and obtain the detections and
	# predictions
	net.setInput(blob)
	detections = net.forward()
    

	# parsing the keypoints
	H = detections.shape[2]
	W = detections.shape[3]
	points = []

	for i in range(nPoints):
		# confidence map of the corresponding body part
		probMap = detections[0, i, :, :]
		
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

	# show the output frame
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
 
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
 
# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()