# Step 3 - Running the detector
# Credit to my teachers and the resources used to make this project <3
# eMaster Class Acadamey: https://www.youtube.com/channel/UCtfTf1nNJQ4PbUDqj-Q48rw
# Murtaza's Workshop - Robotics and AI: https://www.youtube.com/c/MurtazasWorkshopRoboticsandAI
# Darknet: https://pjreddie.com/darknet/
# Darknet Github: https://github.com/pjreddie/darknet


# Imports
import cv2
import numpy as np
import random
from time import time


# Color constants
BULBASAUR_BGR = (147, 200, 147)
SQUIRTLE_BGR = (171, 163, 85)
CHARMANDER_BGR = (62, 95, 241)
PIKACHU_BGR = (29, 214, 250)
GENGAR_BGR = (145, 24, 70)
GREEN = (0, 255, 0)


# Create flashing random colors
def random_box_colors() -> list:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = [r, g, b]
    return rgb


# Main
def main() -> None:
    # Set your best.weights or last.weights file and the yolov3_custom.cfg file.
    net = cv2.dnn.readNet('yolov3_training_five_classes_last.weights', 'yolov3_testing_five_classes.cfg')
    # Use opencv backend.
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
    # Set CPU as computation specific target.
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

    # Read in classes from txt file
    with open("classes_five_classes.txt", "r") as f:
        classes = list(f.read().splitlines())

    # Video input settings.
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    video_width = 640
    video_height = 360
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, video_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, video_height)
    cap.set(cv2.CAP_PROP_FPS, 60)
    # Set opencv font
    font = cv2.FONT_HERSHEY_PLAIN

    # FPS timer and blob input settings.
    timer = 0
    width_and_height_output_img = 320
    confidence_threshold = 0.4
    nms_threshold = 0.4

    # Main video loop.
    while True:
        # Read input and get size.
        _, img = cap.read()
        height, width, _ = img.shape

        # Create blob with parameters specified above.
        blob = cv2.dnn.blobFromImage(img, 1/255, (width_and_height_output_img, width_and_height_output_img), (0, 0, 0),
                                     swapRB=True, crop=False)
        # Set blob, output layer names and layer outputs.
        net.setInput(blob)
        output_layers_names = net.getUnconnectedOutLayersNames()
        layer_outputs = net.forward(output_layers_names)

        # Create boxes, confidences, and class_ids lists
        boxes = []
        confidences = []
        class_ids = []

        # For loops to look for detections
        for output in layer_outputs:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                # If detection, save results
                if confidence > confidence_threshold:
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append((float(confidence)))
                    class_ids.append(class_id)

        # Results.
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, confidence_threshold, nms_threshold)
        # Process results and set appropriate outputs for each class member identified.
        if len(indexes) > 0:
            for i in indexes.flatten():
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                rounded_confidence = round(confidences[i], 2)
                confidence = str(int(rounded_confidence * 100))
                if label == classes[0]:
                    cv2.rectangle(img, (x, y), (x + w, y + h), random_box_colors(), 2)
                    cv2.putText(img, label + " " + confidence + '%', (x, y - 10), font, 1, BULBASAUR_BGR, 2)
                if label == classes[1]:
                    cv2.rectangle(img, (x, y), (x + w, y + h), random_box_colors(), 2)
                    cv2.putText(img, label + " " + confidence + '%', (x, y - 10), font, 1, SQUIRTLE_BGR, 2)
                if label == classes[2]:
                    cv2.rectangle(img, (x, y), (x + w, y + h), random_box_colors(), 2)
                    cv2.putText(img, label + " " + confidence + '%', (x, y - 10), font, 1, CHARMANDER_BGR, 2)
                if label == classes[3]:
                    cv2.rectangle(img, (x, y), (x + w, y + h), random_box_colors(), 2)
                    cv2.putText(img, label + " " + confidence + '%', (x, y - 10), font, 1, PIKACHU_BGR, 2)
                if label == classes[4]:
                    cv2.rectangle(img, (x, y), (x + w, y + h), random_box_colors(), 2)
                    cv2.putText(img, label + " " + confidence + '%', (x, y - 10), font, 1, GENGAR_BGR, 2)

        # Create and display FPS timer
        fps_timer = time()
        if (fps_timer - timer) > 0:
            fps = 1.0 / (fps_timer - timer)
            cv2.putText(img, 'FPS: {}'.format(int(fps)), (10, 30), font, 2, GREEN, 3)
        timer = fps_timer

        # Show video input + escape sequence code.
        cv2.imshow('Pokemon Card Detector', img)
        key = cv2.waitKey(1)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


# Run main.py()
if __name__ == '__main__':
    main()
