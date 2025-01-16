![logo_ironhack_blue 7](https://user-images.githubusercontent.com/23629340/40541063-a07a0a8a-601a-11e8-91b5-2f13e4e6b441.png)

# Waste Classification Project

This repository contains a Computer Vision project to classify waste images into "Recyclable" or "Household Waste." It employs transfer learning with MobileNetV2 and a custom-built pipeline for preprocessing, training, evaluation, and deployment.

---

## Table of Contents
1. [Overview](#overview)
2. [Dataset](#dataset)
3. [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
4. [Model Development](#model-development)
   - [Baseline Model](#baseline-model)
   - [Transfer Learning with MobileNetV2](#transfer-learning-with-mobilenetv2)
5. [Training and Evaluation](#training-and-evaluation)
6. [Deployment](#deployment)
7. [Usage](#usage)
   - [Training](#training)
   - [Prediction](#prediction)
8. [Files in Repository](#files-in-repository)
9. [Future Work](#future-work)

---

## Overview
This project aims to automate waste sorting by classifying images into two categories:
- **Recyclable**
- **Household Waste**

Key highlights:
- Comprehensive EDA for dataset understanding.
- Transfer learning with MobileNetV2.
- Deployment using Streamlit for user-friendly interaction.

---

## Dataset
The dataset consists of images organized into categories:
- **Recyclable:** Aluminum cans, glass bottles, etc.
- **Household Waste:** Food waste, plastic straws, etc.

### Dataset Organization
The dataset was split into:
- **Training**: 70%
- **Validation**: 15%
- **Test**: 15%

Images were preprocessed with unique names to avoid duplication and ensure consistency.

---

## Exploratory Data Analysis (EDA)
- Conducted using custom scripts in `eda_utils.py`.
- Key analyses include:
  - Image size and format.
  - Dataset distribution by categories.

---

## Model Development

### Baseline Model
A custom Convolutional Neural Network (CNN) was built to establish a baseline for classification performance.

### Transfer Learning with MobileNetV2
- **Architecture:** MobileNetV2 pre-trained on ImageNet.
- **Augmentation:** Applied transformations like rotation, zoom, and flipping to improve generalization.
- **Fine-tuning:** Enabled training on specific layers to adapt MobileNetV2 to the dataset.

---

## Training and Evaluation
The models were trained and evaluated with:
- **Metrics:** Accuracy, loss, precision, recall, and F1-score.
- **Regularization:** Dropout layers and learning rate scheduling.
- **Callbacks:** Early stopping and model checkpoints.

---

## Deployment
The model is deployed using Streamlit:
- **Interface:** Upload an image and classify it as "Recyclable" or "Household Waste."
- **Backend:** Uses a saved Keras model (`best_mobilenet_model.keras`) for inference.

### How to Run
```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py

---

## Usage

### Training
Run the notebook `MyTemplate.ipynb` to train and evaluate models:
- Edit paths to match your dataset structure.
- Experiment with different augmentation and transfer learning techniques.

### Prediction
Upload an image to the Streamlit app and receive a prediction with confidence.

---

## Files in Repository

| File                        | Description                                                           |
|-----------------------------|-----------------------------------------------------------------------|
| `requirements.txt `         | List of Python dependencies required for the project..                  |
| `MyTemplate.ipynb`          | Notebook for experimenting with the extended dataset.                |
| `eda_utils.py`              | Utility functions for EDA and dataset analysis.                      |
| `utils.py`                  | Helper functions for organizing images and assigning unique names.   |
| `app.py`                    | Streamlit application for deploying the classification model.         |
| `best_mobilenet_model.keras`| Pre-trained MobileNetV2 model saved after fine-tuning.               |

---

## Future Work
- **Model Optimization**: Test alternative architectures like ResNet or EfficientNet.
- **Data Expansion**: Incorporate more waste categories and diverse images.
- **Deployment**: Extend deployment to cloud platforms (e.g., AWS, Google Cloud).
