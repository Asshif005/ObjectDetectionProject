# Object Detection System

## Project Overview

This project implements a real-time object detection system using the COCO 2017 dataset and a YOLO object detection model.

The system is designed to identify multiple objects from images and live webcam video. The project follows the main stages of a computer vision pipeline, including dataset preparation, preprocessing, model training, validation, performance evaluation and real-time detection.

## Dataset

The project uses the COCO 2017 object detection dataset.

- Dataset: COCO 2017
- Number of classes: 80
- Task: Object Detection
- Annotation type: Bounding boxes

Examples of detectable objects include:

- Person
- Car
- Bicycle
- Dog
- Cat
- Bottle
- Laptop
- Cell phone
- Cup
- Book
- Bus
- Truck

The complete COCO 2017 dataset is not included in this repository because of its large size.

## Computer Vision Pipeline

The project follows this pipeline:

COCO 2017 Dataset  
↓  
Dataset Preparation  
↓  
Annotation Conversion  
↓  
Preprocessing  
↓  
YOLO Model Training  
↓  
Validation  
↓  
Performance Evaluation  
↓  
Real-Time Webcam Detection

## Preprocessing

The original COCO annotations were converted into a YOLO-compatible format.

The dataset was organised into training, validation and testing data. Bounding-box annotations were used to teach the model the location and class of each object.

## Model

YOLO (You Only Look Once) was used as the object detection model.

The trained model predicts:

1. The object class
2. The location of the object
3. The confidence score

## Training

The model was trained using the prepared COCO dataset.

Training performance was monitored using:

- Training loss
- Validation loss
- Precision
- Recall
- mAP@50
- mAP@50-95

## Performance Results

The final training results were approximately:

| Metric | Result |
|---|---:|
| Precision | ~88% |
| Recall | ~75% |
| mAP@50 | ~82% |
| mAP@50-95 | ~70% |

The results show that the model can detect multiple COCO object categories with reasonable performance.

## Real-Time Detection

The trained model was also tested using a webcam.

The system can detect multiple objects in real time, including bottles, people and other COCO categories.

The webcam application can be started using:

```bash
py test_webcam.py

Press Q to close the webcam detection window.

Project Files
File	Description
train.py	Trains the YOLO object detection model
test_webcam.py	Runs real-time webcam detection
detect.py	Runs object detection on images
webcam.py	Webcam detection implementation
convert_coco.py	Converts COCO annotations to YOLO format
check_phone.py	Checks cell phone annotations
data.yaml	Dataset configuration
.gitignore	Prevents large datasets and model files from being uploaded
Installation

Install the required Python packages:

py -m pip install ultralytics
py -m pip install opencv-python
py -m pip install matplotlib
py -m pip install pandas
How to Run
1. Train the model
py train.py
2. Run object detection
py detect.py
3. Run real-time webcam detection
py test_webcam.py

The webcam will open and the model will detect objects in real time.

Press Q to exit the webcam.

Dataset Availability

The COCO 2017 dataset is not included in this GitHub repository because it is very large.

The dataset remains stored locally on the computer used for training.

Results

The trained model successfully detects multiple objects from the COCO dataset, including people, bottles, cars, laptops, cell phones and other object categories.

The model was evaluated using precision, recall, mAP@50 and mAP@50-95.

Conclusion

This project demonstrates a complete object detection system using YOLO and the COCO 2017 dataset.

The project includes dataset preparation, annotation conversion, model training, validation, performance evaluation and real-time webcam detection.