# Run: python3 video.py --video videos/video1.mp4
import cv2
import time
import numpy as np
import argparse

# Load yolov3-tiny weight and config of dataset Vietnam's traffic
weightsPath = 'weights/yolov3_tiny_training_150000.weights'
configPath = 'cfg/yolov3_tiny_training.cfg'
net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)

# Load class and color of object
classes = ["Bus","XeKhach","XeMay","XeOto","XeTai","XeBaGac","XeChuyenDung","XeDap","XeContainer"]
colors = {"Bus":(255,255,0),"XeKhach":(255,0,255),"XeMay":(0,255,255),"XeOto":(0,0,255),"XeTai":(0,255,0),"XeBaGac":(255,0,0),"XeChuyenDung":(125,125,0),"XeDap":(125,0,125),"XeContainer":(0,125,125)}

layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

def predict(img):
    height, width, channels = img.shape

    # Detecting objects
    start_time=time.time()
    blob = cv2.dnn.blobFromImage(img, 0.00392, (320,320), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)
    end=time.time()
    # Processing speed (FPS)
    print("FPS : {:.2}".format(1/(end-start_time)))

    class_ids = []
    confidences = []
    boxes = []
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
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 1)
            font = cv2.FONT_HERSHEY_PLAIN
            cv2.putText(img, label, (x, y), font, 0.5, color, 1)
    return img


if __name__ == "__main__":
    # Build the argument parse
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--video", required=True,
    help="path to input image")
    args = vars(ap.parse_args())

    
    videosPath = args["video"]
    cap = cv2.VideoCapture(videosPath)

    if (cap.isOpened()== False): 
        print("Error opening video stream or file")

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            frame = predict(frame)
            cv2.imshow('Frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('b'):
                break
        else: 
            break
    cap.release()
