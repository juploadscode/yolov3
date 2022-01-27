Introduction:
This respoitory will show you how to create a custom object detector with the yolov3 model. 
Please be sure to check out the links below as they helped me create this project. 

eMaster Class Acadamey: https://www.youtube.com/channel/UCtfTf1nNJQ4PbUDqj-Q48rw
Murtaza's Workshop - Robotics and AI: https://www.youtube.com/c/MurtazasWorkshopRoboticsandAI
Darknet: https://pjreddie.com/darknet/
Darknet Github: https://github.com/pjreddie/darknet

You can use my convert_img_format, ebay_image_mass_download and make_txt python scripts to help improve your data.
*convert_img_format will make all files in a folder the same format.
*ebay_image_mass_download takes parameters and uses beautiful soup to download images from eBay.
*make_blank_txt will create blank txt files for samples with no detections.

Step 1 - Preparing Images: 
*Create a folder called 'images'. 
*Take screenshots of up to 100-500 images per class. For more complex datasets, use >= 1500 per class.
*The more data, the more accurate the model will be.
*Make sure screenshots are easy to see and offer variety. 
*Use https://www.makesense.ai/ to create image labels. 
*Mark a bounding box around the positive detections present in the image.
*Create or select a class and label the image with it's respective match.
*All labels must be consistent to provide the best results.  
*Once all images are marked accordingly, export the labels in yolo format. 
*Drag the labels into the 'images' folder and compress to zip.
*Add the 'images.zip' folder into a Google drive folder called 'yolov3'.
*Continue to the Google Colab workbook to start training the data. 

Step 2 - Open the 'train_yolov3_custom_dataset_colab.ipynb' file and follow the directions there.

Step 3 - After completeing everything in Step 2, open the main.py file and follow the directions there.
**I did not include my weights file due to the large file size.
