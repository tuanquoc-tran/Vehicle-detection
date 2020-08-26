# Run: python3 image.py --image images/image10.jpg
import cv2
import time 
import numpy as np
import argparse

# Build the argument parse
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
    help="path to input image")
args = vars(ap.parse_args())

# Define class and color of object
classes = ["Bus","XeKhach","XeMay","XeOto","XeTai","XeBaGac","XeChuyenDung","XeDap","XeContainer"]
colors = {"Bus":(255,255,0),"XeKhach":(255,0,255),"XeMay":(0,255,255),"XeOto":(0,0,255),"XeTai":(0,255,0),"XeBaGac":(255,0,0),"XeChuyenDung":(125,125,0),"XeDap":(125,0,125),"XeContainer":(0,125,125)}

# Load yolov3-tiny weight and config of dataset Vietnam's traffic
weightsPath = 'weights/yolov3_tiny_training_150000.weights'
configPath = 'cfg/yolov3_tiny_training.cfg'
net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)

# Get class object in model
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

# Load the image
image = cv2.imread(args["image"])
# Get dimension of image
height,width = image.shape[:2]

# Detect object
start_time=time.time()
blob = cv2.dnn.blobFromImage(image, 0.00392, (416,416), (0, 0, 0), True, crop=False)
net.setInput(blob)
outs = net.forward(output_layers)
end=time.time()

class_ids = []
confidences = []
boxes = []
# extract output 
for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.25:
            # Object detected
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)

            # Rectangle coordinates
            x = int(center_x - w / 2)
            y = int(center_y - h / 2)

            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
for i in range(len(boxes)):
    if i in indexes:
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])
        color=colors[label]
        cv2.rectangle(image, (x, y), (x + w, y + h), color, 1)
        font = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(image, label, (x, y), font, 0.5, color, 1)

# Show the image 
cv2.imshow("Image",image)
cv2.waitKey(0)