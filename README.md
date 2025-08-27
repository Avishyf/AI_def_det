# AI_def_det
AI PCB Defects Detector

# PCB Defect Detection with YOLOv8
This project implements an AI-based system for detecting defects on Printed Circuit Boards (PCBs) using the YOLOv8 object detection model. The system is designed to improve detection accuracy for high-ressolution images, especially for small defects, by processing the full image as well as multiple subdivided parts of the image and then consolidating the results.

# Key Features
YOLOv8 Integration: Utilizes the Ultralytics YOLOv8 model for high-performance object detection.

Multi-Scale Inference: The system runs inference on the full image, and then on 4, 8, and 16 smaller subdivisions of the image.

Non-Maximum Suppression (NMS): An Intersection over Union (IoU) based NMS algorithm is implemented to filter out duplicate detections from the multiple inference runs.

Automated Labeling: Detections are automatically labeled with class names and confidence scores and plotted onto the original image.

# Project Structure
train.py: This script is used to train the YOLOv8 model on a custom PCB defect dataset. It configures the training process, including epochs, batch size, image size, and various data augmentation settings.

find_defects.py: This is the main inference script. It loads the trained model and processes an input image. It performs detection on the full image and its subdivisions, applies Non-Maximum Suppression (NMS) to merge the results, and saves the final image with all detected defects highlighted.

weights/: Directory where the trained model weights (best.pt) are stored. (Note: You'll need to create this and place your trained model file here).

data/: Directory containing the custom dataset in the YOLO format (.yaml file, images, and labels).

# Getting Started
Prerequisites
- `Python 3.x`

- `PyTorch`

- `Ultralytics YOLO`

- `Pillow (PIL)`

- `NumPy`

You can install the necessary Python packages using pip:

```pip install ultralytics torch Pillow numpy```

1. Training the Model
Before running the detection, you need a trained model. The train.py script is set up for this.

you can use the trained model for this project by downloading the weights [here](https://drive.google.com/drive/folders/12jqr3LqfFm0V1ufZizrKv8oXLO_Pjz37?usp=drive_link) (its from outside of Git since it heavier than allowed here)

Place your custom dataset in a directory and update the data path in train.py to point to your data.yaml file.

edit your data.yaml file so it will point to the right directories where you store your data

Thw data needs to annonated, the way was chosen by us is with RoboFlow, our data is a mix of an exisiting data that we topped with our own addition

[the main dataset](https://universe.roboflow.com/hanxu-rgxfn/pcb22)

[our addition](https://app.roboflow.com/pcb-project-mqih2/custom-workflow-object-detection-bwd0k/browse?queryText=&pageSize=50&startingIndex=0&browseQuery=true)

the datat needs to be organized this way:
```
/data
├── /images
│   ├── /train
│   │   ├── image1.jpg
│   │   ├── image2.jpg
│   │   └── ...
│   ├── /val
│   │   ├── imageA.jpg
│   │   ├── imageB.jpg
│   │   └── ...
│   └── /test  (optional)
│       ├── imageX.jpg
│       └── ...
└── /labels
    ├── /train
    │   ├── image1.txt
    │   ├── image2.txt
    │   └── ...
    ├── /val
    │   ├── imageA.txt
    │   ├── imageB.txt
    │   └── ...
    └── /test  (optional)
        ├── imageX.txt
        └── ...
```
Run the training script:

`python train.py`

After training is complete, the best.pt file (the trained model weights) will be saved in runs/detect/PCB_det/weights/.

Our training results are

![](https://github.com/Avishyf/AI_def_det/blob/main/confusion_matrix_normalized.png)
![](https://github.com/Avishyf/AI_def_det/blob/main/test_results.png)
2. Defect Detection
Make sure the best.pt file from your training run is in the correct path as specified in `find_defects.py`.

Update the img_path variable in `find_defects.py` to point to the PCB image you want to analyze.

Run the detection script:

`python find_defects.py`

The script will print progress to the console and display the final image with the detected defects. A new image file will also be saved in the same directory.

![](https://github.com/Avishyf/AI_def_det/blob/main/output_detections.jpg)
