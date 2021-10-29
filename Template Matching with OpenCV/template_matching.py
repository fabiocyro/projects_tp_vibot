# Template Matching with OpenCV

# USAGE
# python template_matching.py -i <your_image> -t <your_template>

# importing necessary packages
import cv2
import argparse

# initiatize argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required = True, help = "Path to the input image")
ap.add_argument("-t", "--template", type=str, required = True, help = "Path to the template image")
args = vars(ap.parse_args())

# load both image and template and display on the screen
print("[INFO] Loading images...")
image = cv2.imread(args['image'])
template = cv2.imread(args['template'])
cv2.imshow("Image", image)
cv2.imshow("Template to search", template)

# convert both to grayscale
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

# perform template matching
print("[INFO] Performing template matching...")
result = cv2.matchTemplate(imageGray, templateGray, cv2.TM_CCOEFF_NORMED)
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)

# determine the starting end ending (x, y)-coordinates of the bounding box
(startY, startX) = maxLoc
endX = startX + template.shape[1]
endY = startY + template.shape[0]

# drawing the rectangle (Since the maximum points are detected exactly on the middle of the image/template, the addition of 25 pixels was
# to compensate this and draw the rectangle on the beginning of the match
cv2.rectangle(image, (startX - 25, startY + 25), (endX - 25, endY + 25), (255, 0, 0), 3)

# show the output
cv2.imshow("Output", image)
cv2.waitKey(0)

