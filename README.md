# YOLO-NAS Bacteria Detection

This project explores object detection using the YOLO-NAS model on a custom dataset of bacterial colonies.

## 🔍 Project Summary

- This repository contains the configuration and training scripts for object detection using YOLO-NAS and SuperGradients.

- train_yolonas_custom.py: Python script to initiate training using SuperGradients.

- yolonas_train.yaml: YAML configuration file for model architecture, dataset paths, and training parameters.

- split_dataset.py: Optional script to split your dataset into training and validation sets.

- The dataset is not included due to privacy policy, but the required directory structure is described in the documentation.

Uses YOLO format annotations and is intended for custom object detection, specifically detecting bacterial colonies.

## 📁 Dataset Structure (not included)

Due to privacy policies, the dataset is excluded. Expected structure:

``` dataset/ 
├── images/
    ├── train/ │ 
    └── val/ 
├── labels/ │ 
    ├── train/ │
    └── val/ 
``` </pre>

